import launch


def generate_launch_description():
    return launch.LaunchDescription([
        launch.actions.ExecuteProcess(
            cmd=['ros2',
                 'bag',
                 'record',
                #  '-a'
                '/tf',
                '/cam1/camera/image_raw/compressed',
                '/leak',
                '/depth',
                '/imu'
                '/joy',
                '/servos_input',
                '/servos_feedback'
                 ],
            output='screen'
        )
    ])