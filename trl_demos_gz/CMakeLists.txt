cmake_minimum_required(VERSION 3.5)

project(trl_demos_gz)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch/
  DESTINATION share/${PROJECT_NAME}
)
install(PROGRAMS
  scripts/gazebo_step.sh
  scripts/increase_gazebo_step
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
