# Copyright 2022 RT Corporation

import os

from ament_index_python.packages import get_package_share_directory
from launch.substitutions import Command


class RobotDescriptionLoader():

    def __init__(self):
        self.robot_description_path = os.path.join(
            get_package_share_directory('crane_x7_description'),
            'urdf',
            'crane_x7.urdf.xacro')
        self.port_name = '/dev/ttyUSB0'
        self.baudrate = '3000000'
        self.timeout_seconds = '1.0'
        self.manipulator_config_file_path = ''
        self.manipulator_links_file_path = ''
        self.use_gazebo = 'false'
        self.use_d435 = 'false'
        self.use_mock_components = 'false'
        self.gz_control_config_package = ''
        self.gz_control_config_file_path = ''

    def load(self):
        return Command([
                'xacro ',
                self.robot_description_path,
                ' port_name:=', self.port_name,
                ' baudrate:=', self.baudrate,
                ' timeout_seconds:=', self.timeout_seconds,
                ' manipulator_config_file_path:=', self.manipulator_config_file_path,
                ' manipulator_links_file_path:=', self.manipulator_links_file_path,
                ' use_gazebo:=', self.use_gazebo,
                ' use_d435:=', self.use_d435,
                ' use_mock_components:=', self.use_mock_components,
                ' gz_control_config_package:=', self.gz_control_config_package,
                ' gz_control_config_file_path:=', self.gz_control_config_file_path
                ])
