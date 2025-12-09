from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution

def generate_launch_description():

    mode_arg = DeclareLaunchArgument(
        "mode",
        default_value="sim",
        description="Bringup mode: sim or hardware"
    )

    sim_launch = PathJoinSubstitution([
        FindPackageShare("robot_bringup"),
        "launch",
        "sim.launch.py"
    ])

    hardware_launch = PathJoinSubstitution([
        FindPackageShare("robot_bringup"),
        "launch",
        "hardware.launch.py"
    ])

    return LaunchDescription([
        mode_arg,
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(sim_launch),
            condition=None
        )
    ])

