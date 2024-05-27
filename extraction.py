import pytesseract
from PIL import Image
import json

# Définir explicitement le chemin de l'exécutable Tesseract si nécessaire
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Charger l'image
image_path = 'Genova.png'
image = Image.open(image_path)

# Utiliser Tesseract pour extraire le texte de l'image
text = pytesseract.image_to_string(image, lang='fra')

# Trouver les emplacements des villes de Gênes et de Camaldoli dans le texte
genoa_location = text.find('Gênes')
camaldoli_location = text.find('Camaldoli')

# Créer la structure JSON des résultats
results = {
    "image": image_path,
    "text_extraction": {
        "cities": {}
    }
}

# Ajouter les informations sur Gênes si trouvé
if genoa_location != -1:
    results["text_extraction"]["cities"]["Gênes"] = {
        "location": genoa_location,
        "confidence": 0.95  # Ajouter un taux de confiance fictif
    }

# Ajouter les informations sur Camaldoli si trouvé
if camaldoli_location != -1:
    results["text_extraction"]["cities"]["Camaldoli"] = {
        "location": camaldoli_location,
        "confidence": 0.85  # Ajouter un taux de confiance fictif
    }

# Afficher les résultats au format JSON
print(json.dumps(results, indent=4))
