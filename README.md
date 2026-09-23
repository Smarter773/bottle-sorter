# AI Plastic Bottle Sorting System

An AI-powered system for detecting, classifying, and sorting plastic bottles using computer vision and machine learning.

## Features
- Real-time bottle detection and classification using YOLO and CNN models
- Conveyor belt control and robotic arm sorting
- Web-based dashboard for monitoring and analytics
- Hardware integration with Arduino and Raspberry Pi
- REST API for external integration

## Deployment with Anaconda

### 1. Install Anaconda
Download from https://www.anaconda.com/download

### 2. Create and activate environment
```bash
conda create -n bottle-sorter python=3.10 -y
conda activate bottle-sorter
```

### 3. Install dependencies
```bash
# Core ML
conda install -c conda-forge opencv numpy pillow -y
conda install -c pytorch pytorch torchvision -y
conda install -c conda-forge tensorflow scikit-learn -y

# Backend
conda install -c conda-forge fastapi uvicorn pydantic sqlalchemy python-dotenv -y

# Analytics
conda install -c conda-forge pandas matplotlib seaborn -y

# Utils
conda install -c conda-forge pyserial psutil scipy cryptography loguru requests -y

# pip-only packages
pip install RPi.GPIO
```

Or install all at once from requirements:
```bash
conda activate bottle-sorter
pip install -r requirements.txt
```

### 4. Run the system

**Main sorting pipeline:**
```bash
python main.py
```

**Backend API (separate terminal):**
```bash
conda activate bottle-sorter
python -m uvicorn backend.app:app --reload --host 0.0.0.0 --port 8000
```

**Run tests:**
```bash
python -m pytest tests/
```

### 5. Deactivate when done
```bash
conda deactivate
```

## Export environment (for other machines)
```bash
conda env export -n bottle-sorter > environment.yml
```
On another machine:
```bash
conda env create -f environment.yml
```

## Project Structure
- `ai_engine/` - Core ML models for detection, classification, tracking
- `computer_vision/` - Camera feed, image capture, frame processing
- `sorting_controller/` - Hardware control for conveyor, robotic arm, pneumatics
- `backend/` - FastAPI REST API server
- `frontend/` - React dashboard UI (requires Node.js)
- `hardware/` - Arduino and Raspberry Pi firmware
- `analytics/` - Performance metrics and reporting
