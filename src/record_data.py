#!/usr/bin/env python

import rospy
import rosbag

from std_msgs.msg import Int32
from sensor_msgs.msg import Image

def callback(msg):
    print msg.data

    with rosbag.Bag('output.bag', 'w') as outbag:
        bag.write('camera/image_raw')

rospy.init_node('record_data')

sub = rospy.Subscriber('/camera/image_raw', Image, callback)
rospy.spin()


