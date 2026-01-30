import cv2

# Open the video file
cap = cv2.VideoCapture("sample.mp4")

# Check if video opened successfully
if not cap.isOpened():
    print("Error: Cannot open video")
    exit()

while True:
    ret, frame = cap.read()

    # If no frame is returned, video is over
    if not ret:
        break

    # Show the frame
    cv2.imshow("Video Player", frame)

    # Press 'q' to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
