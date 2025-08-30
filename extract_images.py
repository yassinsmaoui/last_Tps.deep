#!/usr/bin/env python3
"""
Script pour extraire toutes les images du notebook Jupyter et les sauvegarder
dans le dossier img/
"""

import json
import base64
import os
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def extract_images_from_notebook(notebook_path, output_dir):
    """
    Extrait toutes les images d'un notebook Jupyter et les sauvegarde
    """
    # Créer le dossier de sortie s'il n'existe pas
    output_dir = Path(output_dir)
    output_dir.mkdir(exist_ok=True)
    
    # Charger le notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    image_count = 0
    
    print(f"📂 Extraction des images vers {output_dir}/")
    print("="*50)
    
    # Parcourir toutes les cellules
    for cell_idx, cell in enumerate(notebook['cells']):
        if cell['cell_type'] == 'code' and 'outputs' in cell:
            # Parcourir tous les outputs de la cellule
            for output_idx, output in enumerate(cell['outputs']):
                if 'data' in output:
                    data = output['data']
                    
                    # Vérifier s'il y a des images PNG
                    if 'image/png' in data:
                        image_count += 1
                        # Décoder l'image base64
                        img_data = base64.b64decode(data['image/png'])
                        
                        # Nom du fichier
                        filename = f"cell_{cell_idx:02d}_output_{output_idx:02d}_image_{image_count:02d}.png"
                        filepath = output_dir / filename
                        
                        # Sauvegarder l'image
                        with open(filepath, 'wb') as f:
                            f.write(img_data)
                        
                        print(f"✅ Image {image_count}: {filename}")
                    
                    # Vérifier s'il y a des images JPEG
                    if 'image/jpeg' in data:
                        image_count += 1
                        # Décoder l'image base64
                        img_data = base64.b64decode(data['image/jpeg'])
                        
                        # Nom du fichier
                        filename = f"cell_{cell_idx:02d}_output_{output_idx:02d}_image_{image_count:02d}.jpg"
                        filepath = output_dir / filename
                        
                        # Sauvegarder l'image
                        with open(filepath, 'wb') as f:
                            f.write(img_data)
                        
                        print(f"✅ Image {image_count}: {filename}")
    
    print("="*50)
    print(f"🎉 Extraction terminée ! {image_count} images sauvegardées dans {output_dir}/")
    return image_count

def create_image_index(output_dir):
    """
    Crée un fichier index.html pour visualiser toutes les images extraites
    """
    output_dir = Path(output_dir)
    images = sorted(list(output_dir.glob("*.png")) + list(output_dir.glob("*.jpg")))
    
    html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Images extraites du Notebook - Transfer Learning Segmentation</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 20px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .image-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }
        .image-item {
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding: 10px;
            background-color: #fafafa;
            transition: transform 0.3s ease;
        }
        .image-item:hover {
            transform: scale(1.02);
            border-color: #3498db;
        }
        .image-item img {
            width: 100%;
            height: auto;
            border-radius: 5px;
        }
        .image-title {
            font-weight: bold;
            color: #34495e;
            margin-top: 10px;
            text-align: center;
        }
        .stats {
            background-color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            margin-bottom: 20px;
            text-align: center;
        }
        .stats strong {
            color: #e74c3c;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🖼️ Images extraites du Notebook Transfer Learning</h1>
        
        <div class="stats">
            <strong>""" + str(len(images)) + """</strong> images extraites du notebook 
            <em>segmentation_transfer_learning.ipynb</em>
        </div>
        
        <div class="image-grid">
"""
    
    for i, img_path in enumerate(images):
        # Extraire des informations du nom de fichier
        filename = img_path.name
        parts = filename.replace('.png', '').replace('.jpg', '').split('_')
        
        if len(parts) >= 6:
            cell_num = parts[1]
            output_num = parts[3]
            img_num = parts[5]
            title = f"Cellule {cell_num} - Output {output_num} - Image {img_num}"
        else:
            title = f"Image {i+1}"
        
        html_content += f"""
            <div class="image-item">
                <img src="{filename}" alt="{title}" loading="lazy">
                <div class="image-title">{title}</div>
            </div>
        """
    
    html_content += """
        </div>
    </div>
</body>
</html>
"""
    
    # Sauvegarder le fichier HTML
    index_path = output_dir / "index.html"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"📄 Index HTML créé : {index_path}")

if __name__ == "__main__":
    # Chemins des fichiers
    notebook_path = "/workspaces/last_Tps.deep/segmentation_transfer_learning.ipynb"
    output_dir = "/workspaces/last_Tps.deep/img"
    
    # Extraire les images
    try:
        image_count = extract_images_from_notebook(notebook_path, output_dir)
        
        if image_count > 0:
            # Créer un index HTML
            create_image_index(output_dir)
            print(f"\n🌐 Ouvrez {output_dir}/index.html pour voir toutes les images")
        else:
            print("❌ Aucune image trouvée dans le notebook")
            
    except Exception as e:
        print(f"❌ Erreur lors de l'extraction : {e}")
