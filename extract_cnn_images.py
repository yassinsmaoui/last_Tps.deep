#!/usr/bin/env python3
"""
Script d'extraction des images du notebook CNN
Extrait toutes les visualisations générées par le notebook et les sauvegarde
"""

import os
import json
import base64
import re
from pathlib import Path

def extract_images_from_notebook(notebook_path, output_dir):
    """
    Extrait les images d'un notebook Jupyter
    """
    # Créer le dossier de sortie
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)
    
    # Charger le notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    image_count = 0
    extracted_images = []
    
    # Parcourir toutes les cellules
    for cell_idx, cell in enumerate(notebook['cells']):
        if 'outputs' in cell:
            for output_idx, output in enumerate(cell['outputs']):
                if 'data' in output:
                    # Chercher les images PNG
                    if 'image/png' in output['data']:
                        image_count += 1
                        filename = f"cell_{cell_idx:02d}_output_{output_idx:02d}_image_{image_count:02d}.png"
                        filepath = output_path / filename
                        
                        # Décoder et sauvegarder l'image
                        image_data = output['data']['image/png']
                        if isinstance(image_data, list):
                            image_data = ''.join(image_data)
                        
                        # Supprimer les caractères de nouvelle ligne
                        image_data = image_data.replace('\n', '').replace('\r', '')
                        
                        try:
                            with open(filepath, 'wb') as img_file:
                                img_file.write(base64.b64decode(image_data))
                            
                            extracted_images.append({
                                'filename': filename,
                                'cell_index': cell_idx,
                                'output_index': output_idx,
                                'path': str(filepath)
                            })
                            print(f"✅ Extracted: {filename}")
                            
                        except Exception as e:
                            print(f"❌ Error extracting {filename}: {e}")
    
    return extracted_images

def create_image_documentation(images, output_dir):
    """
    Crée une documentation des images extraites
    """
    doc_path = Path(output_dir) / "README.md"
    
    with open(doc_path, 'w', encoding='utf-8') as f:
        f.write("# CNN Implementation - Extracted Images\n\n")
        f.write("This folder contains all images extracted from the CNN notebook.\n\n")
        f.write("## Image List\n\n")
        
        for img in images:
            f.write(f"- **{img['filename']}**\n")
            f.write(f"  - Cell: {img['cell_index']}\n")
            f.write(f"  - Output: {img['output_index']}\n\n")
        
        f.write(f"\n**Total images extracted: {len(images)}**\n")
    
    print(f"📝 Documentation created: {doc_path}")

def main():
    notebook_path = "/workspaces/last_Tps.deep/tp_cnn_implementation.ipynb"
    output_dir = "/workspaces/last_Tps.deep/tp2_cnn_img"
    
    print("🖼️  CNN Image Extraction Tool")
    print("=" * 50)
    
    if not os.path.exists(notebook_path):
        print(f"❌ Notebook not found: {notebook_path}")
        return
    
    print(f"📓 Notebook: {notebook_path}")
    print(f"📁 Output directory: {output_dir}")
    print()
    
    # Extraire les images
    extracted_images = extract_images_from_notebook(notebook_path, output_dir)
    
    if extracted_images:
        print(f"\n✅ Extraction completed: {len(extracted_images)} images extracted")
        create_image_documentation(extracted_images, output_dir)
    else:
        print("\n⚠️  No images found in the notebook")

if __name__ == "__main__":
    main()
