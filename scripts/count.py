#!/usr/bin/env python3

import rospy
import time

print("１：スタート")
print("２：ストップ")
print("０：終了")

while 1:

    figure = int(input())

    if figure == 1:
        start_time = time.time()
        print("カウントスタート")

    elif figure == 2:
        finish_time = time.time()
        print("カウントストップ")
        print(finish_time - start_time)

    elif figure == 0:
        break
