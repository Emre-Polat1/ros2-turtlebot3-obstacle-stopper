#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math

class ObstacleStopper(Node):
    def __init__(self):
        super().__init__('obstacle_stopper')
        self.threshold = 0.5
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            qos_profile_sensor_data
        )
        self.get_logger().info("ObstacleStopper baslatildi. Esik: 0.5 m")

    def scan_callback(self, msg: LaserScan):
        ranges = []
        n = len(msg.ranges)
        window = 5
        for i in list(range(0, window)) + list(range(n - window, n)):
            d = msg.ranges[i]
            if math.isfinite(d):
                ranges.append(d)

        if len(ranges) == 0:
            min_dist = float('inf')
        else:
            min_dist = min(ranges)

        twist = Twist()
        if min_dist < self.threshold:
            twist.linear.x = 0.0
            twist.angular.z = 0.0
        else:
            twist.linear.x = 0.2
            twist.angular.z = 0.5

        self.cmd_pub.publish(twist)

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleStopper()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

