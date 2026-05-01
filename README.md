# PlateGuard 🚗

PlateGuard is a Python-based vehicle number plate validation and OCR detection tool that allows users to validate Indian vehicle registration numbers either by entering the number manually or by providing an image path for OCR-based extraction.

This project was built for learning computer vision, OCR integration, regex-based validation, and practical Python project development.

---

## Features

- Manual vehicle number validation
- OCR-based number plate detection from images
- Indian number plate format verification
- Suspicious / invalid plate detection
- User input-based interactive CLI tool

---

## Tech Stack

- Python
- OpenCV
- Pytesseract OCR
- Regex Validation

---

## Project Structure

```text
PlateGuard/
│
├── detect.py
├── README.md
├── .gitignore
└── images/
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/amitraj231226-cmyk/Plate-Guard.git
cd Plate-Guard
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment (Windows)

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install opencv-python pytesseract imutils
```

---

## Install Tesseract OCR

Download and install Tesseract OCR for Windows.

After installation, update the path inside `detect.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## Usage

Run the project:

```bash
python detect.py
```

Program menu:

```text
===== PlateGuard =====
1. Enter Vehicle Number
2. Upload Image Path
```

---

## Example Usage

### Text Input

Input:

```text
MH12AB3456
```

Output:

```text
Plate Detected: MH12AB3456
Status: Valid Indian Number Plate
```

---

### Image Input

Input:

```text
images/car.jpg
```

Output:

```text
Plate Detected: MH12AB3456
Status: Valid Indian Number Plate
```

---

## Validation Logic

PlateGuard validates using the following regex pattern:

```python
^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$
```

Format breakdown:

- 2 State Letters
- 2 RTO Digits
- 2 Series Letters
- 4 Vehicle Digits

Example:

```text
MH12AB3456
```

---

## Current Limitations

This version validates only format.

It does NOT:

- Verify official RTO registration
- Retrieve owner information
- Confirm registration authenticity
- Detect cloned number plates

---

## Future Improvements

- GUI Version
- Real-time Camera Detection
- Plate Suspicion Scoring
- OCR Accuracy Enhancement
- AI-based Fake Plate Detection

---

## Educational Purpose

This project was created for educational and learning purposes to practice:

- OCR Integration
- Computer Vision
- Python Development
- Cybersecurity-related validation systems

---

## Author

**Ajit Raj**  
BCA Student  
Cybersecurity & Python Project Developer

---

## License

MIT License