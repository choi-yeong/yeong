import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.ion() #matplotlib 인터렉티브 모드 활성화 (실시간 업데이트)

# 종료 플래그
quit_cap=False

# matplotlib 이벤트 핸들러
def on_key(e):
    global quit_cap
    if e.key=='q':
        quit_cap=True
plt.figure(figsize=(12,4))
# 키 이벤트 연결
plt.gcf().canvas.mpl_connect('key_press_event',on_key)

cap=cv2.VideoCapture(0)
if not cap.isOpened():
    print("웹캠을 열 수 없습니다.")
    exit()

while cap.isOpened():
    ret, frame=cap.read()
    if not ret :
        break

    plt.clf # 기존 그래프 초기화

    # 1. 원본
    original=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    
    plt.subplot(1,3,1)
    plt.imshow(original)
    plt.title('original')
    plt.axis('off')
    # 2. 윤곽선(컨투어) 감지
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    _, thres=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
    contours,_=cv2.findContours(thres,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #컨투어 탐지
    copy_origin=original.copy() # 원본을 카피 (frame을 카피할려고했는데 어차피 BGR2RGB를 또 써줘야해서 original을 카피함)
    cv2.drawContours(copy_origin,contours,-1,(0,255,0),2) #컨투어 그리기 (카피한 원본에 그림) -1: 모든 컨투어를 그림
    plt.subplot(1,3,2)
    plt.imshow(copy_origin)
    plt.title('contour')
    plt.axis('off')
    # 3. 샤프닝 필터 적용
    kernel=np.array([   [0,-1,0],
                        [-1,5,-1],
                        [0,-1,0]    ])
    sharped=cv2.filter2D(original,-1,kernel)
    plt.subplot(1,3,3)
    plt.imshow(sharped)
    plt.title('sharped')
    plt.axis('off')
    
    # 업데이트 간격을 조절
    plt.pause(0.01)

    plt.show()
    if quit_cap:
        print("종료합니다.")
        break

cap.release()
cv2.destroyAllWindows()
plt.close('all') # 모든 matplotlib 닫기