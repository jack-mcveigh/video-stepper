from os import path

BASE_PATH = path.abspath(path.dirname(path.dirname(path.dirname(__file__))))
LOG_PATH = path.join(BASE_PATH, 'log')

FRAME_WIDTH = 640
FRAME_HEIGHT = 480

if __name__ == '__main__':
    print(BASE_PATH)
