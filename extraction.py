import pytesseract
from PIL import Image

# Définir le chemin vers l'exécutable Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return ""

def main():
    image_path = "Genova.png"
    extracted_text = extract_text_from_image(image_path)
    print(f"Extracted text from {image_path}:")
    print(extracted_text)

if __name__ == "__main__":
    main()
