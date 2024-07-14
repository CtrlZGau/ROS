#!/bin/bash

rosrun objective pick_IMU.py 

rosrun objective gripper_control.py semi_open
rosrun objective gripper_control.py semi_open

rosrun tf2_ros static_transform_publisher 0 0 0.05 1.57 0 -1.57 tool_gripper imu&
PID1=$!

rosrun objective move_IMU.py 

kill $PID1


rosrun objective gripper_control.py open
rosrun objective gripper_control.py open

rosrun tf2_ros static_transform_publisher 0 0 0.05 1.57 0 -1.57 imu_panel imu&

rosrun objective pick_boxTop.py

rosrun objective gripper_control.py semi_close
rosrun objective gripper_control.py semi_close

rosrun tf2_ros static_transform_publisher 0.1 0 0.08 1.57 0 -1.57 tool_gripper box_top&

rosrun objective place_boxTop.py

rosrun tf2_ros static_transform_publisher 0.1 -0.1 -0.05 0 0 0 base box_top&

rosrun objective gripper_control.py open
rosrun objective gripper_control.py open

rosrun objective scan_box.py


