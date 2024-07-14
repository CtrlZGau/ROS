#!/usr/bin/env python3
import rospy
import tf2_ros
import tf2_geometry_msgs
from geometry_msgs.msg import PoseStamped
from fiducial_msgs.msg import FiducialTransformArray
import csv
import os

class FiducialDataProcessor:
    def __init__(self):
        rospy.init_node('fiducial_data_processor')
        self.tf_buffer = tf2_ros.Buffer(rospy.Duration(10.0))  # Extend buffer time
        self.tf_listener = tf2_ros.TransformListener(self.tf_buffer)
        self.subscriber = rospy.Subscriber('/fiducial_transforms', FiducialTransformArray, self.callback)
        self.base_frame = "base_link"
        self.camera_frame = "camera_link"
        self.markers = {}

    def callback(self, data):
        for transform in data.transforms:
            marker_pose = PoseStamped()
            marker_pose.header = data.header
            marker_pose.pose.position = transform.transform.translation
            marker_pose.pose.orientation = transform.transform.rotation

            try:
                # Use the latest available transform
                transform_time = rospy.Time(0)
                base_pose = self.tf_buffer.transform(marker_pose, self.base_frame, timeout=rospy.Duration(1.0))
                
                # Update the marker pose (overwriting previous detections)
                self.markers[transform.fiducial_id] = base_pose.pose
                rospy.loginfo(f"Updated pose for marker {transform.fiducial_id}")
            except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException) as e:
                rospy.logwarn(f"TF Error for marker {transform.fiducial_id}: {e}")

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'X', 'Y', 'Z', 'QX', 'QY', 'QZ', 'QW'])
            for marker_id, pose in self.markers.items():
                writer.writerow([
                    marker_id,
                    pose.position.x, pose.position.y, pose.position.z,
                    pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w
                ])
        rospy.loginfo(f"Saved transformed marker data to {filename}")

if __name__ == '__main__':
    processor = FiducialDataProcessor()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        pass
    finally:
        file_path = os.path.expanduser('~/catkin_ws/src/objective/Scripts/trial.csv')
        processor.save_to_csv(file_path)