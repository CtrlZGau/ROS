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

    # Create a target pose by modifying the x-coordinate of the initial pose
    initial_pose = move_group.get_current_pose().pose
    target_pose = Pose()
    target_pose.position.x = 0.3   # Adjust the value to control the distance of movement
    target_pose.position.y = 0.1
    target_pose.position.z = 0.35
    target_pose.orientation = initial_pose.orientation 
    
    # Convert Euler angles (roll, pitch, yaw) to quaternion
    roll = 0
    pitch = 1.5708 # 90 degrees in radians (looking down)
    yaw = 0
    quaternion = quaternion_from_euler(roll, pitch, yaw)

    target_pose.orientation.x = quaternion[0]
    target_pose.orientation.y = quaternion[1]
    target_pose.orientation.z = quaternion[2]
    target_pose.orientation.w = quaternion[3]

    # Move the arm to the target pose
    move_to_pose(move_group, target_pose)
    initial_pose = target_pose
    rospy.sleep(1)


    # Parse the board pose
    _, x, y, z, qx, qy, qz, qw = [12,0.33553536033768805,-0.2747763158287744,0.20508778017292842,-0.4081032556523972,0.5624846237339333,0.5817204124723909,-0.4226868137306399]

    # Calculate the position 0.2 meters away from the board
    board_position = np.array([x, y, z])
    board_orientation = np.array([qx, qy, qz, qw])
    
    # Convert quaternion to rotation matrix
    rotation_matrix = tft.quaternion_matrix(board_orientation)[:3, :3]
    
    # The normal vector of the board is the third column of the rotation matrix
    board_normal = rotation_matrix[:, 2]
    
    # Calculate the position 0.2 meters away from the board
    arm_position = board_position + 0.12* board_normal

    # Rotate the orientation 180 degrees around z-axis
    arm_orientation = rotate_quaternion_z_180(board_orientation)

    # Convert the current quaternion to Euler angles
    (roll, pitch, yaw) = tft.euler_from_quaternion(arm_orientation)

    # Adjust the pitch by 90 degrees (1.5708 radians)
    new_pitch = pitch + 1.5708

    # Convert the new Euler angles back to a quaternion
    new_quaternion = tft.quaternion_from_euler(roll, new_pitch, yaw)

    current_pose = move_group.get_current_pose().pose
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal = current_pose
    # Set the new orientation
    pose_goal.orientation.x = new_quaternion[0]
    pose_goal.orientation.y = new_quaternion[1]
    pose_goal.orientation.z = new_quaternion[2]
    pose_goal.orientation.w = new_quaternion[3]

    # Set a longer planning time
    move_group.set_planning_time(15)  # 15 seconds

    if not move_to_pose(move_group, pose_goal):
        rospy.logerr("Failed to move to position facing away from the board")
        return
    
    # Calculate the forward direction (opposite of board normal)
    forward_direction = -board_normal

    current_pose = move_group.get_current_pose().pose

    rospy.sleep(2)

    pose_goal = current_pose

    final_position = arm_position + 0.1 * forward_direction
    pose_goal.position.x = final_position[0]
    pose_goal.position.y = final_position[1] - 0.004
    pose_goal.position.z = arm_position[2] + 0.07

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