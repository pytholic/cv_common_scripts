import os, glob
import cv2
import numpy as np

video_path = '/home/pytholic/Desktop/Projects/icms_data/test_videos/new_car/test.mp4'
frame_number = 500

cap = cv2.VideoCapture(video_path)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width, height)

if frame_number >= 0 & frame_number <= total_frames:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

if (cap.isOpened()== False):
  print("Error opening video stream or file")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

        #print(frame.shape)
        
        # For 4k
        img_right = frame[int(round(0.4166*height, 0)):int(round(0.6944*height, 0)), int(round(0.8203*width, 0)):int(round(0.8984*width, 0))]
        img_left = cv2.flip(frame, 1)
        img_left = img_left[int(round(0.4166*height, 0)):int(round(0.6944*height, 0)), int(round(0.7682*width, 0)):int(round(0.8463*width, 0))]
        img_left = cv2.flip(img_left, 1)

        # img_right = frame[900:1500, 3150:3450]
        # img_left = cv2.flip(frame, 1)
        # img_left = img_left[900:1500, 2950:3250]
        # img_left = cv2.flip(img_left, 1)
        # img_right = frame[800:1400, 2900:3400]
        # img_left = cv2.flip(frame, 1)
        # img_left = img_left[800:1400, 2900:3400]
        # img_left = cv2.flip(img_left, 1)

        # For HD
        # img_right = img[300:900, 1450:1700]
        # img_left = cv2.flip(img, 1)
        # img_left = img_left[300:900, 1450:1700]
        # img_left = cv2.flip(img_left, 1)

        # #horizontal_stack = np.hstack((img_left, img_right))
        horizontal = np.concatenate((img_left, img_right), axis=1)

        cv2.namedWindow("output", cv2.WINDOW_NORMAL)
        cv2.imshow('output', horizontal)

        if cv2.waitKey(0) & 0xFF == ord('q'):
            break
    else:
        break

cap.realease()
cap.destroyAllWindows()
