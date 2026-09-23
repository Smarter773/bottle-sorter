import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    CAMERA_SOURCE = int(os.getenv("CAMERA_SOURCE", "0"))
    MODEL_PATH = os.getenv("MODEL_PATH", "models/bottle_detector.pt")
    CLASSIFICATION_MODEL = os.getenv("CLASSIFICATION_MODEL", "models/classification_model.h5")
    SERIAL_PORT = os.getenv("SERIAL_PORT", "COM3")
    SERIAL_BAUD = int(os.getenv("SERIAL_BAUD", "9600"))
    DB_CONNECTION = os.getenv("DB_CONNECTION", "sqlite:///data/system.db")
    API_HOST = os.getenv("API_HOST", "0.0.0.0")
    API_PORT = int(os.getenv("API_PORT", "8000"))
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    CONVEYOR_SPEED = float(os.getenv("CONVEYOR_SPEED", "1.0"))
    SORTING_THRESHOLD = float(os.getenv("SORTING_THRESHOLD", "0.85"))
    BOTTLE_CATEGORIES = ["PET", "HDPE", "PVC", "LDPE", "PP", "PS", "OTHER"]
    IMAGE_SIZE = (640, 640)
    DEVICE = "cuda" if __import__("torch").cuda.is_available() else "cpu"
