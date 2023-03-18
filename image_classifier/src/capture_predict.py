import sys
import logging
import os
import cv2
import numpy as np

from utils import (write_image, 
                   key_action, 
                   init_cam, 
                   predict_frame)



if __name__ == "__main__":

    # folder to write images to
    out_folder = sys.argv[1]

    # maybe you need this
    os.environ['KMP_DUPLICATE_LIB_OK']='True'

    logging.getLogger().setLevel(logging.INFO)
   
    # also try out this resolution: 640 x 360
    webcam = init_cam(640, 480)
    key = None

    # This is used to manipulate how long a prediction is shown on the screen.
    show_pred = False
    counter = 0
      
    try:
        # q key not pressed 
        while key != 'q':
            # Capture frame-by-frame
            ret, frame = webcam.read()
            # fliping the image 
            frame = cv2.flip(frame, 1)
   
            # draw a [224x224] rectangle into the frame, leave some space for the black border 
            offset = 2
            width = 224
            x = 160
            y = 120
            cv2.rectangle(img=frame, 
                          pt1=(x-offset,y-offset), 
                          pt2=(x+width+offset, y+width+offset), 
                          color=(0, 0, 0), 
                          thickness=2
            )     

            # get key event
            key = key_action()

            if key == 'space':
                # write the image without overlay
                # extract the [224x224] rectangle out of it
                image = frame[y:y+width, x:x+width, :]
                write_image(out_folder, image)         
            
            if key == 'p':
                image = frame[y:y+width, x:x+width, :]
                
                # using the model created in keras_2, predict what the image is
                pred = predict_frame(image, './models/water_bottles.h5')

                # print the prediction in the terminal for later reading
                print(pred)

                # change the status of the variable show_pred to true
                show_pred = True
            
            # for my system, 60 frames is about 2 seconds
            if counter == 60:
                show_pred = False
                counter = 0
            
            # show_pred is true, put the prediction text on the screen
            # use red font, in the bottom left corner of the box
            if show_pred:
                font = cv2.FONT_HERSHEY_SIMPLEX 
                pred = pred
                color = (0, 0, 255)
                cv2.putText(frame, pred, (160,340), font, 1, color, 2, cv2.LINE_AA)

                # the counter increases every frame
                counter += 1

            # disable ugly toolbar
            cv2.namedWindow('frame', flags=cv2.WINDOW_GUI_NORMAL)              
            
            # display the resulting frame
            cv2.imshow('frame', frame)            
        
    finally:
        # when everything done, release the capture
        logging.info('quit webcam')
        webcam.release()
        cv2.destroyAllWindows()
