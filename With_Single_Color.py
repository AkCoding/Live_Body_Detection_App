import cv2

# Load the Cascade Classifier
body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# startt  web cam
cap = cv2.VideoCapture('Body.mp4')