#!/usr/bin/env python3 

import rospy
from mobile_manipulator_body.srv import velocity, velocityResponse
from geometry_msgs.msg import Twist

def pose_Callback(pub,velocity_msg):
	pub.publish(velocity_msg)

def server(data):
    vel_msg = Twist()
    vel_msg.linear.x = 0
    for i in range(data.sec_int):
        vel_msg.linear.x = 1
        pose_Callback(pub,vel_msg)
        rate.sleep()
    pose_Callback(pub,vel_msg)
    print("Done")
    return "Time changed"

if __name__ == "__main__":
    node_name = "Vel_Manipulator"
    rospy.init_node(node_name)
    pub_topic_name = "/robot_base_velocity_controller/cmd_vel"
    rate = rospy.Rate(1)
    pub = rospy.Publisher(pub_topic_name,Twist,queue_size=10)
    service = rospy.Service('velocity_change_service',velocity,server)
    rospy.spin()
