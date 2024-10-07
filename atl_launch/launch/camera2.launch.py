from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([

        # GSCam Node for camera 2 (using ROS parameter)
        Node(
            package="gscam",
            executable="gscam_node",
            namespace='cam2',
            name="gscam2",
            output="screen",
            parameters=[{
                'gscam_config': 'udpsrc port=5601 ! application/x-rtp, encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert'
            }]
        ),

        # Image Transport Node to republish and compress image from /cam2/image_raw
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
                'use_sim_time': 'false',
                'compressed/format': 'jpeg',
                'compressed/jpeg_quality': 10  # JPEG quality
            }]
        )
    ])
