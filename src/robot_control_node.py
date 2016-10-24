#!/usr/bin/env python
import rospy
from math import cos, sin, pi, atan2, acos, sqrt

from sensor_msgs.msg import JointState

def control():
    pub = rospy.Publisher('control_joint_states',JointState,queue_size=10)

    rate = rospy.Rate(50)
    joint_state = JointState()

    p = rospy.get_param('period')

    while not rospy.is_shutdown():
        t = rospy.Time.now().to_sec()

        x = .5*cos(2*pi*t/p)+1.25
        y = .5*sin(2*pi*t/p)
        x2 = x ** 2
        y2 = y ** 2
        theta1 = atan2(y,x) - acos((x2+y2)/(2*sqrt(x2+y2)))
        theta2 = pi - acos((2-x2-y2)/2)

        joint_state.header.stamp = rospy.Time.now()
        joint_state.name = ["base_to_link1","link1_to_link2"]
        joint_state.position = [theta1, theta2]
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
