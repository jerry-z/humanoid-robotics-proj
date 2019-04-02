# Install script for directory: /home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_gazebo/fetchit_challenge/catkin_generated/installspace/fetchit_challenge.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetchit_challenge/cmake" TYPE FILE FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_gazebo/fetchit_challenge/catkin_generated/installspace/fetchit_challengeConfig.cmake"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_gazebo/fetchit_challenge/catkin_generated/installspace/fetchit_challengeConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetchit_challenge" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/fetchit_challenge" TYPE PROGRAM FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/scripts/spawn_assembly_delayed.sh"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/scripts/spawn_assembly_delayed_simple.sh"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetchit_challenge" TYPE DIRECTORY FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/config"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/launch"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/models"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/urdf"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_gazebo/fetchit_challenge/worlds"
    )
endif()

