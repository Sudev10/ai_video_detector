import cv2
import numpy as np
import os

edge_strengths = []

for file in os.listdir():
    if file.startswith("frame_") and file.endswith(".jpg"):
        img = cv2.imread(file)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        edges = cv2.Canny(gray, 100, 200)
        strength = np.mean(edges)

        edge_strengths.append(strength)

print("Edge strengths per frame:")
for i, s in enumerate(edge_strengths):
    print(f"Frame {i}: {s:.2f}")

print("\nAverage edge strength:", np.mean(edge_strengths))
