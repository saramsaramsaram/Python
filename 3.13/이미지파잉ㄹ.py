from PIL import Image

img = Image.open("sample.jpg")
img.show()  

print("이미지 크기:", img.size)
print("이미지 포맷:", img.format)
print("이미지 모드:", img.mode)