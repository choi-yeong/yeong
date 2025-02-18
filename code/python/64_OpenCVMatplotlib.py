#Matplotlib과 OpenCV
import cv2
import numpy as np
import matplotlib.pyplot as plt

image=cv2.imread('test_image.jpg')
### [ BGR to RGB 변경 (openCV는 BGR로 읽지만 matplotlib은 RGB로 읽는다.) ] ###
image_rgb=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# cv2.imshow('image',image)
# cv2.imshow('rgb',image_rgb)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# plt.figure(figsize=(10,10))
# plt.subplot(2,2,1)
# plt.imshow(image_rgb)
# plt.title("original")
# plt.axis('off')

# ### [ 블러 처리 ] ###
# # blurred=cv2.blur(image_rgb, (5,5))
# # plt.subplot(2,2,2)
# # plt.imshow(blurred)
# # plt.title("blur")
# # plt.axis('off')

# ### [ 가우시안 블러 처리 ] ###
# # gaussian = cv2.GaussianBlur(image_rgb, (5,5),0)
# # plt.subplot(2,2,3)
# # plt.imshow(gaussian)
# # plt.title("gaussian")
# # plt.axis('off')

# ### [ 미디안 블러 처리 ] ###
# median = cv2.medianBlur(image_rgb,5)
# plt.subplot(2,2,2)
# plt.imshow(median)
# plt.title("median")
# plt.axis('off')

# ### [ 엣지강조, 샤프닝] ###
# kernel=np.array([[0,-1,0],
#                  [-1,10,-1],
#                  [0,-1,0]])
# ## [ 필터적용 ] ##
# sharped=cv2.filter2D(median,-1,kernel)
# plt.subplot(2,2,3)
# plt.imshow(sharped)
# plt.title("kernel")
# plt.axis("off")

### [ 엣지 추출 ] ###
rgb_image=cv2.imread("test_image.jpg")
image=cv2.imread("test_image.jpg",cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=(10,10))
plt.subplot(2,2,1)
plt.imshow(image, cmap="gray")
plt.title("original")
plt.axis('off')

## Sobel 엣지검출 (이미지, 정밀도, x사이즈, y사이즈, 커널사이즈)
# sobel_x=cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)  # x방향 미분
# sobel_y=cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)  # y방향 미분
# sobel_combined=cv2.magnitude(sobel_x, sobel_y) # Sobel 결과 결합
# plt.subplot(2,2,2)
# plt.title("sobel")
# plt.imshow(sobel_combined, cmap="gray")
# plt.axis("off")

# ## Laplacian 엣지검출
# laplacian = cv2.Laplacian(image, cv2.CV_64F)
# plt.subplot(2,2,3)
# plt.title("laplacian")
# plt.imshow(laplacian, cmap="gray")
# plt.axis("off")


## Canny 엣지검출
edges = cv2.Canny(image,100,200)
plt.subplot(2,2,4)
plt.title("edges")
plt.imshow(edges, cmap="gray")
plt.axis("off")

### [ 컨투어 ] ###
# 이진화처리
_,binary = cv2.threshold(edges, 127,255,cv2.THRESH_BINARY)
# 컨투어감지
contour,_=cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #컨투어의 직선만 표시
# 컨투어 원본에 그리기
result_image=rgb_image.copy()
cv2.drawContours(result_image,contour,-1,(0,255,0),2)
plt.subplot(2,2,3)
plt.imshow(result_image)
plt.title("contour")
plt.axis("off")

### [ 컨투어 계산 ] ###
for i in contour:
    #면적 계산
    print(f"면적 : {cv2.contourArea(i)}")
    #중심점 계산
    M=cv2.moments(i)
    if M['m00'] !=0 :
        cx = int(M['m10']/M['m00']) #x 중심
        cy = int(M['m01']/M['m00']) #y 중심
        print(f"중심점 : {cx},{cy}")
        cv2.circle(result_image,(cx,cy),5,(0,0,0),-1) # 중심점 표시
    else :
        print("중심점 찾을 수 없음. m00값이 0임.")
    print(f"둘레 : {cv2.arcLength(i,True)}") #True : 마지막점을 첫점과 close한다는 것.

plt.subplot(2,2,2)
plt.imshow(cv2.cvtColor(result_image,cv2.COLOR_BGR2RGB))



plt.show()