#!/usr/bin/env python
import roslib
roslib.load_manifest('r2_robot')
import rospy
import math
import tf
import geometry_msgs.msg
from visualization_msgs.msg import Marker

if __name__ == '__main__':
    rospy.init_node('publish_marker')

    listener = tf.TransformListener()
    marker_pub = rospy.Publisher('visualization_marker',Marker,queue_size=1)

    i = 0

    rate = rospy.Rate(20)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('base_link', 'end', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue

        marker = Marker()
        marker.header.frame_id = "base_link"
        marker.header.stamp = rospy.Time.now()
        marker.id = i;
        marker.type = Marker.SPHERE
        marker.action = Marker.ADD
        marker.pose.position.x = trans[0]
        marker.pose.position.y = trans[1]
        marker.pose.position.z = trans[2]
        marker.pose.orientation.x = rot[0]
        marker.pose.orientation.y = rot[1]
        marker.pose.orientation.z = rot[2]
        marker.pose.orientation.w = rot[3]
        marker.scale.x = .1
        marker.scale.y = .1
        marker.scale.z = .1
        marker.color.r = 0.0
        marker.color.g = 1.0
        marker.color.b = 0.0
        marker.color.a = 1.0

        marker.lifetime = rospy.Duration(1)
        marker_pub.publish(marker)

        i = i + 1

        rate.sleep()
