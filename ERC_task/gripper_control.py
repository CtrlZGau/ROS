#!/usr/bin/env python3
# license removed for brevity
import rospy
from std_msgs.msg import String
import sys

def control(command):
    pub = rospy.Publisher('/gripper_command', String, queue_size=10)
    rospy.init_node('gripper_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    if not rospy.is_shutdown():
        rospy.loginfo(command)
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        # total arguments
        control(sys.argv[1])
    except rospy.ROSInterruptException:
        pass