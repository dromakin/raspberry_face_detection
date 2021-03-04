from argparse import ArgumentParser
import subprocess
import datetime


def take_photo(filename: str = None):
    if filename is None:
        filename = '/home/pi/Desktop/image.jpg'

    # raspistill -o cam.jpg
    subprocess.run(["raspistill", "-o", filename, ])


if __name__ == '__main__':
    parser = ArgumentParser()
    date = str(datetime.datetime.now())
    parser.add_argument("-f", "--file", dest="filename",
                        help="write image to file. Use jpg postfix.",
                        default=f"/home/pi/Documents/face_detection/db/{date}.jpg")

    args = parser.parse_args()
    take_photo(args.filename)
