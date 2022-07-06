import time
import threading

from unittest.mock import patch, Mock
from unittest import TestCase

from application.entrypoint.entrypoint import EntrypointClass

class EntrypointTest(TestCase):
    @patch(
        "application.entrypoint.entrypoint.module_level_variable",
        "testing variable"
    )
    @Mock(
        "application.feature_a.feature.RandomFeature.threading.Thread.start",
        return_value=None
    )
    def test_main_thread(
        self,
        feature_thread_start_mock
    ):

        # This is just to print out debug statements.
        self.assertTrue(False)

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
