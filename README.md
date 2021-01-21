#　ROSを使用してストップウォッチを作成した
---

## 動作環境
* OS:ubuntu 20.04 server
* ROS:Noetic
---

## 実行手順
ROSインストール後に下記の手順を行ってください(端末1)
```sh
$ cd ~/catkin_ws/scr
$ git clone https://github.com/ManatoYamaguchi/Robot-system2.git
$ cd..
$ catkin_make
$ source ~/.bashrc
$ cd src/Robot-system2/scripts
$ roscore
```
上記の手順が終わったら下記の手順を別の端末で行ってください(端末2)
```sh
$ cd ~/catkin_ws/src/Robot-system2/scripts
$ chmod +x count_pub.py
$ rosrun Robot-system2 count_pub.py
```
次にさらに別の端末で下記の手順を実行してください(端末3)
```sh
$ cd ~/catkin_ws/src/Robot-system2/scripts
$ chmod +x count_sub.py
$ rosrun Robot-system2 count_sub.py
```
最後に新しい端末を開いてトピックから動作確認を行ってください(端末4)
```sh
$ cd ~/catkin_ws/src/Robot-system2/scripts
$ rostopic list
$ rostopic echo /count_up
```
---

## 実行動画
動画URL：https://youtu.be/VuECCm1N5X
---

## ライセンス
[BSD 3-Clause License](https://github.com/ManatoYamaguchi/Robot-system2/blob/main/LICENSE)
