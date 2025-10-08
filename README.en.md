[English](README.en.md) | [日本語](README.md)

# crane_x7_description

[![industrial_ci](https://github.com/rt-net/crane_x7_description/actions/workflows/industrial_ci.yml/badge.svg?branch=ros2)](https://github.com/rt-net/crane_x7_description/actions/workflows/industrial_ci.yml)

ROS 2 package with URDF description macro for [CRANE-X7](https://rt-net.jp/products/crane-x7/).

## Table of Contents

- [crane\_x7\_description](#crane_x7_description)
  - [Supported ROS distributions](#supported-ros-distributions)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [How to Use](#how-to-use)
  - [Proprietary Rights](#proprietary-rights)

## Supported ROS distributions

### ROS 2

- [Humble Hawksbill](https://github.com/rt-net/crane_x7_description/tree/humble)
- [Jazzy Jalisco](https://github.com/rt-net/crane_x7_description/tree/jazzy)

## Requirements

- OS
  - Ubuntu Desktop 24.04
- ROS 2
  - Jazzy Jalisco

## Installation

```bash
# Create workspace directory
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src

# Clone package
git clone -b $ROS_DISTRO https://github.com/rt-net/crane_x7_description.git

# Install dependencies
rosdep install -r -y -i --from-paths .

# Build & Install
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash
```


## How to Use

Run the following command to display the CRANE-X7 model in RViz:

```sh
ros2 launch crane_x7_description display.launch.py
```

![display_launch](https://rt-net.github.io/images/crane-x7/display_launch.png)

If you use a [RealSense D435 mounter](https://github.com/rt-net/crane_x7_Hardware/blob/master/3d_print_parts/v1.0/CRANE-X7_HandA_RealSenseD435マウンタ.stl), execute the following command.

```sh
ros2 launch crane_x7_description display.launch.py use_d435:=true
```

![display_launch_use_d435](https://rt-net.github.io/images/crane-x7/display_launch_use_d435.png)

## Proprietary Rights

CRANE-X7 is an arm robot developed by RT Corporation for research purposes.
Please read the [license information contained in this repository](./LICENSE) to find out more about licensing.
Companies are permitted to use the materials made available here for internal, research and development purposes only.
If you are interested in building your own robot for your personal use by utilizing the information made available here, take your time to visit our website and purchase relevant components and parts – that will certainly help us keep going!
Otherwise, if you are interested in manufacturing and commercializing products based on the information herein, please contact us to arrange a license and collaboration agreement with us.

We have obtained permission from ROBOTIS Co., Ltd. to use CAD models relating to servo motors XM540 and XM430.
The proprietary rights relating to any components or parts manufactured by ROBOTIS and used in this product, including but not limited to copyrights, trademarks, and other intellectual property rights, shall remain vested in ROBOTIS.
