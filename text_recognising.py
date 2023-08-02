import cv2
import pytesseract

# Загрузка изображения
image_path = "/home/slippyslime/Downloads/Untitled.jpeg"
image = cv2.imread(image_path)

# Предобработка изображения
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
threshold_img = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Распознавание текста
# Параметр lang можно изменять в зависимости от того
# на каком языке должен распознаваться текст    
custom_config = r'--oem 3 --psm 6'
text = pytesseract.image_to_string(threshold_img, config=custom_config, lang='rus')

print("Распознанный текст:")
print(text)
