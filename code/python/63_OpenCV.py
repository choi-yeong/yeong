import cv2
import numpy as np

### [ 기본 이미지 창 띄우기 ] ###
# imagae = cv2. imread("data/coupon.jpg") #imread(괄호) 괄호 안 이미지를 불러온다. (기본값 cv2.IMREAD_COLOR)
# gray_imagae = cv2. imread("data/coupon.jpg",cv2.IMREAD_GRAYSCALE) #imread(괄호) 괄호 안 이미지를 불러온다.
# cv2.imshow("Color Image", imagae) #읽은 이미지를 컬러로 보여준다.
# cv2.imshow("Gray Image", gray_imagae) #읽은 이미지를 흑백으로 보여준다.
# # cv2.waitKey(0) #보여지는 이미지를 바로 종료하지 않고 기다려준다.
# key=cv2.waitKey(0)
# if key==ord('q'):
#     print(chr(key))
# cv2.destroyAllWindows() # 모든 창을 닫는다.

### [ 도형 그리기 ] ###
# width=500
# height = 500
# canvas=np.zeros((height,width,3), dtype=np.uint8)

# #직선그리기(캔버스, 시작점, 끝점, 색상, 두께)
# cv2.line(canvas,(50,50), (450,50), (0,255,0), 3)
# #사각형그리기(캔버스,왼쪽상단,오른쪽하단,색상,두께)
# cv2.rectangle(canvas, (50,100),(200,250),(255,0,0),2)
# #원그리기(캔버스,중심좌표,반지름,색상,두께)
# cv2.circle(canvas,(300,200),50,(0,0,255),-1) #-1은 내부를 채운 원
# #다각형그리기()
# pts=np.array([ [250,300],[350,350],[150,400] ]) #3x2배열
# pts=pts.reshape((-1,1,2)) #reshpe : 배열의 형태를 변경  -1:행렬에 맞게 자동변형
# cv2.polylines(canvas,[pts],isClosed=True,color=(255,255,0),thickness=2) #isClosed:첫점과 마지막점을 이어줄건가?, 
# #텍스트추가(캔버스,텍스트,위치,폰트,글자크기,글자색상,글자굵기)
# cv2.putText(canvas,"Hello OpenCV",(120,450), cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,255),1)
# #FONT_HERSHEY_SIMPLEX:기본값, 산세리프폰트  san체, [san_serif, san:꾸밈없는, serif:꾸밈있는]
# #FONT_HERSHEY_PLAIN : 작은크기의 산세리프폰트
# #FONT_HERSHEY_SCRIPT_SIMPLEX : 필기체 serif체

# cv2.imshow("Canvas",canvas)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


### [ 이미지 색상, 사이즈 변경] ###
# image=cv2.imread("CouponResized.jpg")
# # gray=cv2.cvtColor(image,cv2.COLOR_RGB2GRAY) #흑백변환
# # hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV) #휴값 변환
# # resized=cv2.resize(image, (400,300)) #(폭,높이) 고정값으로 사이즈 변경
# # resized=cv2.resize(image, None, fx=2, fy=4) #(폭,높이) 고정값으로 사이즈 변경
# roi=image[25:100,25:100].copy()
# # # 사진 저장
# # cv2.imwrite("CouponResized.jpg",resized)
# # # 사진 보기
# # cv2.imshow("Gray",gray)
# # cv2.imshow("Hsv",hsv)
# # cv2.imshow("Resize",resized)
# cv2.imshow("Roi",roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows(0)


### [ x값, y값 찾기 및 드래그영역 표시] ###
# start,end=None,None
# def mouse_click(e,x,y,flag,param):
#     global start, end
#     if e==cv2.EVENT_LBUTTONDOWN:
#         print(f"마우스 시작 위치 : x={x}, y={y}")
#         start=(x,y)
#     elif e==cv2.EVENT_LBUTTONUP:
#         print(f"마우스 끝 위치 : x={x}, y={y}")
#         end=(x,y)
#         roi=image[start[1]:end[1],start[0]:end[0]]
#         cv2.imshow("select",roi)


# image=cv2.imread("owl.jpg")
# cv2.imshow("image",image)
# #마우스콜백함수
# cv2.setMouseCallback("image",mouse_click)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

### [ 회전 및 이동 ] ###
image= cv2.imread("owl.png")
#중심좌표
(h,w)=image.shape[:2]
print(h,w)
center=(w//2,h//2) #x축이 넓이, y축이 높이니까.
# #회전
# matrix=cv2.getRotationMatrix2D(center,180.0,1.0) #이미지 회전, 이동을 위해 사용하는 매서드
# rotated=cv2.warpAffine(image, matrix, (w,h))
# 이동 (X방향 100px, y방향 50px)
matrix = np.float32([ [1,0,100],[0,1,50]])
shifted=cv2.warpAffine(image,matrix,(w,h))


cv2.imshow("move",shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()