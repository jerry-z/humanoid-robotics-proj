# Install script for directory: /home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/cse481wi18/map_annotator

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/map_annotator/msg" TYPE FILE FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/cse481wi18/map_annotator/msg/PoseNames.msg"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/cse481wi18/map_annotator/msg/UserAction.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/map_annotator/cmake" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/cse481wi18/map_annotator/catkin_generated/installspace/map_annotator-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/devel/include/map_annotator")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/devel/share/roseus/ros/map_annotator")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/devel/share/common-lisp/ros/map_annotator")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/devel/share/gennodejs/ros/map_annotator")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/devel/lib/python2.7/dist-packages/map_annotator")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/devel/lib/python2.7/dist-packages/map_annotator")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/cse481wi18/map_annotator/catkin_generated/installspace/map_annotator.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/map_annotator/cmake" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/cse481wi18/map_annotator/catkin_generated/installspace/map_annotator-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/map_annotator/cmake" TYPE FILE FILES
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/cse481wi18/map_annotator/catkin_generated/installspace/map_annotatorConfig.cmake"
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/cse481wi18/map_annotator/catkin_generated/installspace/map_annotatorConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/map_annotator" TYPE FILE FILES "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/cse481wi18/map_annotator/package.xml")
endif()

