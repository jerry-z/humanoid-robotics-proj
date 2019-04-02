# Install script for directory: /home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetch_gazebo_demo

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_gazebo/fetch_gazebo_demo/catkin_generated/installspace/fetch_gazebo_demo.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetch_gazebo_demo/cmake" TYPE FILE FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_gazebo/fetch_gazebo_demo/catkin_generated/installspace/fetch_gazebo_demoConfig.cmake"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_gazebo/fetch_gazebo_demo/catkin_generated/installspace/fetch_gazebo_demoConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetch_gazebo_demo" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetch_gazebo_demo/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/fetch_gazebo_demo" TYPE PROGRAM FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetch_gazebo_demo/scripts/demo.py"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetch_gazebo_demo/scripts/pick_place_demo.py"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetch_gazebo_demo" TYPE DIRECTORY FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetch_gazebo_demo/launch"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetch_gazebo_demo/maps"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetch_gazebo_demo/config"
    )
endif()

