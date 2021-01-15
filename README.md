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
$ git clone https://github.com/ManatoYamaguchi/Robot-system2.git
$ cd..
$ catkin_make
$ roscore
$ cd ~/catkin_ws/src/Robot-system2/scripts
$ chmod +x count.py
```
上記の手順が終わったら下記の手順を別の端末で行ってください
```sh
$ rosrun Robot-system2 count.py
```
---

## 実行動画
動画URL：https://youtu.be/m8mAcg4AqaA

---

## ライセンス
BSD 3-Clause License
