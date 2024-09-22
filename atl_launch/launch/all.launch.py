import os
import launch

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
   joystick = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('atl_launch'), 'launch'),
         '/core.launch.py'])
      )

   hardware = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('atl_launch'), 'launch'),
         '/hardware_interface.launch.py'])
      )

   camera1 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('atl_launch'), 'launch'),
         '/camera1.launch.py'])
      )
   camera2 = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('atl_launch'), 'launch'),
         '/camera2.launch.py'])
      )
   viz = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('atl_launch'),
         'launch'),
         '/viz.launch.py'])
      )
   record = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('atl_launch'), 'launch'),
         '/record.launch.py'])
   )

   passit = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('atl_launch'), 'launch'),
         '/pass.launch.py'])
   )

   return LaunchDescription([
      joystick,
      hardware,
      camera1,
      camera2,
      passit,
      viz,
      record
   ])