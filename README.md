
# Gesture Volume Control

This project allows you to control the volume of your Mac computer using hand gestures via a webcam. It uses OpenCV for capturing video, MediaPipe for hand tracking, and osascript to control the system volume.

## Features

- Real-time hand tracking using MediaPipe.
- Volume control by measuring the distance between thumb and index finger.
- Visual feedback with a volume bar displayed on the screen.
- FPS (frames per second) display for performance monitoring.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/GestureVolumeControl.git
   cd GestureVolumeControl
   ```

2. **Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the main script:**

   ```bash
   python GestureVolumeControl.py
   ```

2. **Control the volume:**
   - The volume is controlled by the distance between your thumb (landmark 4) and index finger (landmark 8).
   - A volume bar is displayed on the screen to show the current volume level.
   - The volume is set but moving your ring finger down.

3. **Exit the program:**
   - Press the `q` key to exit the program.

## HandTrackingMin.py

This module contains the minimum code for hand tracking. This serves as a learning material.

## HandTrackingModule.py

This module contains the hand detection and tracking functionality using MediaPipe.

## GestureVolumeControl.py

This script captures the video feed, processes the hand gestures, and sets the system volume using `osascript`.

## Requirements

- Python 3.11
- NumPy
- MediaPipe
- OpenCV
- osascript

## Requirements.txt

The `requirements.txt` file includes all the dependencies needed for the project:

```text
mediapipe==0.10.14
numpy==1.26.4
opencv-python==4.9.0.80
osascript==2020.12.3
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [MediaPipe](https://github.com/google/mediapipe) for the hand tracking solution.
- [OpenCV](https://opencv.org/) for real-time computer vision.
- [osascript](https://pypi.org/project/osascript/) for controlling Mac volume.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Author

- Edward Zou (edwardzou10@gmail.com)
