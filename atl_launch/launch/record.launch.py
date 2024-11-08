import launch
import os
from datetime import datetime

def generate_launch_description():
    # Generate a unique directory name based on the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = os.path.expanduser(f'~/ROSBAGS/rosbag_{timestamp}')

    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['ros2',
                 'bag',
                 'record',
                 '-o', output_dir,  # Specify the unique output directory
                 '/tf',
                 '/leak',
                 '/depth',
                 '/imu',
                 '/joy',
                 '/servos_input',
                 '/servos_feedback',
                 '/cam1/camera/image_raw/compressed',  # Record compressed image topic for cam1
                 '/cam2/camera/image_raw/compressed',   
                 ],
            output='screen'
        )
    ])

if __name__ == '__main__':
    generate_launch_description()