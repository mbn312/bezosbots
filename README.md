# BezosBots

* [Team](#team)
* [Description](#description)
* [Wall Following](#wallfollowing)
* [All Code](#allcode)
* [Citations](#citations)

---
##### <a name="team"></a> Team
---

George Boyer

Doncey Albin

Benjamin Kraske

Matt Nguyen

---
##### <a name="description"></a> Description
---

The goal of this project was to set up and program an AWS DeepRacer to autonomously navigate the hallways in the basement of the Engineering Center at CU Boulder. This was to be accomplished via two methods: 1. A simple wall-following algorithm using lidar and Proportional Integral Derivative (PID) control. 2. A full implementation of Simultaneous Localization and Mapping (SLAM) and path planning. The DeepRacer was able to successfully navigate the basement course using the first method and significant progress was made in implementing the SLAM method. The code for the wall-following implementation can be found in the wallfollowing(#wallfollowing) folder and all of the code that we used over the course of the project can be found in the All Code(#allcode) folder. More detailed instructions on how to set up and run everything can be found in the report.

---
##### <a name="wallfollowing"></a> Wall Following
---

This folder contains our final code that was used to successfully navigate the hallways in the basement of the Engineering Center at CU Boulder. After running catkin_make, you can run the program by running:

```
roslaunch wallfollowing wall_following.launch
```

https://user-images.githubusercontent.com/70385444/146097047-50029dcc-a43c-4dcf-bf7b-72a14637eef2.mov

---
##### <a name="allcode"></a> All Code
---

This folder contains all of the code that we used over the course of our project. Here are the locations of some of things mentioned in our final report that are in this folder.

* localization
    * odometry dead reckoning (scripts/dead_reckoning.py)
    * velocity dead reckoning (scripts/vel_reck.py)
    * pid controllers
    * IMU (scripts/imu_pub.py)
* global_path
    * global planner (scripts/global_planner.py)
* local_path
    * hybrid A star
* RPLidar_Hector_SLAM
    * Hector SLAM
* old_scripts
    * A star (scripts/local_planner.py)


---
##### <a name="citations"></a> Citations
---

Hybrid A star Code found in All Code > local_path folder:
```
@mastersthesis{Kurzer1057261,
   author = {Kurzer, Karl},
   institution = {KTH, Integrated Transport Research Lab, ITRL},
   pages = {63},
   school = {KTH, Integrated Transport Research Lab, ITRL},
   title = {Path Planning in Unstructured Environments : A Real-time Hybrid A* Implementation for Fast and Deterministic Path Generation for the KTH Research Concept Vehicle},
   series = {TRITA-AVE},
   ISSN = {1651-7660},
   number = {2016:41},
   abstract = {On the way to fully autonomously driving vehicles a multitude of challenges have to be overcome. One common problem is the navigation of the vehicle from a start pose to a goal pose in an environment that does not provide any specic structure (no preferred ways of movement). Typical examples of such environments are parking lots or construction sites; in these scenarios the vehicle needs to navigate safely around obstacles ideally using the optimal (with regard to a specied parameter) path between the start and the goal pose. The work conducted throughout this master's thesis focuses on the development of a suitable path planning algorithm for the Research Concept Vehicle (RCV) of the Integrated Transport Research Lab (ITRL) at KTH Royal Institute of Technology, in Stockholm, Sweden. The development of the path planner requires more than just the pure algorithm, as the code needs to be tested and respective results evaluated. In addition, the resulting algorithm needs to be wrapped in a way that it can be deployed easily and interfaced with di erent other systems on the research vehicle. Thus the thesis also tries to gives insights into ways of achieving realtime capabilities necessary for experimental testing as well as on how to setup a visualization environment for simulation and debugging. },
   year = {2016}
}
```
