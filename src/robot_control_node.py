#!/usr/bin/env python
import rospy
from math import cos, sin, pi

from sensor_msgs.msg import JointState

def control():
    pub = rospy.Publisher('control_joint_states',JointState,queue_size=10)
    rate = rospy.Rate(50)
    joint_state = JointState()

    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec()

        joint_state.header.stamp = rospy.Time.now()
        joint_state.name = ["base_to_link1","link1_to_link2"]
        joint_state.position = [1, 1]
        pub.publish(joint_state)

        rate.sleep()

if __name__ == '__main__':
    rospy.init_node('robot_control_node')
    check = rospy.get_param('use_gui',default =False)
    try:
        if check == False:
            control()
    except rospy.ROSInterruptException:
        pass

rospy.spin()
