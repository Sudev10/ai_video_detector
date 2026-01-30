import cv2
import numpy as np

cap = cv2.VideoCapture("sample.mp4")

edge_strengths = []
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    if frame_count % 10 == 0:  # sample every 10th frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        strength = np.mean(edges)
        edge_strengths.append(strength)

    frame_count += 1

cap.release()

mean = np.mean(edge_strengths)
std = np.std(edge_strengths)
cv = std / mean

print("Frames analyzed:", len(edge_strengths))
print("Mean edge strength:", mean)
print("CV (consistency score):", cv)

if cv > 0.35:
    print("⚠️ AI likelihood: HIGH")
elif cv > 0.2:
    print("⚠️ AI likelihood: MEDIUM")
else:
    print("✅ AI likelihood: LOW")
G