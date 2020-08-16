*very simple ROS package to test a multi-camera setup with 2 (or more) realsense RGBD cameras*

Tested using ROS kinetic on Ubuntu 16.04, and a USB 3.0 port (I experienced some bandwidth errors with USB 2.0)

Dependencies: realsense ROS wrapper ([https://github.com/IntelRealSense/realsense-ros](https://github.com/IntelRealSense/realsense-ros))

How to run:
- to test with just one camera, run "roslaunch multi_rgbd_setup rgbd_sensor.launch serial_no_camera1:=91.........." and replace the serial number (there should be a sticker on the camera)
- to test with two cameras, run "roslaunch multi_rgbd_setup rgbd_sensor.launch camera2_active:=true serial_no_camera1:=912112072834 serial_no_camera1:=912112072834" and replace the serial numbers
- edit multi_rgbd_setup/launch/rgbd_sensor.launch file to add more cameras
- run multi_rgbd_setup/src/test.py to check if all cameras are streaming data
