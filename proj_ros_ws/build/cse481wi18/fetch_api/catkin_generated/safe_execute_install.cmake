execute_process(COMMAND "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/cse481wi18/fetch_api/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/cse481wi18/fetch_api/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
