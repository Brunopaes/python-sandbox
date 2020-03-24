import dlib
import cv2


class FaceRecognition:
    def __init__(self):
        self.cnn_face_detector = \
            dlib.cnn_face_detection_model_v1('./mmod_human_face_detector.dat')
        self.video_capture = cv2.VideoCapture(0)

        self.x, self.y, self.h, self.w = 0, 0, 0, 0

    # Used in __call__
    def get_video(self):
        """This function captures a video frame.

        Returns
        -------

        """
        return self.video_capture.read()

    # Used in __call__
    def draw_rectangle(self, frame):
        """This function draws a red rectangle around the detected face.

        Parameters
        ----------
        frame

        Returns
        -------

        """
        cv2.rectangle(
            frame, (self.x, self.y), (self.x + self.w, self.y + self.h),
            (0, 0, 255), 2)
        cv2.imshow('Video', frame)

    # Used in __call__
    def detect_face(self, frame):
        """This function draws a red rectangle around the detected face.

        Parameters
        ----------
        frame

        Returns
        -------

        """
        for face in self.cnn_face_detector(frame, 1):
            self.x = face.rect.left()
            self.y = face.rect.top()
            self.w = face.rect.right() - self.x
            self.h = face.rect.bottom() - self.y

    def __call__(self, *args, **kwargs):
        while True:
            rec, frame = self.get_video()
            self.detect_face(frame)
            self.draw_rectangle(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.video_capture.release()
        cv2.destroyAllWindows()
