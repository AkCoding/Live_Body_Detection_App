import cv2


# Load the Cascade Classifier
body_cascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

# startt  web cam
cap = cv2.VideoCapture('Body.mp4')

while True:

    # read image from webcam
    respose, color_img = cap.read()

    if respose == False:
        break

    # Convert to grayscale
    gray_img = cv2.cvtColor(color_img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = body_cascade.detectMultiScale(gray_img, 1.1, 1)

    # display rectrangle
    for (x, y, w, h) in faces:
        cv2.rectangle(color_img, (x, y), (x + w, y + h), (0, 0, 255), 2)

        # display image
        cv2.imshow('img', color_img)

        # v_writer.write(color_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()