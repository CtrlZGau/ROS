#!/usr/bin/env python3

import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
import tf.transformations as tft
import numpy as np
import sys
import tf2_ros

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

def close_gripper():
    pub = rospy.Publisher('/gripper_command', String, queue_size=10)
    rate = rospy.Rate(10)  # 10hz
    command = "semi_open"
    rospy.loginfo("Closing gripper: " + command)
    pub.publish(command)
    rate.sleep()
    rospy.sleep(3)


def main():
    rospy.init_node('pick_imu_box', anonymous=True)

    # Initialize MoveIt
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "manipulator"
    move_group = moveit_commander.MoveGroupCommander(group_name)

   
    # Parse the position
    frame_id, x, y, z, _, _, _, _ = [10,0.1792336325397422,0.25371753130928965,-0.16248440557110339,0.1693242136890411,-0.08133803889216265,0.6810086317638459,0.7077716281053512]

    # Define approach direction (assuming approaching from above)
    approach_direction = np.array([0, 0, -1])  # Negative z-axis

    # Calculate the orientation
    world_z = np.array([0, 0, 1])  # World z-axis
    y_axis = np.cross(approach_direction, world_z)
    if np.allclose(y_axis, 0):
        world_x = np.array([1, 0, 0])
        y_axis = np.cross(approach_direction, world_x)
    y_axis = y_axis / np.linalg.norm(y_axis)
    x_axis = np.cross(y_axis, approach_direction)
    x_axis = x_axis / np.linalg.norm(x_axis)

    # Create rotation matrix and convert to quaternion
    rotation_matrix = np.column_stack((x_axis, y_axis, approach_direction))
    quaternion = tft.quaternion_from_matrix(np.vstack([np.column_stack([rotation_matrix, [0,0,0]]), [0,0,0,1]]))

    # Create initial pose target
    pose_goal = geometry_msgs.msg.Pose()
    pose_goal.orientation.x = quaternion[0]
    pose_goal.orientation.y = quaternion[1]
    pose_goal.orientation.z = quaternion[2]
    pose_goal.orientation.w = quaternion[3]
    pose_goal.position.x = x +0.012
    pose_goal.position.y = y
    pose_goal.position.z = z + 0.2  # Add some offset to position above the box

    rospy.loginfo("Moving to initial position")
    if not move_to_pose(move_group, pose_goal):
        rospy.logerr("Failed to move to initial position")
        return

    # Rotate gripper by 90 degrees
    rospy.loginfo("Rotating gripper by 90 degrees")
    current_pose = move_group.get_current_pose().pose
    q_rot = tft.quaternion_about_axis(pi/2, (0, 0, 1))
    q_current = [current_pose.orientation.x, current_pose.orientation.y, 
                 current_pose.orientation.z, current_pose.orientation.w]
    q_new = tft.quaternion_multiply(q_rot, q_current)
    current_pose.orientation.x = q_new[0]
    current_pose.orientation.y = q_new[1]
    current_pose.orientation.z = q_new[2]
    current_pose.orientation.w = q_new[3]

    if not move_to_pose(move_group, current_pose):
        rospy.logerr("Failed to rotate gripper")
        return

    # Move down by 0.1 meters
    rospy.loginfo("Moving down by 0.1 meters")
    current_pose = move_group.get_current_pose().pose
    current_pose.position.z -= 0.08
    if not move_to_pose(move_group, current_pose):
        rospy.logerr("Failed to move down")
        return

    # Close gripper
    close_gripper()
    close_gripper()

    # Move up by 0.1 meters
    rospy.loginfo("Moving up by 0.1 meters")
    current_pose = move_group.get_current_pose().pose
    current_pose.position.z += 0.08
    if not move_to_pose(move_group, current_pose):
        rospy.logerr("Failed to move up")
        return

    rospy.loginfo("Pick operation completed successfully")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass