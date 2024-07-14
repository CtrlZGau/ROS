#!/usr/bin/env python3

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
import tf.transformations as tft
import numpy as np
import sys

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
    _, x, y, z, qx, qy, qz, qw = [11,0.4130957007868823,0.3472725953901781,0.5158916060203884,0.5899267096434175,-0.43692444503667577,-0.40573474853357616,0.5444839946326056]

    # Calculate the position 0.2 meters away from the board
    board_position = np.array([x, y, z])
    board_orientation = np.array([qx, qy, qz, qw])
    
    # Convert quaternion to rotation matrix
    rotation_matrix = tft.quaternion_matrix(board_orientation)[:3, :3]
    
    # The normal vector of the board is the third column of the rotation matrix
    board_normal = rotation_matrix[:, 2]
    
    # Calculate the position 0.2 meters away from the board
    arm_position = board_position + 0.1 * board_normal

    # Rotate the orientation 180 degrees around z-axis
    arm_orientation = rotate_quaternion_z_180(board_orientation)

    # Create pose target
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.position.x = arm_position[0]
    pose_goal.position.y = arm_position[1]
    pose_goal.position.z = arm_position[2] - 0.1
    
    # Set the rotated orientation for the arm
    pose_goal.orientation.x = arm_orientation[0]
    pose_goal.orientation.y = arm_orientation[1]
    pose_goal.orientation.z = arm_orientation[2]
    pose_goal.orientation.w = arm_orientation[3]

    # Set a longer planning time
    move_group.set_planning_time(15)  # 15 seconds

    rospy.loginfo(f"Target position: {arm_position}")
    rospy.loginfo(f"Target orientation: {arm_orientation}")
    rospy.loginfo("Moving to position 0.2 meters away from the board with 180-degree rotation")

    if not move_to_pose(move_group, pose_goal):
        rospy.logerr("Failed to move to position facing away from the board")
        return
    
    # Calculate the forward direction (opposite of board normal)
    forward_direction = -board_normal
    # Calculate the new position 0.1 meters forward
    final_position = arm_position + 0.1 * forward_direction

    current_pose = move_group.get_current_pose().pose

    rospy.sleep(2)

    rospy.loginfo("Successfully moved to position facing away from the board")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass