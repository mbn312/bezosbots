#!/usr/bin/env python
import rospy
import math
import numpy as np
from geometry_msgs import Pose2D,PoseStamped,PoseWithCovarianceStamped

targets = [(5,0),(10,0),(13,0),(16.7,3),(16.7,8),(16.7,),(16.7,13),(16.7,18),(16.7,23),(13,24.5),(10,24.5),
           (5,24.5),(0,24.5),(-5,24.5),(-10,24.5),(-13,24.5),(-16.7,23),(-16.7,18),(-16.7,13), (-16.7,8),
           (-16.7,5),(-16.7,3),(-13,0),(-10,0),(-5,0),(0,0)]
cur_goal = None
proximity = (0.2,0.1)
goalPub = rospy.Publisher("/move_base_simple/goal",PoseStamped)

def global_planner(data):
    global targets,cur_goal
    #pose = data.data[:2]
    pose = (data.pose.position.x,data.pose.position.y)
    if cur_goal is None:
        cur_goal = targets.pop(0)
        #talker(pose,cur_goal,False)
    else:
        #calculating error
        rho = np.linalg.norm(np.array(pose)-np.array(cur_goal))

        #checking to see if robot is within 0.2 meters of current goal
        if rho < proximity[0]:
            #updates goal if there are still targets left
            if len(targets) != 0:
                cur_goal = targets.pop(0)
                goal = PoseStamped()
                goal.pose.position.x = cur_goal[0]
                goal.pose.position.y = cur_goal[1]
                goalPub.publish(g)
                #talker(pose,g,False)
            elif rho < proximity[1]:
                rospy.signal_shutdown("goal reached.")

# def talker(pose,goal,done):
#     global cur_goal,publisher
#     if not done:
#         msg = ("New Goal: %s" % goal)
#         rospy.loginfo(msg)
#     goalPub.publish(goal)
    #msg = np.array((pose + goal),dtype=np.float32)
    #publisher.publish(msg)

def listener():
    rospy.init_node("global_path", anonymous=True)
    rospy.Subscriber("/initialpose", PoseWithCovarianceStamped, global_planner)
    rospy.spin()

if __name__ == "__main__":
    listener()