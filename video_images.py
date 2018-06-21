'''
by -- ARCHITO
CONVERT VIDEO TO FRAMES,
TRIM VIDEO
'''
import cv2
import numpy as np
import os
import time
# Playing video from file:

fileName = "Yeah_Baby_Garry_Sandhu.mp4"

cap = cv2.VideoCapture(fileName)

print(cap)

# os.makedirs('data')
#video_start_time = int(input('enter the time from which we are to start trimming the video in seconds'))
#video_end_time = int(input("enter the total duration of video until which we are to trim in seconds"))

TotalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

print(" cv2.CAP_PROP_FRAME_COUNT == {}  (cap.get(cv2.CAP_PROP_FRAME_COUNT)) ==  {}   ".format((cv2.CAP_PROP_FRAME_COUNT),TotalFrames))

#error may be maybe not kya pta
'''
try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 1
a=1

while a:
    print("_________________________//")
    if(time.time()>video_start_time):
        print("_________________________//")
        break
    else: 
        currentFrame +=1
        continue


while(currentFrame < TotalFrames and time.time()<video_end_time):
    # Capture frame-by-frame
	
    ret, frame = cap.read()
    print("the value of ret is {}".format(ret))
	
    # Saves image of the current frame in jpg file
    if currentFrame % 10 == 0:
       # name = 'E:\intern\cctv pics' + str(currentFrame+10000000) + '.jpg'
        name = str(currentFrame+10000000) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
'''