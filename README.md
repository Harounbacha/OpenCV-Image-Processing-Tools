# Basic Image Operations with OpenCV

This repository contains Python scripts for basic image processing operations using OpenCV.

## 🛠 Requirements

- Python 3.x
- OpenCV-Python (`opencv-python`)

## 📦 Installation

```bash
# Create and activate virtual environment (Windows)
python -m venv .venv
.venv\Scripts\activate

# Install required packages
pip install opencv-python
```

## 🚀 Features

- Image resizing
- Image reading and display
- Basic file operations

## 💻 Usage

```python
# Example of resizing an image
import cv2
import os

# Load and resize image
img = cv2.imread('data/image.png')
resized_img = cv2.resize(img, (1148, 774))

# Display results
cv2.imshow('Original', img)
cv2.imshow('Resized', resized_img)
cv2.waitKey(0)
```

## 📁 Project Structure

```
image tracing/
│
├── data/               # Image files directory
├── main.py            # Main script
├── basicImageOperations.py  # Basic image processing operations
└── README.md          # Project documentation
```

## 📝 Notes

- Place your input images in the `data` directory
- Press any key to close image windows
- Image dimensions are specified in (width, height) format

## 🤝 Contributing

Feel free to open issues and pull requests for improvements.

## 📄 License

MIT License