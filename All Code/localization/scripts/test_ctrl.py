#!/usr/bin/env python
# license removed for brevity
import rospy
from ctrl_pkg.msg import ServoCtrlMsg

def talker():
    pub = rospy.Publisher('/manual_drive', ServoCtrlMsg, queue_size=0)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        control = ServoCtrlMsg()
        control.throttle = 0.2
        control.angle = -1.0
        pub.publish(control)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass