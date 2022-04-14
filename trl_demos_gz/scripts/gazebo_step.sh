#!/bin/bash
physicspath=`dirname "$0"`/increase_gazebo_step
installpath=$(builtin cd `dirname "$0"`; cd ../../../../install/trl_demos_maps/share/trl_demos_maps/maps/trl; pwd)/trl.world
echo installpath: $installpath
echo physicspath: $physicspath
if grep -Ff $installpath $physicspath 
then
    echo "world file step size already set"
else
    sed -i '/<world name="world">/r '$physicspath'' $installpath
    echo "world file step size edited"
fi

