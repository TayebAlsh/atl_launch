from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='image_processor_pkg',  # Your package name
            executable='image_processor',    # Your node executable
            name='image_processor_node',     # Optional: Specify a custom node name
            output='screen',                 # Output to terminal
            remappings=[
                ('/original_topic', '/new_topic'),  # Replace with your actual topic names
            ],
        ),
    ])
