# Résultats du TP Transfer Learning - Segmentation d'Images

## 🎯 Objectif
Implémentation d'un pipeline complet de segmentation d'images utilisant le transfer learning avec des architectures état-de-l'art.

## 📊 Résultats Principaux

### Performance des Modèles
| Modèle | IoU | Dice | Précision Pixel | Status |
|--------|-----|------|-----------------|--------|
| **U-Net + ResNet34** | **65.9%** | **77.8%** | **93.9%** | ✅ Entraîné |
| FCN + ResNet50 | 16.1% | 22.8% | 45.2% | ⚠️ Pré-entraîné |
| DeepLabV3 + ResNet50 | 2.7% | 4.9% | 8.0% | ⚠️ Pré-entraîné |

### Analyse par Classe (U-Net entraîné)
| Classe | IoU | Dice | Observations |
|--------|-----|------|--------------|
| Background | 94.0% | 96.9% | Excellente performance |
| Cercles | 53.2% | 69.5% | Défis sur les contours courbes |
| Rectangles | 50.5% | 67.1% | Confusion partielle avec background |

## 🔧 Configuration Technique

### Dataset
- **Taille** : 500 images synthétiques (128x128)
- **Classes** : 3 (Background, Cercles, Rectangles)
- **Split** : 60% train / 20% val / 20% test
- **Génération** : PIL avec formes géométriques colorées

### Entraînement
- **Époque** : 2 (démonstration rapide)
- **Optimiseur** : AdamW (lr=1e-4)
- **Loss** : Combined CrossEntropy + Dice
- **Amélioration** : IoU 28.5% → 65.9% entre époque 1 et 2

## 🎓 Apprentissages Clés

1. **Transfer Learning Efficace** : L'utilisation de modèles pré-entraînés améliore drastiquement les performances
2. **Importance du Fine-tuning** : Différence flagrante entre modèles fine-tunés vs pré-entraînés
3. **Métriques Spécialisées** : IoU et Dice plus informatives que la précision pixel simple
4. **Architecture U-Net** : Particulièrement adaptée à notre tâche de segmentation

## 🚀 Implémentation Complète

✅ **Génération de données synthétiques**  
✅ **Pipeline d'entraînement modulaire**  
✅ **Métriques de segmentation (IoU, Dice)**  
✅ **Visualisation des prédictions**  
✅ **Comparaison multi-modèles**  
✅ **Analyse des erreurs par classe**  
✅ **Sauvegarde/chargement de modèles**  

## 📈 Potentiel d'Amélioration

- **Dataset plus complexe** : Images réelles, plus de classes
- **Augmentation avancée** : Transformations géométriques/photométriques
- **Hyperparamètre tuning** : Learning rate scheduling, architecture search
- **Ensembling** : Combinaison de plusieurs modèles
- **Post-processing** : CRF, morphologie mathématique

## 💡 Applications Réelles

Ce pipeline peut être adapté pour :
- **Imagerie médicale** : Segmentation d'organes, détection de tumeurs
- **Vision industrielle** : Contrôle qualité, détection de défauts
- **Agriculture** : Analyse de cultures, détection de maladies
- **Automobile** : Segmentation de routes, détection d'obstacles

---
*TP réalisé avec PyTorch 2.8.0, segmentation-models-pytorch, et un environnement Jupyter optimisé*
