# ROS Empatica Logger
This repository provides a ROS module to receive data from an Empatica E4
wristband via a [ROS Android application](https://github.com/MonicaPH/ros_android_e4)
and write it to 7 different files. One for each recorded parameter.

## Requirement
This module depends on [empatica_e4_msgs](https://github.com/MonicaPH/empatica_e4_msgs).

## Setup
```
cd catkin/src
git clone https://github.com/MonicaPH/empatica_e4_msgs.git
git clone https://github.com/MonicaPH/ros_empatica_logger.git
cd ..
catkin_make
```

## Run
Open a console and execute `roscore`.
Then open another console and run:
```
rosrun ros_empatica_logger logger
```
This will create 7 files for logging
* acceleration x,
* acceleration y,
* acceleration z,
* skin temperature,
* electrodermal activity (EDA),
* blood volumetric pressure (BVP)
* and ibi.

To stop the module press Ctrl+C.
