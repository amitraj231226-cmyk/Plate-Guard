import cv2
import pytesseract
import re
rto_data = {
    "UP32": "Lucknow",
    "UP65": "Varanasi",
    "UP64": "Sonbhadra",
    "UP70": "Allahabad",
    "UP78": "Kanpur",
    "UP53": "Gorakhpur",
    "UP14": "Ghaziabad",
    "UP16": "Noida",
    "UP80": "Agra",
    "UP25": "Bareilly"
}

state_codes = {
    "UP": "Uttar Pradesh",
    "MH": "Maharashtra",
    "DL": "Delhi",
    "RJ": "Rajasthan",
    "MP": "Madhya Pradesh"
}

pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract OCR\tesseract.exe'

pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$'


def validate_plate(plate):
    cleaned = plate.replace(" ", "").replace("\n", "").upper()

    if re.match(pattern, cleaned):
        state = cleaned[:2]
        rto = cleaned[:4]
        series = cleaned[4:6]
        number = cleaned[6:]

        print(f"\nPlate Detected: {cleaned}")
        print("Status: Valid Indian Number Plate")

        if state in state_codes:
            print(f"State: {state_codes[state]}")
        else:
            print("State: Unknown")

        if rto in rto_data:
            print(f"District: {rto_data[rto]}")
        else:
            print("District: Not Found")

        print(f"Series: {series}")
        print(f"Vehicle Number: {number}")

    else:
        print(f"\nPlate Detected: {cleaned}")
        print("Status: Invalid / Suspicious Plate")


def image_mode():
    path = input("Enter image path: ")

    image = cv2.imread(path)

    if image is None:
        print("Image not found!")
        return

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    validate_plate(text)


def text_mode():
    plate = input("Enter vehicle number: ")
    validate_plate(plate)


print("===== PlateGuard =====")
print("1. Enter Vehicle Number")
print("2. Upload Image Path")

choice = input("Choose option (1/2): ")

if choice == "1":
    text_mode()
elif choice == "2":
    image_mode()
else:
    print("Invalid choice")