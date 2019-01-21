import cv2
import os
import image_processing
import webCrawler

DEBUG_LOG = True


def retrieve_all_images():
    return webCrawler.gather_images()


casc_path = "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(casc_path)


if __name__ == "__main__":

    images = retrieve_all_images()

    for image_name in images:
        try:
            image = cv2.imread(image_name)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30)
            )

            if len(faces) == 0:  # If no face is detected, remove from directory
                os.remove(image_name)
            else:
                for (x, y, w, h) in faces:
                    if DEBUG_LOG:
                        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        cv2.imshow("Image", image)
                        cv2.waitKey(0)
                    image_processing.crop_image(x, y, h, w, image_name)
                    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        except:
            if DEBUG_LOG:
                print("error")
