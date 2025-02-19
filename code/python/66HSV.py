import cv2
import matplotlib.pyplot as plt
import numpy as np


### [ HSV ] ###
# image = cv2.imread("test_image.jpg")

# # BGR->HSV 변환
# hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# # cv2.imshow("hsv", hsv_image)
# # cv2.waitKey(0)
# # cv2.destroyAllWindows()

# # # 색상범위 설정(빨강색)
# r_lower = np.array([0, 120, 70])
# r_upper = np.array([10, 255, 255])
# # (-10, 100, 100) ~ (10, 255, 255)

# # 색상범위 설정(파란색)
# b_lower = np.array([90, 100, 100])
# b_upper = np.array([120, 255, 255])
# # (110, 100, 100) ~ (130, 255, 255)

# # 색상범위 설정(초록색)
# g_lower = np.array([50, 100, 100])
# g_upper = np.array([70, 255, 255])
# # (50, 100, 100) ~ (70, 255, 255)


# # 마스크생성
# r_mask = cv2.inRange(hsv_image, r_lower, r_upper)
# g_mask = cv2.inRange(hsv_image, g_lower, g_upper)
# b_mask = cv2.inRange(hsv_image, b_lower, b_upper)

# # 원본이미지에 마스크 적용
# r_result = cv2.bitwise_and(image, image, mask=r_mask) # 앞의 사진(image)에 뒤에 사진을 마스크함
# g_result = cv2.bitwise_and(image, image, mask=g_mask)
# b_result = cv2.bitwise_and(image, image, mask=b_mask)

# plt.figure(figsize=(8, 8))
# # 원본
# plt.subplot(3, 3, 2)
# plt.title("original")
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.axis("off")

# # 레드마스크
# plt.subplot(3, 3, 4)
# plt.title("r_mask")
# plt.imshow(r_mask, cmap="gray")
# plt.axis("off")
# # 그린마스크
# plt.subplot(3, 3, 5)
# plt.title("g_mask")
# plt.imshow(g_mask, cmap="gray")
# plt.axis("off")
# # 블루마스크
# plt.subplot(3, 3, 6)
# plt.title("b_mask")
# plt.imshow(b_mask, cmap="gray")
# plt.axis("off")

# # 레드_결과
# plt.subplot(3, 3, 7)
# plt.title("result")
# plt.imshow(cv2.cvtColor(r_result, cv2.COLOR_BGR2RGB))
# plt.axis("off")
# # 그린_결과
# plt.subplot(3, 3, 8)
# plt.title("result")
# plt.imshow(cv2.cvtColor(g_result, cv2.COLOR_BGR2RGB))
# plt.axis("off")
# # 블루_결과
# plt.subplot(3, 3, 9)
# plt.title("result")
# plt.imshow(cv2.cvtColor(b_result, cv2.COLOR_BGR2RGB))
# plt.axis("off")

# plt.show()

### [ erode 와 dilate ] ###
# image = cv2.imread("test_image.jpg")
# hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
# lower=np.array([100,150,0])
# upper=np.array([140,255,255])
# #마스크 생성
# mask=cv2.inRange(hsv,lower,upper)
# #커널
# kerner=np.ones((5,5), np.uint8)
# #침식연산: 작은 노이즈 등, 객체의 경계를 줄임.
# mask_eroded=cv2.erode(mask,kerner,iterations=2) # None:3x3 기본커널
# #팽창연산: 객체의 경계를 확장하거나 침식 후 복원.
# mask_dilated=cv2.dilate(mask,kerner,iterations=2)


# fig,axes = plt.subplots(2,2,figsize=(4,4))
# #원본
# axes[0,0].imshow(cv2.cvtColor(image,cv2.COLOR_BGR2RGB))
# axes[0,0].set_title("original")
# axes[0,0].axis('off')
# #마스크
# axes[0,1].imshow(mask,cmap='gray')
# axes[0,1].set_title("mask")
# axes[0,1].axis('off')
# #침식
# axes[1,0].imshow(mask_eroded,cmap='gray')
# axes[1,0].set_title("erode")
# axes[1,0].axis('off')
# #팽창
# axes[1,1].imshow(mask_dilated,cmap='gray')
# axes[1,1].set_title("dilate")
# axes[1,1].axis('off')

# plt.tight_layout()
# plt.show()


cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    ### [ 스킨 검출 ] ###
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #피부색 범위(살구색 기준)
    #H:0~20, S:48~255, V:80~255
    lower=np.array([0,40,130])
    upper=np.array([50,255,255])
    ##마스크화
    mask=cv2.inRange(hsv,lower,upper)
    #노이즈 제거
    kernel=np.ones((5,5),np.uint8)
    #침식
    mask_eroded=cv2.erode(mask,kernel,iterations=1)
    #팽창
    mask_dilated=cv2.dilate(mask,kernel,iterations=1)
    ##컨투어 윤곽선
    #우리가 원하는 영역은 mask된 영역
    contours,_=cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #원본이미지에 윤곽선 그리기
    frame_copy=frame.copy()
    cv2.drawContours(frame_copy,contours,-1,(0,255,0),2)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('contours',frame_copy)
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release() #비디오 캡쳐 해제
cv2.destroyAllWindows()