from collections import deque

from application import module_level_variable
from application.feature_a.feature import RandomFeature

import time


class EntrypointClass():
    def __init__(self):
        self.random_feature = RandomFeature()
        self.entrypoint_thread_queue = deque()

    def entrypoint_threaded_method(self):
        while True:
            if self.entrypoint_thread_queue:
                element = self.entrypoint_thread_queue.popleft()
                print(element)
            time.sleep(0.1)

    def add_to_queue(self):
        self.entrypoint_thread_queue.append(module_level_variable)
