import cv2
import numpy as np
import os

image_path = r"C:\Users\Home Pc\Desktop\PHOTO\5D2402BF-9BB4-4593-B7EF-EDD4AA104DC0.png"    #image
image = cv2.imread(image_path)

if image is None:
    print("Error")
    exit()

original_size = os.path.getsize(image_path)
print(f"Original size: {original_size} bytes")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


shifted = np.roll(gray, 1, axis=1)
correlation = np.corrcoef(gray.flatten(), shifted.flatten())[0, 1]

print(f"Spatial Redundancy (pixel correlation): {correlation:.4f}")

if correlation > 0.90:
    redundancy_type = "High Spatial Redundancy"
elif correlation > 0.70:
    redundancy_type = "Moderate Spatial Redundancy"
else:
    redundancy_type = "Low Spatial Redundancy"

print(f"Identified Redundancy Type: {redundancy_type}")
print("Chosen Compression: JPEG \n")



compressed_path = "compressed.jpg"
cv2.imwrite(compressed_path, image, [int(cv2.IMWRITE_JPEG_QUALITY), 50])

compressed_size = os.path.getsize(compressed_path)
print(f"Compressed size: {compressed_size} bytes")



compression_ratio = original_size / compressed_size
redundancy_percentage = 100 * (1 - 1 / compression_ratio)

print(f"Compression Ratio: {compression_ratio:.2f}")
print(f"Redundancy Percentage: {redundancy_percentage:.2f}%")


compressed_image = cv2.imread(compressed_path)
display_image = cv2.resize(compressed_image, (1000, 840))
cv2.imshow("Compressed Image", display_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
