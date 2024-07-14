#!/usr/bin/env python3

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import tf.transformations as tft
import numpy as np
import sys
from math import pi
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler

def rotate_quaternion_z_180(original_quaternion):
    rotation_z_180 = tft.quaternion_about_axis(np.pi, (0, 0, 1))
    rotated_quaternion = tft.quaternion_multiply(rotation_z_180, original_quaternion)
    return rotated_quaternion

def move_to_pose(move_group, pose_goal):
    move_group.set_pose_target(pose_goal)
    success = False
    for attempt in range(10):  # Try up to 10 times
        plan = move_group.go(wait=True)
        if plan:
            success = True
            break
        rospy.sleep(0.2)  # Short delay between attempts
    move_group.stop()
    move_group.clear_pose_targets()
    return success

def main():
    rospy.init_node('place_box_on_board', anonymous=True)

    # Initialize MoveIt
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)

    # Parse the board pose
    _, x, y, z, qx, qy, qz, qw = [1,0.4724830374884754,0.060016175362241186,0.40701729313192914,-0.4807549977618302,0.5111679602995692,0.5123852447995108,-0.4950184939999178]

    current_pose = move_group.get_current_pose().pose
    pose_goal = Pose()
    pose_goal = current_pose
    pose_goal.position.x = x - 0.13
    pose_goal.position.y = y 
    pose_goal.position.z = z - 0.05

    # Convert Euler angles (roll, pitch, yaw) to quaternion
    roll = 0
    pitch = 1.5708   # 90 degrees in radians (looking down)
    yaw = 0
    quaternion = quaternion_from_euler(roll, pitch, yaw)

    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    # Move the arm to the target pose
    move_to_pose(move_group, pose_goal)

    """current_pose = move_group.get_current_pose().pose

    # Calculate the new position 0.1 meters forward
    final_position = arm_position + 0.1 * forward_direction

    current_pose.position.x = final_position[0]
    current_pose.position.y = final_position[1]
    current_pose.position.z = final_position[2]

    if not move_to_pose(move_group, current_pose):
        rospy.logerr("Failed to move to position facing away from the board")
        return"""

    rospy.loginfo("Successfully moved to position facing away from the board")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass