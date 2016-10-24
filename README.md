# Inverse Kinematics, URDFs, and Markers
This package allows simulation of a two-link planar robot in Rviz. The robot model was generated using a urdf; The trajectory for the robot was calculated using the analytical solution to the inverse kinematics of the system; and the path of the end effector is traced using visualization markers.

## The Robot Model ##
[r2_robot.urdf](https://github.com/ME495-EmbeddedSystems/homework-2-f2016-BlakeStrebel/blob/master/urdf/r2_robot.urdf) describes the robot. The tool urdf_to_graphiz was used to generate a graphic representation of the links and joints of the [robot](https://github.com/ME495-EmbeddedSystems/homework-2-f2016-BlakeStrebel/blob/master/urdf/r2_robot.pdf). The robot consists of a stationary `base_link` and then two links which compose the actual robot `link1` and `link2`. These links are connected by continuous joints which allow rotation about the z-axis. There is also a third stationary link at the end of the robot arm. This point is used to calculate the inverse kinematics and for visualization purposes.

## Controlling the Robot ##
The robot end effector follows a trajectory which traces out a circle of diameter 1 meter that is symmetric across the x-axis and shifted 1.25 meters in the positive x direction, both with respect to the fixed frame describing the `base_link`. [robot_control_node](https://github.com/ME495-EmbeddedSystems/homework-2-f2016-BlakeStrebel/blob/master/src/robot_control_node.py) publishes a `sensor_msgs/JointState` message on the `control_joint_states` topic which contains the orientations of the joints which result in the trajectory being followed. These orientations are determined using the analytic solution to the inverse kinematics of the system which were solved geometrically.

The `control_joint_states` topic is added to the `source_list` parameter for the `joint_state_publisher` node. The joint state publisher node takes the information from the `control_joint_states` topic and publishers a `sensor_msgs/JointState` message on the `joint_state` topic. The `robot_state_publisher` uses the data from this topic, and the kinematic description of the robot from the URDF to calculate the forward kinematics of the robot. Finally, this data is published to the `/tf` topic which is used by `Rviz` to simulate the robots movements.

## Visualizing the trajectory ##
The trajectory of the end-effector is visualized using Rviz visualization markers. The [publish_marker.py](https://github.com/ME495-EmbeddedSystems/homework-2-f2016-BlakeStrebel/blob/master/src/publish_marker.py) looks up the transform from the `base_link` to the link at the end-effector, `end`. This transformation data is then used to determine the position and orientations of spherical markers which are published to the `visualization_marker` topic. Rviz is automatically configured to subscribe the the `visualization_marker` topic and print the markers with the specified characteristics to the simulation. The lifetime for these markers is set to be half the period of the circular trajectory. This creates the visual effect where the markers appear to be following the end-effector.

## Using the Package ##
This package can be run using the [r2_robot.launch](https://github.com/ME495-EmbeddedSystems/homework-2-f2016-BlakeStrebel/blob/master/launch/r2_robot.launch) file. The launch file requires that the robot model, `model` be specified at runtime. It also has several optional parameters. The `joint state publisher` gui can be used to control the robot instead of the `control_joint_states` topic. This behavior is specified by setting the `gui` parameter to `True` at runtime. Furthermore, the period of the end-effector trajectory and the frequency that markers are published can be set using the `period` and `marker_frequency` parameters. The user can also elect to not run Rviz by setting the `rviz` parameter to `False`.
