# Face and Eye Detection System

A simple, real-time face and eye detection system built using Python and OpenCV. This application captures video from your default camera and identifies faces and eyes in real-time, highlighting them with distinct colored squares.

## 🚀 Features

- **Real-time Detection**: Uses Haar Cascade classifiers for fast and efficient detection.
- **Visual Feedback**: 
  - **Blue Rectangles**: Highlight detected faces.
  - **Green Rectangles**: Highlight detected eyes within the face region.
- **Text Labels**: Clearly labels 'Face' and 'Eye' on the video stream.
- **Easy Exit**: Press the `q` key to stop the camera and close the application.

---

## 🛠️ Requirements

- **Python 3.x**
- **OpenCV (`opencv-python`)**

---

## 📖 Installation & Setup

1. **Install OpenCV**:
   Run the following command in your terminal or command prompt to install the necessary library:
   ```bash
   pip install opencv-python
   ```

2. **Download the Script**:
   Ensure `face_eye_detector.py` is in your desired working directory.

---

## 🎮 User Manual

### How to Run
1. Open your terminal or powershell.
2. Navigate to the folder containing the script.
3. Execute the script using Python:
   ```powershell
   python face_eye_detector.py
   ```

### Operational Instructions
- **Camera Access**: Once the script starts, it will attempt to open your default camera (index 0). Please ensure no other application is currently using your webcam.
- **Detection Tips**:
  - **Lighting**: Ensure your face is well-lit for better detection accuracy.
  - **Frontal View**: The system is optimized for frontal face detection.
  - **Distance**: Stand at a moderate distance from the camera so your face and eyes are clearly visible.
- **Closing the App**: To stop the detection and close the window, click on the camera window to focus it and press the **`q`** key on your keyboard.

---

## 📂 Code Structure
- `face_eye_detector.py`: The main script containing the logic for camera initialization, frame processing, and object detection.

## 📜 License
This project is open-source and free to use.
