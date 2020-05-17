import mtcnn_face_detector as mfd
import cv2
import numpy as np

my_input = cv2.imread("test.jpg")
adjusted_input = cv2.resize(my_input,(1000,700))

results,op = mfd.detection(adjusted_input)

cv2.imshow("faces detected",op)
cv2.waitKey(0)
cv2.destroyAllWindows()