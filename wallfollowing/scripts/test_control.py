#!/usr/bin/env python 
import sensor_msgs.point_cloud2 as pc2
import rospy
from sensor_msgs.msg import PointCloud2, LaserScan
from std_msgs.msg import Float64, Float64MultiArray, MultiArrayDimension, MultiArrayLayout
import laser_geometry.laser_geometry as lg
import math
import numpy as np
import signal

rospy.init_node("dumb_control")

ybar = 0
ytar = 0.0 #1.5


angleStart =  -np.pi/2 - np.pi/6
angleEnd = -np.pi/2 + np.pi/6

tangleStart = angleStart - np.pi/4.0
tangleEnd = angleStart + np.pi/9

bangleStart = angleEnd - np.pi/6
bangleEnd = angleEnd + np.pi/5

angleStartRight = np.pi/2 - np.pi/6
angleEndRight = np.pi/2 + np.pi/6
angleStartTop =  -0.122173 + np.pi
angleEndTop = 0.122173 + np.pi


pub = rospy.Publisher('error', Float64MultiArray, queue_size=1)

def calculateMean(arr, angleS, angle_increment):
  tempArr = []
  for num, i in enumerate(arr):
    test = np.abs(i*np.sin(angleS+num*angle_increment))
    if np.isfinite(test):
      tempArr.append(test)
  mean = 0
  if len(tempArr) != 0:
    mean = np.mean(tempArr)
  return (mean, len(arr) - len(tempArr))


def laser_sub(msg):
  global ybar
  global ytar
  global angleStart
  global angleEnd
  global angleStartRight
  global angleEndRight
  global angleStartTop
  global angleEndTop
  global pub
  #rospy.loginfo(msg.angle_min)
  #rospy.loginfo(msg.angle_max)
  range_min = int((angleStart - msg.angle_min)/msg.angle_increment)
  range_max = int((angleEnd - msg.angle_min)/msg.angle_increment)
  trange_min = int((tangleStart - msg.angle_min)/msg.angle_increment)
  trange_max = int((tangleEnd - msg.angle_min)/msg.angle_increment)
  brange_min = int((bangleStart - msg.angle_min)/msg.angle_increment)
  brange_max = int((bangleEnd - msg.angle_min)/msg.angle_increment)
  range_min_top = int((angleStartTop - msg.angle_min)/msg.angle_increment)
  range_max_top = int((angleEndTop - msg.angle_min)/msg.angle_increment)
  range_min_right = int((angleStartRight - msg.angle_min)/msg.angle_increment)
  range_max_right = int((angleEndRight - msg.angle_min)/msg.angle_increment)
  #rospy.loginfo('min = ' + str(range_min))
  #rospy.loginfo(range_max)
  ranges = msg.ranges[range_min:range_max]
  rangesTop = msg.ranges[range_min_top:range_max_top]
  rangesRight = msg.ranges[range_min_right:range_max_right]
  #rospy.loginfo(rangesTop)
  #rospy.loginfo(ranges)
  rangesTop2 = np.clip(rangesTop, msg.range_min, msg.range_max)
  ranges2 = np.clip(ranges, msg.range_min, msg.range_max)
  rangesRight2 = np.clip(rangesRight, msg.range_min, msg.range_max)

  tbar, infCountT = calculateMean(rangesTop, angleStartTop, msg.angle_increment)
  rbar, infCountR = calculateMean(rangesRight, angleStartRight, msg.angle_increment)
  tybar, tinfCountL = calculateMean(msg.ranges[trange_min:trange_max], angleStart, msg.angle_increment)
  bybar, binfCountL = calculateMean(msg.ranges[brange_min:brange_max], angleStart, msg.angle_increment)
  ybar = tybar# (tybar + bybar) /2
  infCountL = tinfCountL #tinfCountL + binfCountL
  calculateMean(rangesTop2, angleStartTop, msg.angle_increment)
  left_rounded, _ = calculateMean(ranges2, angleStart, msg.angle_increment)
  calculateMean(rangesRight2, angleStartRight, msg.angle_increment)
    
  #rospy.loginfo(ybar)
  newmsg = Float64MultiArray()
  #newmsg.layout.data_offset = 0
  #newmsg.layout.dim = [MultiArrayDimension(), MultiArrayDimension()]
  #newmsg.layout.dim[0].size = int(2)
  #newmsg.layout.dim[1].size = int(2)
  #newmsg.layout.dim[0].label = 'fuck1'
  #newmsg.layout.dim[1].label = 'fuck2'
  #newmsg.layout.dim[0].stride = 8
  #newmsg.layout.dim[1].stride = 8
  newmsg.data = [float(ybar),float(infCountL), float(tbar),float(infCountT), float(rbar), float(infCountR), float(left_rounded)]
  print(newmsg)
  pub.publish(newmsg)
  #print([[ytar-ybar,len(ranges)-len(tempArr)],[tbar,len(rangesTop)-len(tempArrTop)]])

rospy.Subscriber('scan', LaserScan, laser_sub, queue_size=1) 
rospy.spin()
