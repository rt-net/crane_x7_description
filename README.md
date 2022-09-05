[English](README.en.md) | [日本語](README.md)

# crane_x7_description

[![industrial_ci](https://github.com/rt-net/crane_x7_description/workflows/industrial_ci/badge.svg?branch=ros2)](https://github.com/rt-net/crane_x7_description/actions?query=workflow%3Aindustrial_ci+branch%3Aros2)

[CRANE-X7](https://rt-net.jp/products/crane-x7/)のURDFファイルを含むROS 2パッケージです。

## サポートするROSディストリビューション

- Foxy
- Galactic

### ROS 1

- [Melodic](https://github.com/rt-net/crane_x7_description/tree/v1.0.0)
- [Noetic](https://github.com/rt-net/crane_x7_description/tree/v1.0.0)

## インストール方法

```sh
# 本パッケージをクローンし、依存関係をインストールする
mkdir -p ~/dev_ws/src
cd ~/dev_ws/src
git clone -b ros2 https://github.com/rt-net/crane_x7_description
rosdep install -r -y -i --from-paths .

# パッケージをビルドする
cd ~/dev_ws
colcon build --symlink-install
source install/setup.bash
```

## 使用方法

次のコマンドを実行するとRViz上にCRANE-X7のモデルが表示されます

```sh
ros2 launch crane_x7_description display.launch.py
```

![display_launch](https://rt-net.github.io/images/crane-x7/display_launch.png)

## 知的財産権について

CRANE-X7は、アールティが開発した研究用アームロボットです。
このリポジトリのデータ等に関するライセンスについては、[LICENSE](./LICENSE)ファイルをご参照ください。
企業による使用については、自社内において研究開発をする目的に限り、本データの使用を許諾します。
本データを使って自作されたい方は、義務ではありませんが弊社ロボットショップで部品をお買い求めいただければ、励みになります。
商業目的をもって本データを使用する場合は、商業用使用許諾の条件等について弊社までお問合せください。

サーボモータのXM540やXM430に関するCADモデルの使用については、ROBOTIS社より使用許諾を受けています。
CRANE-X7に使用されているROBOTIS社の部品類にかかる著作権、商標権、その他の知的財産権は、ROBOTIS社に帰属します。
