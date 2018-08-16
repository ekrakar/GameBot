#used to convert mp4 files to images so they can be labeled
import cv2

vidcap = cv2.VideoCapture("C:/Users/eric/Videos/ManyCam/My Recording_5.mp4")#"C:/Users/eric/Desktop/projects/runescape/saved_video/My Recording_5.mp4"
success,image = vidcap.read()
count = 1850
success = True
while success:
  if count % 5 == 0:
      #img = cv2.resize(image, (600, 324))
      cv2.imwrite("C:/Users/eric/Desktop/projects/runescape/images/frame%d.jpg" % (count / 5), image)     # save frame as JPEG file "C:/Users/eric/Desktop/projects/runescape/images/frame%d.jpg"
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
