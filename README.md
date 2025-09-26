# Collision Video Generator

![Screenshot](https://github.com/kuoyaoming/LGSVL-collision-video-generator/blob/master/image/Screenshot.png)

## Introduction

This tool generates collision-scenario videos using the LGSVL Simulator via its Python API. It controls one EGO vehicle and one NPC vehicle to reproduce selected collision types. By default, videos are exported at 1920×1080 and 50 fps. Users can choose from five collision types and configure multiple environment parameters.

### Collision types
- LD: Vehicle turns right at a signalized intersection and enters the opposite direction of a vehicle traveling straight from a lateral approach.
- LTIP: Vehicle stops at a stop sign, then turns left across lateral crossing traffic.
- OD: Vehicle turns left at an uncontrolled intersection and cuts across the path of an oncoming vehicle.
- RTIP: Vehicle stops at a stop sign, then turns right across lateral crossing traffic.
- SCP: Vehicle stops at a stop sign, then proceeds straight across lateral crossing traffic.

### Environment parameters
- speed (km/h)
- rain level
- fog level
- wetness level
- pedestrian count (beta)
- NPC vehicle count (beta)

## Getting Started

### System requirements
- Ubuntu 18.04
- 4 GHz quad-core CPU
- NVIDIA GTX 1080, 8 GB GPU memory

### Software requirements
- Python 3.6
- LGSVL Simulator 2020.03-rc1
- Python API for LGSVL Simulator
- ROS Melodic
- lgsvl_msgs
- ffmpeg

## Installation

### Set up LGSVL Simulator
1. Download the 2020.03-rc1 release for Linux: [https://github.com/lgsvl/simulator/releases/tag/2020.03-rc1](https://github.com/lgsvl/simulator/releases/tag/2020.03-rc1)
2. Unzip the archive and run the executable.

### Set up the Python API for LGSVL Simulator
1. Get the Python API: [https://github.com/lgsvl/PythonAPI](https://github.com/lgsvl/PythonAPI)
2. Install the API:
```bash
cd PythonAPI
pip3 install --user .
```

### Set up lgsvl_msgs for ROS connectivity
1. Install ROS1 Melodic on Ubuntu 18.04: [ROS Documentation](http://wiki.ros.org/melodic/Installation/Ubuntu)
2. Install `lgsvl_msgs`: [lgsvl_msgs Documentation](https://www.lgsvlsimulator.com/docs/lgsvl-msgs/)

## Usage

### Prepare the simulator
1. Launch the simulator.
2. Click "Open Browser" to open the Simulator UI.
3. After default maps and vehicles download, go to the "Simulations" tab.
4. Create a new Simulation, give it a name, and check "API Only". Click Submit.
5. Select the new Simulation and click "Play" in the bottom-right.

### Run the tool
1. Clone and start the tool:
```bash
git clone https://github.com/kuoyaoming/collision_video_generator
cd collision_video_generator
python main.py
```
2. Choose your desired setup and parameters.
3. Click the "Play" button to generate the video.

## Notes
- Default output: 1920×1080 at 50 fps.
- Items marked as "beta" are experimental and may change.

## Acknowledgments
- Built on the LGSVL Simulator and its Python API.
