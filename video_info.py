import cv2

cap = cv2.VideoCapture("sample.mp4")

if not cap.isOpened():
    print("Cannot open video")
    exit()

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_count += 1

    if frame_count == 1:
        print("Frame shape:", frame.shape)
        print("Data type:", frame.dtype)

cap.release()

print("Total frames:", frame_count)
