import cv2
import pytesseract
import re
rto_data = {
    "UP11": "Saharanpur",
    "UP12": "Muzaffarnagar",
    "UP13": "Bulandshahr",
    "UP14": "Ghaziabad",
    "UP15": "Meerut",
    "UP16": "Noida",
    "UP17": "Baghpat",
    "UP19": "Shamli",
    "UP20": "Bijnor",
    "UP21": "Moradabad",
    "UP22": "Rampur",
    "UP23": "Jyotiba Phule Nagar",
    "UP24": "Badaun",
    "UP25": "Bareilly",
    "UP26": "Pilibhit",
    "UP27": "Shahjahanpur",
    "UP30": "Hardoi",
    "UP31": "Lakhimpur Kheri",
    "UP32": "Lucknow",
    "UP33": "Raebareli",
    "UP34": "Sitapur",
    "UP35": "Unnao",
    "UP36": "Amethi",
    "UP40": "Bahraich",
    "UP41": "Barabanki",
    "UP42": "Faizabad",
    "UP43": "Gonda",
    "UP44": "Sultanpur",
    "UP45": "Ambedkar Nagar",
    "UP46": "Shrawasti",
    "UP47": "Balrampur",
    "UP50": "Azamgarh",
    "UP51": "Basti",
    "UP52": "Deoria",
    "UP53": "Gorakhpur",
    "UP54": "Mau",
    "UP55": "Siddharthnagar",
    "UP56": "Maharajganj",
    "UP57": "Padrauna",
    "UP58": "Sant Kabir Nagar",
    "UP60": "Ballia",
    "UP61": "Ghazipur",
    "UP62": "Jaunpur",
    "UP63": "Mirzapur",
    "UP64": "Sonbhadra",
    "UP65": "Varanasi",
    "UP66": "Bhadohi",
    "UP67": "Chandauli",
    "UP70": "Prayagraj",
    "UP71": "Fatehpur",
    "UP72": "Pratapgarh",
    "UP73": "Kaushambi",
    "UP74": "Kannauj",
    "UP75": "Etawah",
    "UP76": "Farrukhabad",
    "UP77": "Kanpur Dehat",
    "UP78": "Kanpur Nagar",
    "UP79": "Auraiya",
    "UP80": "Agra",
    "UP81": "Aligarh",
    "UP82": "Etah",
    "UP83": "Firozabad",
    "UP84": "Mainpuri",
    "UP85": "Mathura",
    "UP86": "Mahamaya Nagar",
    "UP87": "Kanshiram Nagar",
    "UP90": "Banda",
    "UP91": "Hamirpur",
    "UP92": "Jalaun",
    "UP93": "Jhansi",
    "UP94": "Lalitpur",
    "UP95": "Mahoba",
    "UP96": "Chitrakoot"
}

state_codes = {
    "UP": "Uttar Pradesh",
    "MH": "Maharashtra",
    "DL": "Delhi",
    "RJ": "Rajasthan",
    "MP": "Madhya Pradesh"
}

from plateguard_dashboard import save_scan, show_dashboard

pytesseract.pytesseract.tesseract_cmd = r'E:\Tesseract OCR\tesseract.exe'

pattern = r'^[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}$'


def validate_plate(plate):
    cleaned = plate.replace(" ", "").replace("\n", "").upper()

    if re.match(pattern, cleaned):
        state = cleaned[:2]
        rto = cleaned[:4]
        series = cleaned[4:6]
        number = cleaned[6:]

        save_scan(
            cleaned,
            "Valid",
            state_codes.get(state, "Unknown"),
            rto_data.get(rto, "Unknown")
        )

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
        
        save_scan(cleaned, "Invalid")


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
print("3. View Scan History")

choice = input("Choose option (1/2/3): ")

if choice == "1":
    text_mode()
elif choice == "2":
    image_mode()
elif choice == "3":
    show_dashboard()
else:
    print("Invalid choice")