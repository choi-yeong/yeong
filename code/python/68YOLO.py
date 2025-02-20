import cv2,pyautogui
import matplotlib.pyplot as plt
from ultralytics import YOLO
import pygetwindow as gw
import numpy as np
model = YOLO('yolov8n.pt') # 미리 학습된 YOLOv8 모델 불러오기
### [ 이미지 파일의 경우 ] ###
# image_path="test.jpg" #분석할 이미지 경로
# # 객체 탐지
# results=model.predict(source=image_path, save=False, save_txt=False, conf=0.5) #source:이미지, save:저장할것인가?, save_text:탐지된결과를 저장할것인가?, conf:신뢰도 임계값 | 반환값은 탐지 결과의 리스트형태
# # 결과 시각화
# frame=results[0].plot() #plot:탐지된 객체를 시각화한 이미지로 반환.
# resized=cv2.resize(frame, None, fx=0.5, fy=0.5) #(폭,높이) 비율값으로 사이즈 변경
# cv2.imshow("YOLO",resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

### [ 웹캠의 경우 ] ###
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    results=model.predict(source=frame, save=False, save_txt=False, conf=0.5) #source:이미지, save:저장할것인가?, save_text:탐지된결과를 저장할것인가?, conf:신뢰도 임계값 | 반환값은 탐지 결과의 리스트형태
    # 결과 시각화
    frame=results[0].plot() #plot:탐지된 객체를 시각화한 이미지로 반환.
    resized=cv2.resize(frame, None, fx=0.5, fy=0.5) #(폭,높이) 비율값으로 사이즈 변경
    cv2.imshow("YOLO",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release() #비디오 캡쳐 해제
cv2.destroyAllWindows()


### [ 윈도우캡처의 경우 ]  ###
window_title="번화가 사진 : 네이버 이미지검색 - Chrome"  # 원하는 윈도우창 제목 입력
#윈도우 위치 찾기
win=gw.getWindowsWithTitle(window_title)

if not win:
    print("창을 찾을 수 없습니다.")
else :
    win=win[0]
    while True :
        x,y,w,h=win.left, win.top, win.width, win.height
        # 해당영역 캡쳐
        screenshot=pyautogui.screenshot(region=(x,y,w,h))
        # OpenCV 형식변환
        frame=np.array(screenshot)
        frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
        gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # 이미지 인식
        results=model.predict(source=frame, save=False, save_txt=False, conf=0.5) #source:이미지, save:저장할것인가?, save_text:탐지된결과를 저장할것인가?, conf:신뢰도 임계값 | 반환값은 탐지 결과의 리스트형태
        # 결과 시각화
        frame=results[0].plot() #plot:탐지된 객체를 시각화한 이미지로 반환.
        resized=cv2.resize(frame, None, fx=0.5, fy=0.5) #(폭,높이) 비율값으로 사이즈 변경

        # 이미지표시
        cv2.imshow('Captured Window',frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break


cv2.destroyAllWindows() # 종료 시 모든 캡쳐창 종료