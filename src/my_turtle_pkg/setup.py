from setuptools import setup

package_name = 'my_turtle_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='emre',
    maintainer_email='example@example.com',
    description='Obstacle stopper node for TurtleBot3',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'obstacle_stopper = my_turtle_pkg.obstacle_stopper:main',
        ],
    },
)

