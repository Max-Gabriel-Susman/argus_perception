from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='realsense2_camera',
            executable='realsense2_camera_node',
            name='realsense2_camera',
            output='screen',
            parameters=[{
                'enable_depth': True,
                'enable_infra1': True,
                'enable_infra2': True,
                'enable_color': True,
                'align_depth': True,
                'pointcloud__neon_.enable': True,
                'pointcloud__neon_.stream_filter': 'color',
                'pointcloud__neon_.stream_index_filter': 0,
                'pointcloud__neon_.ordered_pc': True,
                'pointcloud__neon_.allow_no_texture_points': True,
                'align_depth.enable': True,
                'pointcloud.enable': True,
            }],
        ),
        Node(
            package='argus_perception',
            executable='rs_monitor',
            name='rs_monitor',
            output='screen',
        ),
    ])
