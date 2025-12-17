from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path):
    try: 
        img = Image.open(image_path.stream)
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print("OCR ERROR:",e)
        return "Could not read text from image. Please try a clearer image."
    
def clean_ocr_text(text):
    text = text.replace("\n"," ")
    text = " ".join(text.split())

    return text
