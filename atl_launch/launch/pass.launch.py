import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

# def generate_launch_description():

    # config = os.path.join(
    #     get_package_share_directory('atl_launch'),
    #     'config',
    #     'trim.yaml'
    # )

    # return LaunchDescription([
    #     Node(
    #         package="atl_passthrough",
    #         executable="atl_passthrough_node",
    #         name="atl_passthrough",
    #         # parameters=[config],
    #         parameters=[
    #             ("servo_trim_1", 0.5),
    #             ("servo_trim_2", 0.5),
    #             ("servo_trim_3", 0.5),
    #             ("servo_trim_4", 0.5)
    #         ],
    #         output="screen"
    #     )
    # ])


def generate_launch_description():
    ld = LaunchDescription()
    # config = os.path.join(
    #     get_package_share_directory('atl_passthrough'),
    #     'config',
    #     'params.yaml'
    #     )
        
    node=Node(
        package = 'atl_passthrough',
        name = 'atl_passthrough',
        executable = 'atl_passthrough_node',
        # parameters = [config]
    )
    ld.add_action(node)
    return ld