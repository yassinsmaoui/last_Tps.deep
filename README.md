# 🧠 TP Transfer Learning - Segmentation d'Images

## 📝 Description
Implémentation complète d'un pipeline de **Transfer Learning** pour la **segmentation d'images** utilisant PyTorch. Ce projet explore différentes architectures pré-entraînées (U-Net, DeepLabV3, FCN) et compare leurs performances sur un dataset synthétique.

## 🎯 Objectifs du TP
- ✅ **Comprendre** les concepts du Transfer Learning en segmentation
- ✅ **Implémenter** des modèles pré-entraînés (U-Net, DeepLabV3, FCN)
- ✅ **Analyser** les performances avec des métriques appropriées (IoU, Dice)
- ✅ **Visualiser** les résultats et comparer les approches
- ✅ **Optimiser** l'entraînement avec différentes stratégies

## 📊 Résultats Principaux

### Performance des Modèles
| Modèle | IoU | Dice | Précision Pixel | Status |
|--------|-----|------|-----------------|--------|
| **U-Net + ResNet34** | **68.4%** | **79.5%** | **94.7%** | ✅ Entraîné |
| FCN + ResNet50 | 16.1% | 22.8% | 45.2% | ⚠️ Pré-entraîné |
| DeepLabV3 + ResNet50 | 2.7% | 4.9% | 8.0% | ⚠️ Pré-entraîné |

### Dataset Synthétique
- **500 images** de 256×256 pixels
- **3 classes** : Background (noir), Cercles (rouge), Rectangles (vert)
- **Split** : 60% train / 20% validation / 20% test

## 📁 Structure du Repository

```
├── segmentation_transfer_learning.ipynb    # 📓 Notebook principal complet
├── resultats_tp.md                        # 📊 Résumé détaillé des résultats
├── rapport_corrections.md                 # 🔧 Documentation des corrections
├── demo_programmatique.ipynb              # 🎮 Notebook de démonstration
├── TP Transfer Learning la segmentation d'images.pdf  # 📚 Document de référence
├── .gitignore                            # 🚫 Exclusions Git
└── README.md                             # 📖 Ce fichier
```

## 🚀 Utilisation

### 1. Cloner le repository
```bash
git clone https://github.com/yassinsmaoui/last_Tps.deep.git
cd last_Tps.deep
```

### 2. Installation des dépendances
```bash
pip install torch torchvision segmentation-models-pytorch
pip install matplotlib numpy pillow scikit-learn
```

### 3. Lancer le notebook
```bash
jupyter notebook segmentation_transfer_learning.ipynb
```

## 🔧 Fonctionnalités Implémentées

### 🎨 Génération de Données
- **Générateur synthétique** avec PIL
- **Formes géométriques** colorées (cercles, rectangles)
- **Augmentation** de données avec PyTorch transforms

### 🧠 Modèles de Segmentation
- **U-Net** + ResNet34 backbone
- **DeepLabV3** + ResNet50 backbone  
- **FCN** + ResNet50 backbone
- **Transfer Learning** avec modèles pré-entraînés ImageNet

### 📏 Métriques Spécialisées
- **IoU** (Intersection over Union)
- **Coefficient de Dice** (F1-score pour segmentation)
- **Précision pixel** par classe
- **Matrice de confusion** détaillée

### 📊 Visualisation et Analyse
- **Comparaison** prédictions vs vérité terrain
- **Analyse des erreurs** par classe
- **Graphiques** d'évolution des métriques
- **Comparaison multi-modèles**

## 🎓 Concepts Clés Abordés

### Transfer Learning
- Utilisation de modèles pré-entraînés sur ImageNet
- Fine-tuning des dernières couches
- Amélioration significative des performances

### Architectures de Segmentation
- **U-Net** : Skip connections, architecture symétrique
- **DeepLabV3** : ASPP, convolutions dilatées
- **FCN** : Fully Convolutional Networks

### Métriques de Segmentation
- **IoU** : Mesure de superposition des régions
- **Dice** : Plus sensible aux petites régions
- **Analyse par classe** : Performance détaillée

## 🌟 Points Forts du Projet

- 🔄 **Pipeline complet** : Génération → Entraînement → Évaluation
- 📊 **Métriques appropriées** : IoU, Dice, précision pixel
- 🎯 **Transfer Learning efficace** : +50% d'amélioration vs modèles non fine-tunés
- 📈 **Visualisations claires** : Prédictions, erreurs, comparaisons
- 📖 **Documentation complète** : Théorie + implémentation

## 💡 Applications Réelles

Ce pipeline peut être adapté pour :
- **🏥 Imagerie médicale** : Segmentation d'organes, détection de tumeurs
- **🏭 Vision industrielle** : Contrôle qualité, détection de défauts
- **🌾 Agriculture** : Analyse de cultures, détection de maladies
- **🚗 Automobile** : Segmentation de routes, détection d'obstacles

## 🚀 Améliorations Possibles

- **Dataset plus complexe** : Images réelles, plus de classes
- **Augmentation avancée** : Albumentations, augmentations géométriques
- **Hyperparamètre tuning** : Optimisation automatique
- **Ensembling** : Combinaison de plusieurs modèles
- **Post-processing** : CRF, morphologie mathématique

## 📚 Technologies Utilisées

- **PyTorch 2.8.0** : Framework de deep learning
- **Torchvision** : Modèles pré-entraînés
- **Segmentation Models PyTorch** : Architectures spécialisées
- **PIL/Pillow** : Génération d'images synthétiques
- **Matplotlib** : Visualisations
- **NumPy** : Calculs numériques
- **Scikit-learn** : Métriques additionnelles

## 👨‍💻 Auteur

**Yassin Smaoui** - [GitHub Profile](https://github.com/yassinsmaoui)

## 📄 Licence

Ce projet est réalisé dans le cadre d'un TP académique sur le Transfer Learning en segmentation d'images.

---

*⭐ N'hésitez pas à donner une étoile si ce projet vous a été utile !*