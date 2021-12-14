#!/usr/bin/env python
# license removed for brevity
import rospy
from ctrl_pkg.msg import ServoCtrlMsg
from std_msgs.msg import Float64
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

signal.signal(signal.SIGINT, end)
signal.signal(signal.SIGTERM, end)
last_err = 0.0

def control_data_input(msg):
    global last_err
    err = msg.data
    if last_err == 0:
        de = 0
    else:
        de = err - last_err 
    cntrl = ServoCtrlMsg()
    cntrl.throttle = .5
    p = .75
    Kd = .5
    if abs(err)<0.1:
        p = 0
        Kd = 4
    elif abs(err)>4:
        p = 2
        Kd = 0
    angle = -p*(err-.25) + Kd*de
    last_err = err
    cntrl.angle = np.clip(angle,-1.0,1.0)
    pub.publish(cntrl)

def throttle_input(msg):
    msg.throttle = np.clip(msg.throttle,0.0,0.4)
    pub.publish(msg)

def control_data_input_end(msg):
    cntrl = ServoCtrlMsg()
    cntrl.throttle = 0.0
    angle = 0.0
    cntrl.angle = np.clip(angle,-1.0,1.0)
    pub.publish(cntrl)

if __name__ == '__main__':
    while not rospy.is_shutdown():
        try:
            rospy.Subscriber('/error', Float64, control_data_input)
            rospy.Subscriber('/new_manual_drive', ServoCtrlMsg, throttle_input)
	    rate = rospy.Rate(10) #10Hz
	    rate.sleep()
        except rospy.ROSInterruptException:
	    print("Ending PID Control")
            rospy.Subscriber('/error', Float64, control_data_input_end)
            rospy.Subscriber('/new_manual_drive', ServoCtrlMsg, throttle_input)
	    pass
