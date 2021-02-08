#!/usr/bin/env python

import time
import rospy
from nav_msgs.msg import Odometry


class Extract:
    def __init__(self):
        self.trajectory_file = None

    def odom_callback(self, data):
        """Extracts the values ​​of type nav_msgs/Odometry."""
        timeStampNum = data.header.stamp.secs + \
            (data.header.stamp.nsecs * 10**(-9))
        timeStamp = str(timeStampNum)

        tx = data.pose.pose.position.x
        ty = data.pose.pose.position.y
        tz = data.pose.pose.position.z

        qx = data.pose.pose.orientation.x
        qy = data.pose.pose.orientation.y
        qz = data.pose.pose.orientation.z
        qw = data.pose.pose.orientation.w

        values = timeStamp + " " + str(tx) + " " + str(ty) + " " + str(
            tz) + " " + str(qx) + " " + str(qy) + " " + str(qz) + " " + str(qw) + "\n"

        self.trajectory_file.write(values)
        print("[DATA] [{}]".format(values))

    def write_file(self, file):
        """Write the output file structure."""
        self.trajectory_file = open(file, 'w')

        rospy.init_node('extract_data_odometry')
        rospy.Subscriber('/integrated_to_init', Odometry, self.odom_callback)
        print(">>> Waiting to extract data ...")
        rospy.spin()

        self.trajectory_file.close()


if __name__ == '__main__':
    try:
        e = Extract()
        e.write_file('trajectory.txt')
    except rospy.ROSInterruptException:
        pass
