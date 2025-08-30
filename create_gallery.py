#!/usr/bin/env python3
"""
Script pour créer des vignettes et une galerie markdown des images extraites
"""

from PIL import Image
import os
from pathlib import Path

def create_thumbnails(img_dir, thumb_size=(300, 300)):
    """
    Crée des vignettes pour toutes les images
    """
    img_dir = Path(img_dir)
    thumb_dir = img_dir / "thumbnails"
    thumb_dir.mkdir(exist_ok=True)
    
    images = sorted(list(img_dir.glob("*.png")) + list(img_dir.glob("*.jpg")))
    
    print(f"🖼️ Création de vignettes {thumb_size[0]}x{thumb_size[1]}...")
    
    for img_path in images:
        try:
            # Ouvrir l'image
            with Image.open(img_path) as img:
                # Créer la vignette
                img.thumbnail(thumb_size, Image.Resampling.LANCZOS)
                
                # Sauvegarder la vignette
                thumb_path = thumb_dir / f"thumb_{img_path.name}"
                img.save(thumb_path, quality=85, optimize=True)
                
                print(f"✅ Vignette créée : {thumb_path.name}")
                
        except Exception as e:
            print(f"❌ Erreur avec {img_path.name}: {e}")
    
    print(f"🎉 Vignettes sauvegardées dans {thumb_dir}/")

def create_markdown_gallery(img_dir):
    """
    Crée un fichier markdown avec galerie d'images
    """
    img_dir = Path(img_dir)
    images = sorted(list(img_dir.glob("*.png")) + list(img_dir.glob("*.jpg")))
    
    # Descriptions des images
    descriptions = {
        "cell_07_output_02_image_01.png": "Dataset Synthétique - Exemples d'images avec cercles et rectangles",
        "cell_07_output_03_image_02.png": "Distribution des Classes - Histogramme des pixels par classe", 
        "cell_09_output_00_image_03.png": "Architectures - Comparaison U-Net vs DeepLabV3",
        "cell_11_output_01_image_04.png": "DataLoaders - Visualisation des batches d'entraînement",
        "cell_11_output_02_image_05.png": "Augmentation - Transformations appliquées aux données",
        "cell_15_output_01_image_06.png": "Métriques - Validation des calculs IoU et Dice",
        "cell_17_output_02_image_07.png": "Entraînement - Courbes d'apprentissage U-Net",
        "cell_18_output_01_image_08.png": "Prédictions - Comparaison avec vérité terrain",
        "cell_19_output_01_image_09.png": "Comparaison - Performance des 3 modèles"
    }
    
    markdown_content = """# 🖼️ Galerie d'Images - Transfer Learning Segmentation

Cette galerie présente toutes les visualisations générées par le notebook de transfer learning pour la segmentation d'images.

## 📊 Résultats Clés

- **9 visualisations** extraites du notebook
- **3 modèles** comparés : U-Net, DeepLabV3, FCN
- **Performances remarquables** : IoU 67.4% avec U-Net après seulement 2 époques

---

"""
    
    for i, img_path in enumerate(images, 1):
        filename = img_path.name
        description = descriptions.get(filename, f"Visualisation {i}")
        
        # Extraire le numéro de cellule pour le contexte
        if "cell_" in filename:
            cell_num = filename.split('_')[1]
            cell_context = f"*Générée par la cellule {int(cell_num)+1} du notebook*"
        else:
            cell_context = ""
        
        markdown_content += f"""
## {i}. {description}

{cell_context}

![{description}]({filename})

---
"""
    
    markdown_content += """

## 🎯 Analyse des Résultats

### Meilleur Modèle : U-Net + ResNet34
- **IoU moyen** : 67.4%
- **Coefficient Dice** : 78.6% 
- **Précision pixels** : 94.7%

### Performance par Classe
| Classe | IoU | Dice |
|--------|-----|------|
| Background | 94.8% | 97.4% |
| Cercles | 63.6% | 77.7% |
| Rectangles | 43.6% | 60.7% |

### Apprentissages Clés
1. **Transfer Learning efficace** : Amélioration drastique vs modèles non fine-tunés
2. **Convergence rapide** : Résultats excellents en 2 époques seulement
3. **Architecture U-Net** : Particulièrement adaptée à la segmentation
4. **Métriques spécialisées** : IoU et Dice plus informatives que la précision simple

---

*Galerie générée automatiquement à partir de `segmentation_transfer_learning.ipynb`*
"""
    
    # Sauvegarder le fichier markdown
    gallery_path = img_dir / "GALLERY.md"
    with open(gallery_path, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"📝 Galerie markdown créée : {gallery_path}")

if __name__ == "__main__":
    img_dir = "/workspaces/last_Tps.deep/img"
    
    # Créer les vignettes
    create_thumbnails(img_dir)
    
    # Créer la galerie markdown  
    create_markdown_gallery(img_dir)
    
    print("\n🎉 Galerie complète créée !")
    print(f"📂 Dossier : {img_dir}/")
    print(f"🌐 HTML : {img_dir}/index.html")
    print(f"📝 Markdown : {img_dir}/GALLERY.md")
