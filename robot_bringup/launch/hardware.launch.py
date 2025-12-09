from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():

    robot_description_launch = PathJoinSubstitution([
        FindPackageShare("robot_description"),
        "launch",
        "display.launch.py"
    ])

    robot_control_launch = PathJoinSubstitution([
        FindPackageShare("robot_control"),
        "launch",
        "control.launch.py"
    ])

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(robot_description_launch)
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(robot_control_launch)
        )
    ])

