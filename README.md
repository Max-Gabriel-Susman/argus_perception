# Argus Perception

This repository contains the Perception package for the Argus Autonomous Vehicle System. 

## Local Setup

Change directory to your workspace and source setup script: 
```
source install/setup.bash
```

## Local Operations

Prior to performing the rest of the operations in this section you'll need to perform the operations in the `Local Setup` section.

Launch the Realsense computer vision node: 
```
ros2 launch argus_perception realsense_launch.py
```

Run the RQT application for this package:
```
ros2 run rqt_graph rqt_graph
```

Launch rviz: 
```
rviz2
```
