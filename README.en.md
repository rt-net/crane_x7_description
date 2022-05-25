[English](README.en.md) | [日本語](README.md)

# crane_x7_description

[![industrial_ci](https://github.com/rt-net/crane_x7_description/workflows/industrial_ci/badge.svg?branch=master)](https://github.com/rt-net/crane_x7_description/actions?query=workflow%3Aindustrial_ci+branch%3Amaster)

ROS package with URDF description macro for [CRANE-X7](https://rt-net.jp/products/crane-x7/).

This ROS packages was separated from [rt-net/crane_x7_ros](https://github.com/rt-net/crane_x7_ros).

See [rt-net/crane_x7_ros#154](https://github.com/rt-net/crane_x7_ros/issues/154) for details.

## Supported ROS distributions

- Melodic
- Noetic

## Installation

```sh
# Clone crane_x7_description and install dependencies
cd ~/catkin_ws/src
git clone https://github.com/rt-net/crane_x7_description
rosdep install -r -y -i --from-paths .

# Build the package
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

## How to Use

Display a CRANE-X7 robot model on RViz with the following command:

```sh
roslaunch crane_x7_description display.launch 
```

![display_launch](https://rt-net.github.io/images/crane-x7/display_launch.png)

## Proprietary Rights

CRANE-X7 is an arm robot developed by RT Corporation for research purposes.
Please read the [license information contained in this repository](./LICENSE) to find out more about licensing.
Companies are permitted to use the materials made available here for internal, research and development purposes only.
If you are interested in building your own robot for your personal use by utilizing the information made available here, take your time to visit our website and purchase relevant components and parts – that will certainly help us keep going!
Otherwise, if you are interested in manufacturing and commercializing products based on the information herein, please contact us to arrange a license and collaboration agreement with us.

We have obtained permission from ROBOTIS Co., Ltd. to use CAD models relating to servo motors XM540 and XM430.
The proprietary rights relating to any components or parts manufactured by ROBOTIS and used in this product, including but not limited to copyrights, trademarks, and other intellectual property rights, shall remain vested in ROBOTIS.
