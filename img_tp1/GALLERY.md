# Galerie d'Images - TP1 Transfer Learning Segmentation

Cette galerie présente toutes les visualisations générées durant l'exécution du notebook de transfer learning pour la segmentation d'images.

## 📊 Résultats Clés

- **9 visualisations** extraites du notebook
- **3 modèles** comparés : U-Net, DeepLabV3, FCN
- **Performances remarquables** : IoU 67.4% avec U-Net après seulement 2 époques

---


## 1. Dataset Synthétique - Exemples d'images avec cercles et rectangles

*Générée par la cellule 8 du notebook*

![Dataset Synthétique - Exemples d'images avec cercles et rectangles](cell_07_output_02_image_01.png)

---

## 2. Distribution des Classes - Histogramme des pixels par classe

*Générée par la cellule 8 du notebook*

![Distribution des Classes - Histogramme des pixels par classe](cell_07_output_03_image_02.png)

---

## 3. Architectures - Comparaison U-Net vs DeepLabV3

*Générée par la cellule 10 du notebook*

![Architectures - Comparaison U-Net vs DeepLabV3](cell_09_output_00_image_03.png)

---

## 4. DataLoaders - Visualisation des batches d'entraînement

*Générée par la cellule 12 du notebook*

![DataLoaders - Visualisation des batches d'entraînement](cell_11_output_01_image_04.png)

---

## 5. Augmentation - Transformations appliquées aux données

*Générée par la cellule 12 du notebook*

![Augmentation - Transformations appliquées aux données](cell_11_output_02_image_05.png)

---

## 6. Métriques - Validation des calculs IoU et Dice

*Générée par la cellule 16 du notebook*

![Métriques - Validation des calculs IoU et Dice](cell_15_output_01_image_06.png)

---

## 7. Entraînement - Courbes d'apprentissage U-Net

*Générée par la cellule 18 du notebook*

![Entraînement - Courbes d'apprentissage U-Net](cell_17_output_02_image_07.png)

---

## 8. Prédictions - Comparaison avec vérité terrain

*Générée par la cellule 19 du notebook*

![Prédictions - Comparaison avec vérité terrain](cell_18_output_01_image_08.png)

---

## 9. Comparaison - Performance des 3 modèles

*Générée par la cellule 20 du notebook*

![Comparaison - Performance des 3 modèles](cell_19_output_01_image_09.png)

---


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
