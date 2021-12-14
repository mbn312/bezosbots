#!/usr/bin/env python
import rospy
from std_msgs.msg import Float32MultiArray
from rospy.numpy_msg import numpy_msg
from nav_msgs.msg import OccupancyGrid

class Node(object):
    def __init__(self):
        self.listener()
        self.publisher = rospy.Publisher("/controller",numpy_msg(Float32MultiArray))
        self.interval = 10
        self.padding = 25
        self.map = None

    def local_planner(self,start,goal,map,pixels):
#         closedSet = []
#         openSet = [start]
        closedSet = {}
        openSet = {start:np.inf}
        cameFrom = {start:None}

        gScore = {(i,j):np.inf for i in range(pixels[0]) for j in range(pixels[1])}
        gScore[start] = 0

#         fScore = {(i,j):np.inf for i in range(pixels[0]) for j in range(pixels[1])}
#         fScore[start] = np.linalg.norm(np.array(start)-np.array(end))
        openSet[start] = np.linalg.norm(np.array(start)-np.array(end))

        while len(openSet) != 0:
#             current = openSet[0]
#
#             for x in openSet:
#                 if fScore[x] < fScore[current]:
#                     current = x
            current = min(openSet, key=openSet.get)

            if current == end:
                path = [current]
                while cameFrom[current] is not None:
                    path.append(cameFrom[current])
                    current = cameFrom[current]
                path.reverse()
                return np.array(path,dtype=np.float32)

#             openSet.remove(current)
#             closedSet.append(current)

            closedSet[current] = openSet[current]
            openSet.pop(current)

            for neighbor in get_neighbors(map,current):
                if neighbor not in closedSet:
#                     if neighbor not in openSet:
#                         openSet.append(neighbor)
                    if neighbor not in openSet:
                        openSet[neighbor] = np.inf

                    tent_gScore = gScore[current] + np.linalg.norm(np.array(current)-np.array(neighbor))

                    if tent_gScore < gScore[neighbor]:ß
                        cameFrom[neighbor] = current
                        gScore[neighbor] = tent_gScore
#                         fScore[neighbor] = gScore[neighbor] + np.linalg.norm(np.array(neighbor)-np.array(end))
                        openSet[neighbor] = gScore[neighbor] + np.linalg.norm(np.array(neighbor)-np.array(end))
        return None


    def get_neighbors(self,map,point):
        neighbors = []
        if point[0] != 0 and self.map[point[0]-1][point[1]] != 1:
            neighbors.append((point[0]-1,point[1]))
            if point[1] != 0 and self.map[point[0]-1][point[1]-1] != 1:
                neighbors.append((point[0]-1,point[1]-1))
            if point[1] != (pixels[1]-1) and self.map[point[0]-1][point[1]+1] != 1:
                neighbors.append((point[0]-1,point[1]+1))

        if point[0] != (pixels[0]-1) and self.map[point[0]+1][point[1]] != 1:
            neighbors.append((point[0]+1,point[1]))
            if point[1] != 0 and self.map[point[0]+1][point[1]-1] != 1:
                neighbors.append((point[0]+1,point[1]-1))
            if point[1] != (pixels[1]-1) and self.map[point[0]+1][point[1]+1] != 1:
                neighbors.append((point[0]+1,point[1]+1))

        if point[1] != 0 and self.map[point[0]][point[1]-1] != 1:
            neighbors.append((point[0],point[1]-1))

        if point[1] != (pixels[1]-1) and self.map[point[0]][point[1]+1] != 1:
            neighbors.append((point[0],point[1]+1))

        return neighbors

    def callback(self,data):
        current = data.data[:2]
        goal = data.data[2:]
        #load map
        if self.map is None:
            rospy.loginfo("I didnt get the dammn map")
            return
        pixels = self.map.shape
        rho = np.linalg.norm(goal-current)
        if rho < 10:
            rospy.signal_shutdown("goal reached.")
        else:
            old_map = self.map.copy()
            for i in range(self.padding):
                new_map = self.map.copy()
                for x in range(pixels[0]):
                    for y in range(pixels[1]):
                        if self.map[x][y]:
                            if y != 0:
                                new_map[x][y-1] = 1
                                if x != 0:
                                    new_map[x-1][y-1] = 1
                                if x != (pixels[0]-1):
                                    new_map[x+1][y-1] = 1
                            if y != (pixels[1]-1):
                                new_map[x][y+1] = 1
                                if x != 0:
                                    new_map[x-1][y+1] = 1
                                if x != (pixels[1]-1):
                                    new_map[x+1][y+1] = 1
                            if x != 0:
                                new_map[x-1][y] = 1
                            if x != (pixels[0]):
                                new_map[x+1][y] = 1
                self.map = new_map
            path = local_planner(current,goal,map,pixels)
            self.publisher.publish(path)

    def mapCallback(self,data):
        data = np.asarray(msg.data, dtype=np.float32).reshape(msg.info.height,msg.info.width)
        newmap = data./100;
        self.map = np.where(newmap > .5, 1, 0)

    def listener(self):
        rospy.init_node("local_path", anonymous=True)
        rospy.Subscriber("/local_path", numpy_msg(Float32MultiArray), self.callback)
        rospy.Subscriber("/map", OccupancyGrid, self.mapCallback)
        rospy.spin()

if __name__ == "__main__":
    listener()
