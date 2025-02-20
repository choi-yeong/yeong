import cv2, pyautogui, mss
import numpy as np
import pygetwindow as gw

window_title="새 탭"  # 원하는 윈도우창 제목 입력
#윈도우 위치 찾기
win=gw.getWindowsWithTitle(window_title)

if not win:
    print("창을 찾을 수 없습니다.")
else :
    win=win[0]
    with mss.mss() as sct: # mss 객체 생성
        while True :
            x,y,w,h=win.left, win.top, win.width, win.height
            # 다중 모니터 지원을 위한 캡처
            monitor = {
                "left": x,
                "top": y,
                "width": w,
                "height": h
            }
            screenshot = sct.grab(monitor)  # mss로 캡처
            # OpenCV 형식변환
            frame=np.array(screenshot)
            # frame=cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
            gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            
            # 이미지 인식
            # results=model.predict(source=frame, save=False, save_txt=False, conf=0.5) #source:이미지, save:저장할것인가?, save_text:탐지된결과를 저장할것인가?, conf:신뢰도 임계값 | 반환값은 탐지 결과의 리스트형태
            
            # 색깔 인식(색깔 필터링)
            hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            # 색상범위 설정(초록색)
            colors = { # [ (lower), (upper), (바운딩박스컬러)  ]
                "Red": [(0, 120, 70), (10, 255, 255), (15, 15, 255)],
                "Green": [(35, 50, 50), (60, 255, 255), (15, 255, 15)],
                "Blue": [(90, 150, 0), (150, 255, 255), (255, 15, 15)]
            }
            frame_copy=frame.copy()
            for color_name, (lower, upper, box_color) in colors.items():
                mask = cv2.inRange(hsv, np.array(lower), np.array(upper))

                # 노이즈 제거
                kernel = np.ones((3, 3), np.uint8)
                mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
                mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

                # 윤곽선 검출
                contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # 바운딩 박스 및 텍스트 추가
                for contour in contours:
                    x, y, w, h = cv2.boundingRect(contour)
                    if w > 10 and h > 10:
                        cv2.rectangle(frame_copy, (x, y), (x + w, y + h), box_color, 2)
                        cv2.putText(frame_copy, color_name, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)

            # 결과 시각화
            # frame=results[0].plot() #plot:탐지된 객체를 시각화한 이미지로 반환.
            resized=cv2.resize(frame_copy, None, fx=0.75, fy=0.75) #(폭,높이) 비율값으로 사이즈 변경

            # 이미지표시
            cv2.imshow('Captured Window',resized)
            if cv2.waitKey(1)&0xFF==ord('q'):
                break


cv2.destroyAllWindows() # 종료 시 모든 캡쳐창 종료