# Install script for directory: /home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_ros/fetch_navigation

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_ros/fetch_navigation/catkin_generated/installspace/fetch_navigation.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetch_navigation/cmake" TYPE FILE FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_ros/fetch_navigation/catkin_generated/installspace/fetch_navigationConfig.cmake"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_ros/fetch_navigation/catkin_generated/installspace/fetch_navigationConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetch_navigation" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_ros/fetch_navigation/package.xml")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetch_navigation" TYPE DIRECTORY FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_ros/fetch_navigation/config")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/fetch_navigation" TYPE DIRECTORY FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_ros/fetch_navigation/launch")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/fetch_navigation" TYPE PROGRAM FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_ros/fetch_navigation/scripts/tilt_head.py")
endif()

