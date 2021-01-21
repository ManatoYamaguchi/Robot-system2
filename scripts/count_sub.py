#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

def cb(message):
    print(message.data)

if __name__ == "__main__":
    rospy.init_node('count_sub')
    sub = rospy.Subscriber('count_up', Float64, cb)
    rospy.spin()
