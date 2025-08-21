# Images extraites du Notebook Transfer Learning

Ce dossier contient toutes les images/graphiques générés par le notebook `segmentation_transfer_learning.ipynb`.

## 📋 Liste des Images

### 🎯 **Image 1** : `cell_07_output_02_image_01.png`
- **Source** : Cellule 8 - Génération du dataset synthétique
- **Description** : Exemples d'images synthétiques générées (cercles et rectangles colorés)
- **Contenu** : Visualisation des données d'entraînement avec masques de segmentation

### 🎯 **Image 2** : `cell_07_output_03_image_02.png`  
- **Source** : Cellule 8 - Analyse du dataset
- **Description** : Distribution des classes dans le dataset synthétique
- **Contenu** : Histogramme montrant la répartition des pixels par classe

### 🎯 **Image 3** : `cell_09_output_00_image_03.png`
- **Source** : Cellule 10 - Architecture des modèles
- **Description** : Comparaison visuelle des architectures U-Net et DeepLabV3
- **Contenu** : Schémas des architectures de segmentation

### 🎯 **Image 4** : `cell_11_output_01_image_04.png`
- **Source** : Cellule 12 - Test des DataLoaders  
- **Description** : Exemples de batches d'images et masques
- **Contenu** : Visualisation des données préparées pour l'entraînement

### 🎯 **Image 5** : `cell_11_output_02_image_05.png`
- **Source** : Cellule 12 - Augmentation des données
- **Description** : Effets des transformations appliquées aux images
- **Contenu** : Images avant/après augmentation de données

### 🎯 **Image 6** : `cell_15_output_01_image_06.png`
- **Source** : Cellule 16 - Test des métriques
- **Description** : Visualisation des métriques IoU et Dice
- **Contenu** : Graphiques de validation des calculs de métriques

### 🎯 **Image 7** : `cell_17_output_02_image_07.png`
- **Source** : Cellule 18 - Résultats d'entraînement
- **Description** : Courbes d'apprentissage du modèle U-Net
- **Contenu** : Évolution de la perte, IoU et Dice pendant l'entraînement

### 🎯 **Image 8** : `cell_18_output_01_image_08.png`
- **Source** : Cellule 19 - Prédictions du modèle
- **Description** : Comparaison prédictions vs vérité terrain
- **Contenu** : Images originales, masques réels, prédictions et erreurs

### 🎯 **Image 9** : `cell_19_output_01_image_09.png`
- **Source** : Cellule 20 - Comparaison des modèles
- **Description** : Performance comparative des 3 architectures
- **Contenu** : Histogrammes des métriques IoU, Dice et précision par modèle

## 🔧 Utilisation

### Visualisation rapide
Ouvrez le fichier `index.html` dans un navigateur pour voir toutes les images organisées.

### Images individuelles
Chaque image est nommée selon le format :
```
cell_XX_output_YY_image_ZZ.png
```
- `XX` : Numéro de la cellule (décompte à partir de 0)
- `YY` : Numéro de l'output dans la cellule  
- `ZZ` : Numéro de l'image dans l'output

## 📊 Résumé des Résultats Visualisés

### Performances des Modèles (Image 9)
| Modèle | IoU | Dice | Précision |
|--------|-----|------|-----------|
| **U-Net + ResNet34** | **67.4%** | **78.6%** | **94.7%** |
| FCN + ResNet50 | 16.1% | 22.8% | 45.2% |
| DeepLabV3 + ResNet50 | 2.7% | 4.9% | 8.0% |

### Progression d'Entraînement (Image 7)
- **Époque 1** : IoU 44.0% → **Époque 2** : IoU 68.4%
- Amélioration spectaculaire en seulement 2 époques
- Convergence rapide grâce au transfer learning

## 🎓 Applications Pédagogiques

Ces images illustrent parfaitement :
1. **Pipeline complet** de segmentation par transfer learning
2. **Métriques spécialisées** (IoU, Dice) vs précision simple
3. **Importance du fine-tuning** (différence énorme entre modèles)
4. **Qualité des prédictions** et analyse des erreurs
5. **Comparaison objective** des architectures

---
*Images générées automatiquement le $(date) à partir du notebook segmentation_transfer_learning.ipynb*
