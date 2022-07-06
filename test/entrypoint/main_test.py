import time
import threading

from unittest import TestCase

from application.entrypoint.entrypoint import EntrypointClass

class EntrypointTest(TestCase):
    def test_main_thread(self):
        entrypoint_instance = EntrypointClass()
        self.assertEqual(len(entrypoint_instance.entrypoint_thread_queue), 0)

        for _ in range(10):
            entrypoint_instance.add_to_queue()

        self.assertEqual(len(entrypoint_instance.entrypoint_thread_queue), 10)

        t = threading.Thread(
            target=entrypoint_instance.entrypoint_threaded_method
        )
        t.start()
        t.join(timeout=2)

        self.assertEqual(len(entrypoint_instance.entrypoint_thread_queue), 0)

        # This is just to print out debug statements.
        self.assertTrue(False)
