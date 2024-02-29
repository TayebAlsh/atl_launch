from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable

def generate_launch_description():

#  ! ffmpegcolorspace

    return LaunchDescription([
        SetEnvironmentVariable(name='GSCAM_CONFIG', value='udpsrc port=5600 ! application/x-rtp, encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert'),
        Node(
            package="gscam",
            executable="gscam_node",
            namespace='cam1',
            name="gscam1",
            output="screen",
        )
    ])
