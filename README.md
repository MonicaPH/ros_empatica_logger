# ROS Empatica Logger
This repository provides a ROS module to receive data
from an Empatica E4 wristband via a
[ROS Android application](https://github.com/MonicaPH/ros_android_e4)
and write it to 7 different files. One for each recorded parameter.

## Requirement
This module depends on [empatica_e4_msgs](https://github.com/hyeonukbhin/empatica_e4_msgs).

## Setup
'''
cd catkin/src
git clone https://github.com/MonicaPH/ros_empatica_logger.git
cd ..
catkin_make
'''

## Run
'''
rosrun ros_empatica_logger logger
'''
