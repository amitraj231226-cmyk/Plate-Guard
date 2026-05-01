# PlateGuard 🚗

PlateGuard is a Python-based vehicle number plate validation and OCR detection tool.

It allows users to:

- Validate vehicle numbers through manual text input
- Extract number plate text from vehicle images
- Verify Indian number plate format
- Detect suspicious / invalid plate formats

---

## Features

### Text Input Validation
Users can directly enter a vehicle registration number.

Example:

MH12AB3456

The tool checks whether it follows the standard Indian registration format.

---

### Image-Based Detection
Users can provide an image path.

PlateGuard uses OCR to extract text from the number plate.

---

### Format Validation
Checks if the plate matches the Indian vehicle registration pattern.

Valid format example:

MH12AB3456

---

### Suspicious Plate Detection
Flags plates with invalid formatting.

Example:

M123AB456

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

---
