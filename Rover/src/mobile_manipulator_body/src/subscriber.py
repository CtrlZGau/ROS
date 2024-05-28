#!/usr/bin/env python3 
import rospy
from nav_msgs.msg import Odometry

def callback(data):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z
    distance = (x ** 2 + y ** 2 + z ** 2) ** 0.5
    print("Distance: ",distance)

def listener():
    rospy.init_node('listerner',anonymous="True")
    rospy.Subscriber("/robot_base_velocity_controller/odom",Odometry,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
