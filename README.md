# TRL Demos 
### Welcome :D
These are the source files for running TRL Demos.
## Installation
This repository assumes you have downloaded ROS2 Galactic, as well as the [RMF binary install](https://github.com/open-rmf/rmf) .

Create a new workspace & clone repo into source folder.
```sh
mkdir -p ~/trl_demos_ws/src
cd ~/trl_demos_ws/src
git clone git@github.com:siot-decada-robotics/trl.git
```
## Common commands
```sh
colcon build
traffic-editor
ros2 launch trl_demos_gz trl.launch.xml
ros2 run rmf_demos_tasks dispatch)clean -cs test_zone -st 0 --use_sim_time
```

