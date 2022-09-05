# Copyright 2022 RT Corporation

from crane_x7_description.robot_description_loader import RobotDescriptionLoader
from launch.launch_context import LaunchContext
import pytest


def exec_load(loader):
    # Command substitutionの実行方法はCommandのテストを参考にした
    # https://github.com/ros2/launch/blob/074cd2903ddccd61bce8f40a0f58da0b7c200481/launch/test/launch/substitutions/test_command.py#L47
    context = LaunchContext()
    return loader.load().perform(context)


def test_load_description():
    # xacroの読み込みが成功することを期待
    rdl = RobotDescriptionLoader()
    assert exec_load(rdl)


def test_change_description_path():
    # xacroのファイルパスを変更し、読み込みが失敗することを期待
    rdl = RobotDescriptionLoader()
    rdl.robot_description_path = 'hoge'
    with pytest.raises(Exception) as e:
        exec_load(rdl)
    assert e.value


def test_port_name():
    # port_nameが変更され、xacroにポート名がセットされることを期待
    rdl = RobotDescriptionLoader()
    rdl.port_name = '/dev/ttyUSB1'
    assert '"port_name">/dev/ttyUSB1' in exec_load(rdl)


def test_baudrate():
    rdl = RobotDescriptionLoader()
    rdl.baudrate = '4000000'
    assert '"baudrate">4000000' in exec_load(rdl)


def test_timeout_seconds():
    rdl = RobotDescriptionLoader()
    rdl.timeout_seconds = '3.0'
    assert '"timeout_seconds">3.0' in exec_load(rdl)


def test_manipulator_config_file_path():
    rdl = RobotDescriptionLoader()
    rdl.manipulator_config_file_path = 'test/config/file/path'
    assert '"manipulator_config_file_path">test/config/file/path' in exec_load(rdl)


def test_manipulator_links_file_path():
    rdl = RobotDescriptionLoader()
    rdl.manipulator_links_file_path = 'test/links/file/path'
    assert '"manipulator_links_file_path">test/links/file/path' in exec_load(rdl)


def test_use_gazebo():
    # use_gazeboが変更され、xacroにign_ros2_controlがセットされることを期待
    rdl = RobotDescriptionLoader()
    rdl.use_gazebo = 'true'
    assert 'ign_ros2_control/IgnitionSystem' in exec_load(rdl)
