cmake_minimum_required(VERSION 3.5)

project(trl_demos)

find_package(ament_cmake REQUIRED)

install(DIRECTORY
  launch/
  include/
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
