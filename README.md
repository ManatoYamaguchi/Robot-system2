#　ROSを使用してストップウォッチを作成した
---

## 動作環境
* OS:ubuntu 20.04 server
* ROS:Noetic
---

## 実行手順
ROSインストール後に下記の手順を行ってください
```sh
$ cd ~/catkin_ws/scr
$ git clone 
$ cd..
$ catkin_make
$ roscore
$ cd ~/catkin_ws/src/mypkg/Robot-system2/scripts
$ chmod +x count.py
```
上記の手順が終わったら下記の手順を別の端末で行ってください
```sh
$ rosrun mypkg count.py
```
---

## 実行動画
動画URL：
---

## ライセンス
BSD 3-Clause License
---
