#이미지처리
import cv2
import numpy as np

#이미지 읽어서 크기 출력
image=cv2.imread("owl.png")
(h,w)=image.shape[:2]
print("이미지 크기 = " ,w,":",h)
#흑백변환 후 표시
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #흑백변환
cv2.imshow("gray",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#50%크기로 축소 후 표시
resized_image=cv2.resize(image,None,None,fx=0.5,fy=0.5)
cv2.imshow("resize",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#90도 회전 후 사진파일 저장
(rh,rw)=resized_image.shape[:2]
print("변경된 이미지 크기 = " ,rw,":",rh)
center=(rw//2,rh//2)
matrix=cv2.getRotationMatrix2D(center,90.0,1.0) #이미지 회전, 이동을 위해 사용하는 매서드
rotated=cv2.warpAffine(resized_image, matrix, (rw,rh))
# cv2.imwrite("rotated_owl.png",rotated) #저장

cv2.imshow("rotate",rotated) #보기
cv2.waitKey(0)
cv2.destroyAllWindows()