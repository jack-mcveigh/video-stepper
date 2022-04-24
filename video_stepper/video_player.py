import os
import cv2
import random
from typing import List

from config import FRAME_HEIGHT, FRAME_WIDTH


class VideoPlayer:
    def __init__(self, videos: list, video_path: str,
                 fps=24, loop=True, shuffle=False):
        self.videos = videos
        self.video_path = video_path
        self.fps = fps
        self.loop = loop
        self.shuffle = shuffle

    def play(self):
        while True:
            for video in self.video_queue():
                self.__play_video(os.path.join(self.video_path, video))

            if not self.loop:
                break

    def video_queue(self) -> str:
        video_queue = self.__build_queue()
        while video_queue:
            yield video_queue.pop(0)

    def __build_queue(self) -> List[str]:
        new = self.videos.copy()
        if self.shuffle:
            random.shuffle(new)
        return new

    @staticmethod
    def __play_video(video: str, fps=24) -> None:
        mspf = int((1/fps) * 1000)

        cap = cv2.VideoCapture(video)
        if not cap.isOpened():
            raise Exception('Unable to video file.')

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret:
                adj_frame = cv2.resize(frame, (FRAME_WIDTH, FRAME_HEIGHT),
                                       fx=0, fy=0,
                                       interpolation=cv2.INTER_CUBIC)
                cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
                cv2.setWindowProperty("window",
                                      cv2.WND_PROP_FULLSCREEN,
                                      cv2.WINDOW_FULLSCREEN)
                cv2.imshow("window", adj_frame)

                key = cv2.waitKey(mspf) & 0xFF
                if key == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    exit(0)
                elif key == ord('n'):
                    break
            else:
                break
        cap.release()
