from setuptools import find_packages, setup

# these imports are for resolving the problem with ROS looking for the ddr_rviz.launch.py file in install/shared
import os
from glob import glob

package_name = 'differential_drive_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        (os.path.join('share', package_name), glob('urdf/*.xacro.urdf')),
        (os.path.join('share', package_name), glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='piotr',
    maintainer_email='piotr.bledowski.77@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
