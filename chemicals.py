import cv2

# Đọc ảnh từ file
image = cv2.imread('cu.jpg')

# Chuyển đổi ảnh sang ảnh đen trắng
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Hiển thị ảnh gốc và ảnh đã xử lý
cv2.imshow('Original Image', image)
cv2.imshow('Processed Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
