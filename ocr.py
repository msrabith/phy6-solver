from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    return "Solve the physics problem shown in the image."
def clean_ocr_text(text):
    text = text.replace("\n"," ")
    text = " ".join(text.split())

    return text
