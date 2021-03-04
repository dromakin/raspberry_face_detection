import os
import glob
import face_recognition
import logging

from config.settings import DB_DIR

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


def init():
    logging.info("Start searching images.")
    jpgFilenamesList = glob.glob(os.path.join(DB_DIR, '*.jpg'))
    known_face_names_ = list()
    known_face_encodings_ = list()
    # print(jpgFilenamesList)

    str_log = str()

    for file in jpgFilenamesList:
        str_log += f"image find: {file}. "

        name = file.split(".")[0]
        known_face_names_.append(name)

        # print(os.path.join(DB_DIR, file))
        # print(name)

        image = face_recognition.load_image_file(os.path.join(DB_DIR, file))
        image_encoding = face_recognition.face_encodings(image)[0]

        str_log += "Detection ready! "

        known_face_encodings_.append(image_encoding)

        str_log += "Done!"

        logging.info(str_log)

    return known_face_encodings_, known_face_names_
