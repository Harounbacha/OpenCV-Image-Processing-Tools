# 🖼️ OpenCV Image Processing Tools

A collection of Python scripts demonstrating various image processing techniques using OpenCV.

## 🛠️ Features

- Basic image operations (resize, crop)
- Color space conversions (BGR, RGB, HSV, Grayscale)
- Image blurring techniques (Gaussian, Median, Bilateral)
- Video capture and playback
- Image reading and writing

## 📋 Requirements

- Python 3.x
- OpenCV-Python

## 🚀 Installation

```bash
# Clone the repository
git clone https://github.com/Harounbacha/imageWith-cv2.git

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install opencv-python
```

## 📁 Project Structure

```
.
├── data/                    # Image and video files
├── basicImageOperations.py  # Resizing operations
├── colorSpacing.py         # Color space conversions
├── imageBlurring.py        # Blur filtering techniques
├── imageCropping.py        # Image cropping examples
├── read.py                 # Image reading/writing
├── showVideo.py            # Video operations
└── README.md              # Documentation
```

## 💻 Usage Examples

### Image Resizing
```python
import cv2
import os

img = cv2.imread('data/image.png')
resized = cv2.resize(img, (1148, 774))
cv2.imshow('Resized Image', resized)
cv2.waitKey(0)
```

### Color Space Conversion
```python
import cv2

img = cv2.imread('data/image.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
```

### Image Blurring
```python
import cv2

img = cv2.imread('data/image.png')
blurred = cv2.GaussianBlur(img, (5,5), 0)
```

## 📝 Notes

- Image files should be placed in the `data` directory
- Press any key to close image windows
- Default color space in OpenCV is BGR
- Video playback can be stopped with any key press

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details