#!/bin/bash
sed -i '/<world name="world">/r /home/ubuntu/trl_demos_ws/src/trl/trl_demos_gz/scripts/increase_gazebo_step' /home/ubuntu/trl_demos_ws/install/trl_demos_maps/share/trl_demos_maps/maps/trl/trl.world
echo "world file step size edited"

exit 0