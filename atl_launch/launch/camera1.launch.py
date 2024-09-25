from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        SetEnvironmentVariable(
            name='GSCAM_CONFIG',
            value='udpsrc port=5600 ! application/x-rtp, encoding-name=H264 ! rtph264depay ! h264parse ! avdec_h264 ! videoconvert'
        ),

        # GSCam Node for camera 1
        Node(
            package="gscam",
            executable="gscam_node",
            namespace='cam1',
            name="gscam1",
            output="screen",
        ),

        # Image Transport Node to republish and compress image from /cam1/camera/image_raw
        Node(
            package="image_transport",
            executable="republish",
            namespace='cam1',
            name="image_compress",
            output="screen",
            remappings=[
                ('in', '/cam1/camera/image_raw'),  # Subscribe to the correct raw image topic
                ('out', '/cam1/camera/image_raw/compressed')  # The default compressed topic
            ],
            parameters=[{
                'use_sim_time': LaunchConfiguration('use_sim_time', default='false'),
                'compressed/format': 'jpeg',  # Compression format
                'compressed/jpeg_quality': 10  # JPEG quality
            }]
        )
    ])
