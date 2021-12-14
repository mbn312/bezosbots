#!/usr/bin/env python  
import roslib
roslib.load_manifest('fix_q')
import rospy

import tf
from geometry_msgs.msg import Quaternion
from sensor_msgs.msg import Imu

def imu_pub(msg):
    pub = rospy.Publisher('/imu/data',Imu,queue_size=0)
    #rospy.init_node('handle_imu', anonymous=True)
    #rate = rospy.Rate(2) # Hz
    #while not rospy.is_shutdown():
    msg.orientation.x = 0
    msg.orientation.y = 0
    msg.orientation.z = 0
    msg.orientation.w = 1
    pub.publish(msg)
        #rate.sleep()
    

if __name__ == '__main__':
    rospy.init_node('imu_pub')
    rospy.Subscriber('/imu_data',
                     Imu,
                     imu_pub)
    rospy.spin()
