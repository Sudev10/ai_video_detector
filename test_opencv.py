import cv2
import numpy as np

# Create a black image
img = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw text
cv2.putText(
    img,
    "OpenCV is Working",
    (40, 200),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 255, 0),
    2
)

# Show the image
cv2.imshow("Test Window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
