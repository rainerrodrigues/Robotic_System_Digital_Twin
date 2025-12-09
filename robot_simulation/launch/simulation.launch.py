from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    # Path to robot_description launch (to load URDF into robot_state_publisher)
    robot_desc_launch = PathJoinSubstitution([
        FindPackageShare('robot_description'),
        'launch',
        'display.launch.py'
    ])

    # Path to world file
    world_file = PathJoinSubstitution([
        FindPackageShare('robot_simulation'),
        'worlds',
        'empty.world'
    ])

    return LaunchDescription([
        # Launch robot_description (spawns robot_state_publisher + RViz)
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(robot_desc_launch)
        ),
        # Launch Gazebo
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([
                FindPackageShare('ros_gz_sim'),
                '/launch/gz_sim.launch.py'
            ]),
            launch_arguments={'world': world_file}.items()
        )
    ])

