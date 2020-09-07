# Collision video generator

![Screenshot](https://github.com/kuoyaoming/LGSVL-collision-video-generator/blob/master/image/Screenshot.png)
# Introduction

This tool can generate a different type of collision video.  Control one EGO vehicle and one NPC vehicle to perform a different type of collision by using python API Pre-written script based on the LGSVL simulator. the video default resolution is 1920 * 1080 50fps. Users can choose five different types of collisions and four environment parameters.

### list of collision types：
* LD: The vehicle is turning right at a signalized intersection and then turns into the opposite direction of another vehicle crossing straight initially from a lateral direction.
* LTIP: The vehicle stops at a stop sign and then proceeds to turn left against lateral crossing traffic.
* OD: The vehicle is turning left at an intersection without traffic controls and then cuts across the path of another vehicle traveling from the opposite direction.
* RTIP: The vehicle stops at a stop sign and then proceeds to turn left against lateral crossing traffic.
* SCP: The vehicle stops at a stop sign and then proceeds against lateral crossing traffic.

### list of environment parameters ：
* speed (km / h)
* rain level
* fog level
* wetness level
* pedstrain number (beta)
* NPC vehicle number (beta)

# Getting Started

## System Requirements

the simulator need hight performance so there is hardware recommend:

* Ubuntu 18.04
* 4 GHz Quad Core CPU
* Nvidia GTX 1080, 8GB GPU memory

## Package Requirements

* python 3.6
* LGSVL simulator 2020.03-rc1
* Python API for LGSVL Simulator
* ROS Melodic
* lgsvl_msgs
* ffmpeg

## Requirements package installation

### Setup LGSVL simulator

1. Download the 2020.03-rc1 of the LGSVL for linux here: [https://github.com/lgsvl/simulator/releases/tag/2020.03-rc1](https://github.com/lgsvl/simulator/releases/tag/2020.03-rc1)
2. Unzip the downloaded folder and run the executable.

### Setup Python API for LGSVL Simulator

1. Download the Python API from github repository: [https://github.com/lgsvl/PythonAPI](https://github.com/lgsvl/PythonAPI)

2. Installing
```
pip3 install --user .
```
### Setup lgsvl_msgs for ROS connect
1. Follow the [ROS Documentation](http://wiki.ros.org/melodic/Installation/Ubuntu) install ROS1 for Ubuntu 18.04
2. Follow the [lgsvl_msgs Documentation](https://www.lgsvlsimulator.com/docs/lgsvl-msgs/) install lgsvl_msgs for ROS

# Usage

## Before start the tool
1. Launch the simulator.
2. Click the Open Browser button to open the Simulator UI.
3. After the default maps and vehicles have been downloaded, navigate to the Simulations tab.
4. Create a new Simulation. Give it a name and check the API Only option. Click Submit.
5. Select the newly created Simulation and click the "Play" button in the bottom right.

## Start
1. This tool is available in separate repository: [https://github.com/kuoyaoming/collision_video_generator](https://github.com/kuoyaoming/collision_video_generator)
```
git clone https://github.com/kuoyaoming/collision_video_generator

cd collision_video_generator

python main.py
```
2. Choose any setup that you want.
3. Click the Play button.
# LGSVL-collision-video-generator

