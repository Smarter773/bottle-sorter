import sys
import signal
import cv2
from loguru import logger

from config import Config
from ai_engine.detection import BottleDetector
from ai_engine.classification import BottleClassifier
from computer_vision.camera_feed import CameraFeed
from computer_vision.frame_processing import FrameProcessor
from sorting_controller.conveyor_control import ConveyorController
from sorting_controller.pneumatic_sorter import PneumaticSorter
from backend.app import create_app


class BottleSortingSystem:
    def __init__(self):
        self.running = False
        self.detector = BottleDetector()
        self.classifier = BottleClassifier()
        self.camera = CameraFeed()
        self.processor = FrameProcessor()
        self.conveyor = ConveyorController()
        self.sorter = PneumaticSorter()
        self.api = None

    def start(self):
        logger.info("Starting Bottle Sorting System")
        self.detector.load_model(Config.MODEL_PATH)
        self.classifier.load_model(Config.CLASSIFICATION_MODEL)
        self.camera.start()
        self.conveyor.start()
        self.sorter.initialize()
        self.running = True
        self.api = create_app()
        self._main_loop()

    def _main_loop(self):
        while self.running:
            frame = self.camera.read_frame()
            if frame is None:
                continue
            processed = self.processor.process(frame)
            detections = self.detector.detect(processed)
            for det in detections:
                bottle_type = self.classifier.classify(det["crop"])
                self.sorter.sort(bottle_type)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                self.stop()

    def stop(self):
        logger.info("Shutting down system")
        self.running = False
        self.camera.release()
        self.conveyor.stop()
        self.sorter.shutdown()


if __name__ == "__main__":
    system = BottleSortingSystem()
    signal.signal(signal.SIGINT, lambda s, f: system.stop())
    system.start()
