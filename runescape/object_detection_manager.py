#adaptation of a version from https://towardsdatascience.com/how-to-train-your-own-object-detector-with-tensorflows-object-detector-api-bec72ecfe1d9
#handles the graphs video input and image processing
import time
import argparse
import multiprocessing
import numpy as np
import tensorflow as tf

from runescape.bot_main import RunBot
from runescape.app_utils import FPS, WebcamVideoStream
from multiprocessing import Queue, Pool
from object_detection.utils import label_map_util

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT1 = 'interfacegraphs/frozen_inference_graph1.pb'
PATH_TO_CKPT2 = 'interfacegraphs/frozen_inference_graph2.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = 'training/object-detection.pbtxt'

NUM_CLASSES = 3

# Loading label map
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def detect_objects(image_np, sess, detection_graph, obj):
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
    image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

    # Each box represents a part of the image where a particular object was detected.
    boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

    # Each score represent how level of confidence for each of the objects.
    # Score is shown on the result image, together with the class label.
    scores = detection_graph.get_tensor_by_name('detection_scores:0')
    classes = detection_graph.get_tensor_by_name('detection_classes:0')
    num_detections = detection_graph.get_tensor_by_name('num_detections:0')

    # Actual detection.
    (boxes, scores, classes, num_detections) = sess.run(
        [boxes, scores, classes, num_detections],
        feed_dict={image_tensor: image_np_expanded})

    i = 0
    output = []
    while scores[0, i] > .4:
        if int(classes[0, i]) == obj:   
            elem = [0, 0, 0]
            elem[0] = classes[0, i]
            elem[1] = (boxes[0, i, 0] + boxes[0, i, 2]) / 2
            elem[2] = (boxes[0, i, 1] + boxes[0, i, 3]) / 2
            output.append(elem)
            i += 1
    return output


def worker(input_q, output_q):
    # Load a (frozen) Tensorflow model into memory.
    # this is the graph used for detecting enemies
    detection_graph1 = tf.Graph()
    with detection_graph1.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT1, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess1 = tf.Session(graph=detection_graph1)
        
    # Load a (frozen) Tensorflow model into memory.
    # this is the graph used for detecting items
    detection_graph2 = tf.Graph()
    with detection_graph2.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(PATH_TO_CKPT2, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def, name='')

        sess2 = tf.Session(graph=detection_graph2)

    #loop for getting the input images and matchign with the correct model
    while True:
        input_list = input_q.get()
        frame = input_list[0]
        graph = input_list[1]
        if graph == 1:
            output_q.put(detect_objects(frame, sess1, detection_graph1, 1))
        else:
            output_q.put(detect_objects(frame, sess2, detection_graph2, 3))


if __name__ == '__main__':
    #default values for the input
    parser = argparse.ArgumentParser()
    parser.add_argument('-src', '--source', dest='video_source', type=int,
                        default=0, help='Device index of the camera.')
    parser.add_argument('-wd', '--width', dest='width', type=int,
                        default=1280, help='Width of the frames in the video stream.')
    parser.add_argument('-ht', '--height', dest='height', type=int,
                        default=720, help='Height of the frames in the video stream.')
    parser.add_argument('-num-w', '--num-workers', dest='num_workers', type=int,
                        default=1, help='Number of workers.')
    parser.add_argument('-q-size', '--queue-size', dest='queue_size', type=int,
                        default=1, help='Size of the queue.')
    args = parser.parse_args()

    #setup logging
    logger = multiprocessing.log_to_stderr()
    logger.setLevel(multiprocessing.SUBDEBUG)

    #setsup the processes used to process the images
    input_q1 = Queue(maxsize=args.queue_size)
    output_q1 = Queue(maxsize=args.queue_size)
    input_q2 = Queue(maxsize=args.queue_size)
    output_q2 = Queue(maxsize=args.queue_size)
    input_q3 = Queue(maxsize=args.queue_size)
    output_q3 = Queue(maxsize=args.queue_size)
    input_q4 = Queue(maxsize=args.queue_size)
    output_q4 = Queue(maxsize=args.queue_size)
    pool1 = Pool(args.num_workers, worker, (input_q1, output_q1))
    pool2 = Pool(args.num_workers, worker, (input_q2, output_q2))
    pool3 = Pool(args.num_workers, worker, (input_q3, output_q3))
    pool4 = Pool(args.num_workers, worker, (input_q4, output_q4))
    pools = [[pool1, input_q1, output_q1], [pool2, input_q2, output_q2], [pool3, input_q3, output_q3], [pool4, input_q4, output_q4]]

    #sets up the camera
    video_capture = WebcamVideoStream(src=args.video_source,
                                      width=args.width,
                                      height=args.height).start()
    #gives the processes time to load the models before continueing
    time.sleep(15)
    bot = RunBot(pools, video_capture)
    bot.update()


