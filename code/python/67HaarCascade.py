import cv2, pyautogui, mss
import numpy as np
import pygetwindow as gw
## haar cascade xml 파일로드 ##
# 하알캐스케이드 경로찾기
# print(cv2.data.haarcascades)
cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
eyes_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# ### 사람 이미지의 경우 ###
# image=cv2.imread('')# 사진파일의 경우 경로 입력
# #open cv형식으로 변환
# gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #사진의 경우 흑백으로 변환

# #얼굴감지
# faces = cascade.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5,minSize=(30,30))

# #탐지된 얼굴에 사각형 그리기
# for x,y,w,h in faces :
#     cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
# #결과표시
# cv2.imshow('Face Detection', image)

### 화면캡쳐의 경우 ###
window_title="얼굴 : 네이버 이미지검색 - Chrome"  # 원하는 윈도우창 제목 입력
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
        # 얼굴 인식
        faces = cascade.detectMultiScale(gray_frame,scaleFactor=1.1 , minNeighbors=9,minSize=(20,20))
        # 탐지된 얼굴 표시
        for x,y,w,h in faces :
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            # 얼굴에서 눈 감지
            face_roi=gray_frame[y:y+h,x:x+w]
            eyes=eyes_cascade.detectMultiScale(face_roi,scaleFactor=1.1,minNeighbors=13,minSize=(10,10))
            for ex,ey,ew,eh in eyes:
                cv2.rectangle(frame,(x+ex,y+ey),(x+ex+ew,y+ey+eh),(0,255,255),2)

        # 이미지표시
        cv2.imshow('Captured Window',frame)
        if cv2.waitKey(1)&0xFF==ord('q'):
            break


cv2.destroyAllWindows() # 종료 시 모든 캡쳐창 종료