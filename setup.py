from setuptools import setup, find_packages

package_name = 'argus_perception'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # INSTALL THE LAUNCH FILE(S):
        ('share/' + package_name + '/launch', ['launch/realsense_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Max Gabriel Susman',
    maintainer_email='gabe.susman@gmail.com',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'rs_monitor = argus_perception.rs_monitor:main',
        ],
    },
)
