#!/usr/bin/env python
# license removed for brevity
import rospy
from ctrl_pkg.msg import ServoCtrlMsg
from std_msgs.msg import Float64
import numpy as np
import signal

pub = rospy.Publisher('/manual_drive', ServoCtrlMsg, queue_size=10)
angle = 0.0
throttle = .5
err_array = []
d_errSum = 0.0
err_prev = 0.0

def control_data_input(msg):
    global angle
    global throttle
    global err_array
    global d_errSum
    global err_prev

    throttle_max = 0.5
#    throttle_min = 0.0
    err = msg.data
#    err_array.append(err)
    d_err = err - err_prev
    d_errSum += err
    cntrl = ServoCtrlMsg()
    t_p = 1.5
    p = 1
    g_I = 0.0
    g_D = 0

#    if (err <= abs(0.8)):
#        p = 0.1
#    if (err < 0):
#        throttle = throttle - err
#    if (err > 0):
#        throttle = throttle - t_p*err

    angle = (p*err + g_I*d_errSum + g_D*d_err)

#    if (throttle > throttle_max):
    throttle = throttle_max
#    if (throttle < throttle_min):
#        throttle = throttle_min
    if (abs(err) < 0.01):
        throttle = throttle_max
        angle = 0.0
    if (angle < -1.0):
        angle = -1.0
    if (angle > 1.0):
        angle = 1.0
#    if (len(err_array) >= 2 and throttle == throttle_min and abs(err_array[-1]) - abs(err_array[-2]) == 0):
#        print("WERE STUCK!")
#        throttle = 0.8
#        err_array = []
#    if (abs(err) > 0.1):
#        p += 2
#    rospy.loginfo("angle: %s, error: %s", angle, err)

    err_prev = err
    cntrl.throttle = throttle
    cntrl.angle = angle #np.clip(angle,-1.0,1.0)
    pub.publish(cntrl)

def throttle_input(msg):
    msg.throttle = np.clip(msg.throttle,0.0,0.4)
    pub.publish(msg)

def end(sig, frame):
    cntrl = ServoCtrlMsg()
    cntrl.angle = 0.0
    cntrl.throttle = 0.0
    pub.publish(cntrl)
    rospy.signal_shutdown("ended")

if __name__ == '__main__':
    rospy.init_node('manual_drive')
    signal.signal(signal.SIGINT, end)
    signal.signal(signal.SIGTERM, end)
    rospy.Subscriber('/error',
                    Float64,
                    control_data_input)
    rospy.Subscriber('/new_manual_drive',
                    ServoCtrlMsg,
                    throttle_input)
    rospy.spin()

