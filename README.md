# eOnsight OCR Project

## Introduction
Ce projet utilise Tesseract OCR pour extraire des textes à partir d'une image, localiser des noms spécifiques et fournir un taux de confiance pour chaque extraction.

## Prérequis
- Python 3.x
- Tesseract OCR (https://github.com/tesseract-ocr/tesseract)

## Installation
1. Clonez ce dépôt :
    ```bash
    git clone <url_du_depot>
    cd eOnsight- Stage
    ```

2. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

3. Installez Tesseract OCR :
    - Téléchargez et installez Tesseract depuis [ce lien](https://github.com/UB-Mannheim/tesseract/wiki).
    - Ajoutez le répertoire d'installation de Tesseract à votre PATH.

4. Assurez-vous que Tesseract est installé correctement en vérifiant sa version :
    ```bash
    tesseract --version
    ```

## Utilisation
Exécutez le script d'extraction :
```bash
python extraction.py
# projet_eOnsight_stage
