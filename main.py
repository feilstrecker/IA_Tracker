import cv2
from random import randint

# Put your video name here
cap = cv2.VideoCapture("video.mp4")

ok, frame = cap.read()
if not ok:
    print("failed to read the file.")
    exit()

bbox = cv2.selectROI('Tracker', frame)
color = (randint(0, 255), randint(0, 255), randint(0, 255))
tracker = cv2.legacy.TrackerCSRT_create()

while cap.isOpened():
    ok, frame = cap.read()
    if not ok:
        break

    ok , box = tracker.update(frame)
    (x,y,w,h) = [int(v) for v in box]
    cv2.rectangle(frame, (x,y), (x+w, y+h), color, 2,2)
    cv2.imshow('Tracker', frame)

    if cv2.waitKey(1) & 0XFF == 27:
        break