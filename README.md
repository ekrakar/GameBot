# GameBot
A simple program that could do some things in RuneScape used for machine learning and python practice

note: This was designed for me to practice combining multiple components in one and shouldn't actually be used to play the game.

Uses Google's Object Detection https://github.com/tensorflow/models/tree/master/research/object_detection
Specifically the ssd_inception_v2 model

Python modules used:
Pyautogui
Numpy
Tensorflow
Pandas
Opencv
Matplotlib

To get the input I used a program called Mannycam to record the screan with the game on it.

The program runs is designed to run up to 4 accounts at once and can do a couple of simple tasks in the game using predefined routines. One of which is fighting cows which utilizes object detection to find the enemies and the items they drop.

Origonally the model was only trained to find enemies. When I later trained it to find items too it was bad at finding the enemies but great at finding the items. I was using this as a school project so I didn't have time to fix this problem as it takes several days to train the model. I ended up with 2 models it used one to find enemies one to find items.


