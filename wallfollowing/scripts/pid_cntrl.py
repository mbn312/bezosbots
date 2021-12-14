#!/usr/bin/env python
# license removed for brevity
import rospy
from ctrl_pkg.msg import ServoCtrlMsg
from std_msgs.msg import Float64, Float64MultiArray
import numpy as np
import signal

pub = rospy.Publisher('/manual_drive', ServoCtrlMsg, queue_size=10)
rospy.init_node('manual_drive')

def end(sig, frame):
    cntrl = ServoCtrlMsg()
    cntrl.angle = 0.0
    cntrl.throttle = 0.0
    pub.publish(cntrl)
    rospy.signal_shutdown("ended")

def control_data_input(msg):
    global pub
    left_err = msg.data[0]
    amount_inf = msg.data[1]
    top_err = msg.data[2]
    top_amount_inf = msg.data[3]
    right_err = msg.data[4]
    right_amount_inf = msg.data[5]
    left_err_rinf = msg.data[6]
    cntrl = ServoCtrlMsg()
    cntrl.throttle = .9
    middle_err = right_err - left_err
    p = .28
    dist = 1.6
    err = dist - left_err
    #if top_amount_inf >= 6:
    #   print('top amount')
    #   err = err
    #   if amount_inf >= 20:
    #     print('amount inf')
    #     err = 0
    #if top_amount_inf < 6:
    #   print('top close')
    #   err = dist - left_err_rinf
    angle = -p*(err)
    print(angle)
    #if top_err < 1:
    #   angle = 1
    #   print('Oh no!')
    cntrl.angle = np.clip(angle, -1.0, 1.0)
    pub.publish(cntrl)


def throttle_input(msg):
    msg.throttle = np.clip(msg.throttle, 0.0, 0.4)
    pub.publish(msg)


def control_data_input_end(msg):
    cntrl = ServoCtrlMsg()
    cntrl.throttle = 0.0
    angle = 0.0
    cntrl.angle = np.clip(angle, -1.0, 1.0)
    pub.publish(cntrl)


if __name__ == '__main__':
    rospy.Subscriber('/error', Float64MultiArray, control_data_input)
    rospy.Subscriber('/new_manual_drive', ServoCtrlMsg, throttle_input)
    signal.signal(signal.SIGINT, end)
    signal.signal(signal.SIGTERM, end)    
    rospy.spin()
