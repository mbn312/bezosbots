#!/usr/bin/env python
# license removed for brevity
import rospy
from ctrl_pkg.msg import ServoCtrlMsg
import numpy as np

pub = rospy.Publisher('/manual_drive', ServoCtrlMsg, queue_size=10)

def control_data_input(msg):
    msg.throttle = np.clip(msg.throttle,0.0,0.5)
    # msg.throttle = 0.3
    pub.publish(msg)

if __name__ == '__main__':
    rospy.init_node('manual_drive')
    rospy.Subscriber('/new_manual_drive',
                    ServoCtrlMsg,
                    control_data_input)
    rospy.spin()

   
