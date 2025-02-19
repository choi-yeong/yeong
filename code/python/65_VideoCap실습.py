
import cv2
import numpy as np
import matplotlib.pyplot as plt

cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    #프레임 표시
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    canny=cv2.Canny(frame,100,100)
    _,thres_frame=cv2.threshold(gray_frame,178,255,cv2.THRESH_BINARY)
    contour,_=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    copy_origin_frame=frame.copy()
    ### [ 엣지강조, 샤프닝] ###
    kernel=np.array([[0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]])
    sharped=cv2.filter2D(frame,-1,kernel)
    cv2.drawContours(copy_origin_frame,contour,-1,(0,255,0),2)
    cv2.imshow('origin stream',frame)
    cv2.imshow('contour stream',copy_origin_frame)
    cv2.imshow('sharp stream',sharped)
    cv2.imshow('canny stream',canny)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release() #비디오 캡쳐 해제
cv2.destroyAllWindows()