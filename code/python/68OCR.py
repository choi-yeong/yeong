import cv2,pyautogui,pytesseract
from ultralytics import YOLO
import pygetwindow as gw
import numpy as np
import matplotlib.pyplot as plt

# Tesseract 경로
pytesseract.pytesseract.tesseract_cmd="C:/Program Files/Tesseract-OCR/tesseract.exe"
# 이미지 전처리
image=cv2.imread("data/car.png")
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
# 블러처리
blur = cv2. GaussianBlur(gray_image,(5,5),0)
# 이진화
thresh= cv2.adaptiveThreshold(blur, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#adaptiveThreshold : 조명에 대응해주는 메서드

# tesseract를 이용해서 이미지에서 텍스트 추출
text = pytesseract.image_to_string(gray_image, lang="kor+eng", config="--psm 1")

print("추출된 텍스트 :", text)

# cv2.imshow("car",thresh)
# cv2.waitKey(0)
# cv2.destroyAllWindows()