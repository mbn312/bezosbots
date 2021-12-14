#!/usr/bin/env python
# Referenced for publishing odom: https://gist.github.com/atotto/f2754f75bedb6ea56e3e0264ec405dcf
from ctrl_pkg.msg import ServoCtrlMsg
from geometry_msgs.msg import Point, Pose, Quaternion, Twist, TwistStamped, Vector3, TransformStamped
# from nav_msgs.msg import Odometry
# from sensor_msgs.msg import Imu
import tf
from math import sin, cos, tan, pi
import rospy
import roslib
import copy
roslib.load_manifest('localization')


class Node(object):
    def __init__(self):
        self.x_0 = 0.0
        self.y_0 = 0.0
        self.thet_0 = 0.0
        self.vel =  0.0
        self.odom_quat = Quaternion(*tf.transformations.quaternion_from_euler(0, 0, 0))
    # Setup rate how rospy does here with self
        rospy.init_node('odom_pub')
        self.rate = rospy.Rate(10)
        rospy.Subscriber('/manual_drive',
                         ServoCtrlMsg,
                         self.control_data_input)
        # rospy.Subscriber('/imu/data',
        #                  Imu,
        #                  self.imu_data_input)

    def control_data_input(self, msg):
        throttle = msg.throttle
        if throttle < 0:
            throttle = 0
        conversion = -1.0
        self.vel = conversion*throttle
        self.odom_pub()

    # def imu_data_input(self, msg):
    #     self.odom_quat = msg.orientation
    #     self.odom_pub()

    def odom_pub(self):
        self.current_time = rospy.Time.now()
        # [_, _, self.thet_0] = tf.transformations.euler_from_quaternion(
            # [self.odom_quat.x, self.odom_quat.y, self.odom_quat.z, self.odom_quat.w])
        self.thet_0 = 0.0
        pub = rospy.Publisher('vel', Twist, queue_size=10)

        x_d = self.vel*cos(self.thet_0)
        y_d = self.vel*sin(self.thet_0)

        tvel = Twist()
        # tvel.header.stamp = self.current_time
        # tvel.header.frame_id = "vel"
        # tvel.twist 
        tvel = Twist(Vector3(x_d, y_d, 0), Vector3(0, 0, 0))
        # odom.twist.covariance = [10.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        #                          0.0, 20.0, 0.0, 0.0, 0.0, 0.0,
        #                          0.0, 0.0, 0.0, 0.0, 0.0, 0.0,
        #                          0.0, 0.0, 0.0, 3.0, 0.0, 0.0,
        #                          0.0, 0.0, 0.0, 0.0, 3.0, 0.0,
        #                          0.0, 0.0, 0.0, 0.0, 0.0, 3.0]
        pub.publish(tvel)

    def pubandsleep(self):
        while not rospy.is_shutdown():
            self.odom_pub()
            self.rate.sleep()


if __name__ == '__main__':
    test = Node()
    while not rospy.is_shutdown():
        rospy.spin()
    # test.pubandsleep()
