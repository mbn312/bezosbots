#!/usr/bin/env python
# Referenced for publishing odom: https://gist.github.com/atotto/f2754f75bedb6ea56e3e0264ec405dcf
from ctrl_pkg.msg import ServoCtrlMsg
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, Vector3, TransformStamped
from nav_msgs.msg import Odometry
from sensor_msgs.msg import Imu
import tf
from math import sin, cos, tan, pi
import rospy
import roslib
import copy
roslib.load_manifest('fix_q')


class Node(object):
	def __init__(self):
		self.x_0 = 0.0
		self.y_0 = 0.0
		self.thet_0 = 0.0
		self.vel = 0
		self.angle = 0
	# Setup rate how rospy does here with self
		rospy.init_node('odom_pub')
		self.rate = rospy.Rate(10)
		rospy.Subscriber('/manual_drive',
                     ServoCtrlMsg,
                     self.control_data_input)
		rospy.Subscriber('/imu/data',
                     Imu,
                     self.imu_data_input)
		self.current_time = rospy.Time.now()
		self.last_time = rospy.Time.now()
		self.odom_broadcaster = tf.TransformBroadcaster()
		self.odom_quat = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
		self.ang_rate = 0.0


	def control_data_input(self, msg):
		throttle = msg.throttle
		# print(msg.angle)
		conversion = -2.5#####
		self.vel = conversion*throttle
		a_conv = 0.523599
		# self.angle = a_conv*msg.angle*0.25
		self.angle = 0
		self.odom_pub()
		# print("in data_inputs")
	
	def imu_data_input(self, msg):
		self.odom_quat = msg.orientation
		self.ang_rate = msg.angular_velocity.z
		self.odom_pub()
	
	def odom_pub(self):
		self.current_time = rospy.Time.now()
		# print(Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0)))
		# print(self.current_time)
		# print(rospy.Time.now())
		# print(self.last_time)
		[_,_,a3] = tf.transformations.euler_from_quaternion([self.odom_quat.x,self.odom_quat.y,self.odom_quat.z,self.odom_quat.w])
		# print(a3)
		dt = (self.current_time-self.last_time).to_sec()
		# print(dt)
		pub = rospy.Publisher('odom',Odometry,queue_size=10)
	    
		x_d = self.vel*cos(a3)#self.thet_0)
		y_d = self.vel*sin(a3)#self.thet_0)
		# whl_bs = 0.15 #15cm wheelbase ######
		# thet_d = self.vel/whl_bs*tan(self.angle)
	    
		x = self.x_0 + dt*x_d
		y = self.y_0 + dt*y_d
		thet = self.thet_0 + dt*self.ang_rate
		# print(x_d,y_d)
		# print(x,y)
		# odom_trans = TransformStamped()
		# odom_trans.header.stamp = self.current_time
		# odom_trans.header.frame_id = "odom"
		# odom_trans.child_frame_id = "base_link"
		# odom_trans.transform.translation.x = x
		# odom_trans.transform.translation.y = y
		# odom_trans.transform.translation.z = 0.0
		# odom_trans.transform.rotation = self.odom_quat
		# self.odom_broadcaster.sendTransform(odom_trans)

		odom = Odometry()
		# odom_quat = tf.transformations.quaternion_from_euler(0, 0, thet)
		# print(self.odom_quat)
		# print(type(self.odom_quat))
		self.odom_broadcaster.sendTransform(
        (x, y, 0.),
        [self.odom_quat.x,self.odom_quat.y,self.odom_quat.z,self.odom_quat.w],
    	self.current_time,
        "base_link",
        "odom"
    	)
		odom.header.stamp = self.current_time
		odom.header.frame_id = "odom"
		# odom.pose.pose = Pose(Point(x, y, 0.), Quaternion(*self.odom_quat))
		odom.pose.pose.orientation = self.odom_quat
		odom.pose.pose.position.x = x
		odom.pose.pose.position.y = y
		odom.pose.pose.position.z = 0.
		odom.pose.covariance = [ 2.0, 0.0, 0.0, 0.0, 0.0, 0.0,
								 0.0, 4.0,0.0, 0.0, 0.0, 0.0,
								 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
								 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
								 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
								 0.0, 0.0, 0.0, 0.0, 0.0, 0.5]
		odom.child_frame_id = "base_link"
		odom.twist.twist = Twist(Vector3(x_d, y_d, 0), Vector3(0, 0, self.ang_rate))
		pub.publish(odom)
    
		self.last_time = copy.copy(self.current_time)
		self.x_0 = x
		self.y_0 = y
		self.thet_0 = thet
		# print("in odom pub")
	    
	def pubandsleep(self):
		while not rospy.is_shutdown():
			self.odom_pub()
    		# Need the right sleep func here
			self.rate.sleep()
			# print("pubandsleep")
    
if __name__ == '__main__':
    test = Node()
    test.pubandsleep()
