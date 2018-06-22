import cv2
import numpy as np
import os

fileName = "Yeah_Baby_Garry_Sandhu.mp4"

cap = cv2.VideoCapture(fileName)
TotalFrames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total number of frames is {}".format(TotalFrames))
print("________________________/\__________________________")
#__________________________________________________________________________________________
hours = int(input("Input hours of video: ")) * 3600
minutes = int(input("Input minutes video: ")) * 60
seconds = int(input("Input seconds video: "))

Total_duration = + hours + minutes + seconds

print("The  amounts of seconds", Total_duration)

frame_per_sec = TotalFrames/Total_duration 
#__________________________________________________________________________________________
start_hours = int(input("Start Input hours: ")) * 3600
start_minutes = int(input("StaRT Input minutes: ")) * 60
start_seconds = int(input("sTaRt Input seconds: "))

start_time = start_hours + start_minutes + start_seconds

start_frame = frame_per_sec * start_time
print("start time in secs = {} and start frame = {}".format(start_time,start_frame)) 
#__________________________________________________________________________________________

end_hours = int(input("end Input hours: ")) * 3600
end_minutes = int(input("end Input minutes: ")) * 60
end_seconds = int(input("end Input seconds: "))

end_time = end_hours + end_minutes + end_seconds

end_frame = frame_per_sec * end_time
print("end time in secs = {} and end frame = {}".format(end_time,end_frame))
#_________________________________________________________________________________________
curr_frame = 1

while(curr_frame < end_frame ):
    ret, frame = cap.read()
    print("the value of ret is {}".format(ret))
    if(curr_frame > start_frame):
        print("__ __ __ __|||||||||||||||")
        curr_frame += 1
        name = str(curr_frame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)

    else:
        curr_frame += 1