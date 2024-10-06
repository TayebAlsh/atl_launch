from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        SetEnvironmentVariable(name='GSCAM_CONFIG', value='udpsrc port=5601 ! application/x-rtp, encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert'),
        Node(
            package="gscam",
            executable="gscam_node",
            namespace='cam2',
            name="gscam2",
            output="screen",
        ),
        Node(
            package="image_transport",
            executable="republish",
            name="image_compress",
            namespace='cam2',
            output="screen",
            remappings=[
                ('in', '/cam2/image_raw'),
                ('out', '/cam2/camera/compressed')
            ],
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time', default='false'),
                'compressed/format': 'jpeg',
                'compressed/jpeg_quality': 10  # Set quality to 50%
            }]
        )
    ])