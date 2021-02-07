#!/usr/bin/env python

import time
import rospy
from nav_msgs.msg import Odometry

trajectoryFile = None
timeStamp = None
pitch = None


def odom_callback(data):
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

    trajectoryFile.write(timeStamp + " " + str(tx) + " " + str(ty) + " " + str(
        tz) + " " + str(qx) + " " + str(qy) + " " + str(qz) + " " + str(qw) + "\n")


def writeFile(file):
    # inicializa nodo ROS
    rospy.init_node('extract_data_odometry')
    trajectoryFile = open(file, 'w')

    rospy.Subscriber('/integrated_to_init', Odometry, odom_callback)
    rospy.spin()
    trajectoryFile.close()


if __name__ == '__main__':
    writeFile('trajectory.txt')
