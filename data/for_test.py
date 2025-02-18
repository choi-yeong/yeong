from matplotlib import font_manager

# 폰트 이름 확인
path = "Pretendard.ttf"
font = font_manager.FontProperties(fname=path).get_name()
print("설정된 폰트 이름:", font)