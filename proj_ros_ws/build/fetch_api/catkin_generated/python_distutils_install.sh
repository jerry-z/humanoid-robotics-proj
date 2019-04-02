#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_api"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/install/lib/python2.7/dist-packages:/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build" \
    "/usr/bin/python" \
    "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/src/fetch_api/setup.py" \
    build --build-base "/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/build/fetch_api" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/install" --install-scripts="/home/jzhang102/Documents/humanoid_proj/proj_ros_ws/install/bin"
