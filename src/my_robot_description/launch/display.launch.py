from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, FindExecutable, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Package share path
    pkg_share = FindPackageShare('my_robot_description')

    # File paths
    urdf_file = PathJoinSubstitution([pkg_share, 'urdf', 'my_robot.urdf.xacro'])
    rviz_config_file = PathJoinSubstitution([pkg_share, 'rviz', 'urdf_config.rviz'])

    # Run xacro to generate URDF
    robot_description = Command([
        PathJoinSubstitution([FindExecutable(name='xacro')]), ' ', urdf_file
    ])

    return LaunchDescription([
        # Publish robot state
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_description}]
        ),

        # GUI joint state publisher
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        # RViz2
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen'
        )
    ])
