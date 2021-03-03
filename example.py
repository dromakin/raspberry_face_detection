# import cv2
#
# # Load the cascade
# face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
#
# # To capture video from webcam.
# cap = cv2.VideoCapture(0)
# # To use a video file as input
# # cap = cv2.VideoCapture('filename.mp4')
#
# while True:
#     # Read the frame
#     _, img = cap.read()
#     # Convert to grayscale
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     # Detect the faces
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4)
#     # Draw the rectangle around each face
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
#     # Display
#     cv2.imshow('img', img)
#     # Stop if escape key is pressed
#     k = cv2.waitKey(30) & 0xff
#     if k == 27:
#         break
# # Release the VideoCapture object
# cap.release()

# import cv2
# import sys
#
# # cascPath = "haarcascade_frontalface_default.xml"
# cascPath = './haarcascades/haarcascade_frontalface_default.xml'
# faceCascade = cv2.CascadeClassifier(cascPath)

# video_capture = cv2.VideoCapture(0)
#
# while True:
#     # Capture frame-by-frame
#     ret, frame = video_capture.read()
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     faces = faceCascade.detectMultiScale(
#         gray,
#         scaleFactor=1.1,
#         minNeighbors=5,
#         minSize=(30, 30)
#     )
#
#     # Draw a rectangle around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#
#     # Display the resulting frame
#     cv2.imshow('Video', frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# # When everything is done, release the capture
# video_capture.release()
# cv2.destroyAllWindows()


# import cv2
#
#
# def show_webcam(mirror=False):
#     cam = cv2.VideoCapture(0)
#     while True:
#         ret_val, img = cam.read()
#         if mirror:
#             img = cv2.flip(img, 1)
#         cv2.imshow('my webcam', img)
#         if cv2.waitKey(1) == 27:
#             break  # esc to quit
#     cv2.destroyAllWindows()
#
#
# def main():
#     show_webcam(mirror=True)
#
#
# if __name__ == '__main__':
#     main()
#


# import cv2
#
# # initialize the camera
# cam = cv2.VideoCapture(0)
# ret, image = cam.read()
#
# if ret:
#     cv2.imshow('SnapshotTest',image)
#     if cv2.waitKey(1) == 27:
#         # cv2.destroyAllWindows()
#         cv2.destroyWindow('SnapshotTest')
#     cv2.imwrite('/home/pi/SnapshotTest.jpg',image)
# cam.release()
