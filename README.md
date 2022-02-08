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
## Notes
080221 - Binary release of traffic-editor has a bug that does not work well with multi-level worlds. Use latest traffic-editor in this [checkout](https://github.com/open-rmf/rmf_traffic_editor/tree/bug/fully_transform_vertex_point_in_properties_pane) to edit the trl.building.yaml
