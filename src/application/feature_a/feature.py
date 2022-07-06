from collections import deque

import threading
import time


class RandomFeature:
    def __init__(self):
        self.feature_random_property = 'asdf'
        self.feature_thread_queue = deque()

        self.feature_thread = threading.Thread(
            target=self.feature_threaded_method
        )
        self.feature_thread.start()

    def feature_threaded_method(self):
        while True:
            if self.feature_thread_queue:
                self.feature_thread_queue.popleft()
            time.sleep(0.1)
