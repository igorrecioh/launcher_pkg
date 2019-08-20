from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    ld = LaunchDescription([
        Node(package='ros2_geek_pkg', node_executable='geek_publisher', output='screen'),
	Node(package='ros2_geek_pkg', node_executable='geek_subscriber', output='screen')
    ])
    return ld


if __name__ == '__main__':
    generate_launch_description()
