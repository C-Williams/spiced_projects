import logging
import os
from datetime import datetime
import cv2
import numpy as np

from tensorflow.keras.models import load_model
from keras.applications.mobilenet import preprocess_input


def write_image(out, frame):
    """
    writes frame from the webcam as png file to disk. datetime is used as filename.
    """
    if not os.path.exists(out):
        os.makedirs(out)
    now = datetime.now() 
    dt_string = now.strftime("%H-%M-%S-%f") 
    filename = f'{out}/{dt_string}.png'
    logging.info(f'write image {filename}')
    cv2.imwrite(filename, frame)


def key_action():
    # https://www.ascii-code.com/
    k = cv2.waitKey(1)
    if k == 113: # q button
        return 'q'
    if k == 32: # space bar
        return 'space'
    if k == 112: # p key
        return 'p'
    return None


def init_cam(width, height):
    """
    setups and creates a connection to the webcam
    """

    logging.info('start web cam')
    cap = cv2.VideoCapture(0)

    # Check success
    if not cap.isOpened():
        raise ConnectionError("Could not open video device")
    
    # Set properties. Each returns === True on success (i.e. correct resolution)
    assert cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    assert cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    return cap


def predict_frame(image,model_path):
    """
    uses a pretrained model to predict what is contained in the frame
    """

    classes = ['chris_bottle','crista_bottle','gerrit_bottle',
               'helge_bottle','himansu_bottle','moritz_bottle',
               'mykola_bottle','nazila_bottle','renato_bottle',
               'simantini_bottle','empty']
    
    # reverse color channels
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # convert image to numpy array and batch format
    x = np.array(image)
    X = np.array([x]) 

    # use the MobileNet preprocessing for more accurate predictions
    X_preprocess = preprocess_input(X)

    # load the model and make a prediction
    model = load_model(model_path)
    pred = model.predict(X_preprocess)

    # return the value in the prediction array that is the maximum value
    return classes[pred.argmax()]
