#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64

while not rospy.is_shutdown():

    rospy.init_node('count')
    pub = rospy.Publisher('count_up', Float64, queue_size = 1)
    rate = rospy.Rate(10)

    print("1:start")
    print("2:stop")

    figure = int(input())

    if figure == 1:
        start_time = rospy.get_time()
        print("count start")

    if figure == 2:
        finish_time = rospy.get_time()
        print("count stop")
        time = finish_time - start_time
        print(time)
        pub.publish(time)


    rate.sleep()
