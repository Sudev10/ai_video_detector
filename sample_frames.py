import cv2

cap = cv2.VideoCapture("sample.mp4")

if not cap.isOpened():
    print("Cannot open video")
    exit()

frame_index = 0
sample_rate = 10  # take 1 frame every 10 frames
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_index % sample_rate == 0:
        cv2.imwrite(f"frame_{saved}.jpg", frame)
        saved += 1

    frame_index += 1

cap.release()

print(f"Saved {saved} frames")
