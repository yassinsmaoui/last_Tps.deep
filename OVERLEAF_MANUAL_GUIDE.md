# Guide d'Utilisation Overleaf - Upload Manuel

## 📄 Rapport IMRAD - Transfer Learning pour la Segmentation d'Images

Ce guide vous explique comment utiliser le rapport LaTeX dans Overleaf avec upload manuel des fichiers.

## 📁 Fichiers à Uploader dans Overleaf

### Fichiers Obligatoires
1. **`rapport_tp1_imrad.tex`** - Document principal LaTeX
2. **`references.bib`** - Bibliographie BibTeX
3. **Dossier `img_tp1/`** - Toutes les images (9 fichiers PNG)

### Structure dans Overleaf
```
Votre Projet Overleaf/
├── rapport_tp1_imrad.tex
├── references.bib
└── img_tp1/
    ├── cell_07_output_02_image_01.png
    ├── cell_07_output_03_image_02.png
    ├── cell_09_output_00_image_03.png
    ├── cell_15_output_01_image_06.png
    ├── cell_17_output_02_image_07.png
    ├── cell_18_output_01_image_08.png
    └── ... (autres images)
```

## 🚀 Instructions d'Upload Étape par Étape

### Étape 1 : Créer le Projet
1. Aller sur [www.overleaf.com](https://www.overleaf.com)
2. Cliquer "New Project" → "Blank Project"
3. Nommer le projet : "TP1 - Transfer Learning Segmentation"

### Étape 2 : Uploader le Document Principal
1. Supprimer le fichier `main.tex` par défaut
2. Cliquer "Upload" → Sélectionner `rapport_tp1_imrad.tex`
3. Le fichier sera automatiquement défini comme document principal

### Étape 3 : Uploader la Bibliographie
1. Cliquer "Upload" → Sélectionner `references.bib`

### Étape 4 : Créer le Dossier Images
1. Cliquer "New Folder"
2. Nommer le dossier : `img_tp1`

### Étape 5 : Uploader les Images
1. Entrer dans le dossier `img_tp1`
2. Cliquer "Upload" → Sélectionner TOUTES les images PNG du dossier
3. Vérifier que les 9 images sont présentes :
   - `cell_07_output_02_image_01.png`
   - `cell_07_output_03_image_02.png`
   - `cell_09_output_00_image_03.png`
   - `cell_15_output_01_image_06.png`
   - `cell_17_output_02_image_07.png`
   - `cell_18_output_01_image_08.png`
   - Et les autres fichiers PNG

### Étape 6 : Compiler
1. Cliquer "Recompile"
2. Le PDF sera généré avec toutes les images

## 🖼️ Images Intégrées

Le rapport contient 6 figures principales :

| Figure | Fichier | Description |
|--------|---------|-------------|
| Figure 1 | `cell_07_output_02_image_01.png` | Exemples du dataset synthétique |
| Figure 2 | `cell_07_output_03_image_02.png` | Distribution des classes |
| Figure 3 | `cell_09_output_00_image_03.png` | Architectures des modèles |
| Figure 4 | `cell_15_output_01_image_06.png` | Courbes d'entraînement |
| Figure 5 | `cell_17_output_02_image_07.png` | Visualisation des prédictions |
| Figure 6 | `cell_18_output_01_image_08.png` | Comparaison des modèles |

## ✅ Avantages de l'Upload Manuel

✅ **Rapidité** : Compilation instantanée sans dépendance réseau  
✅ **Fiabilité** : Pas de risque de liens brisés  
✅ **Contrôle** : Gestion complète des versions d'images  
✅ **Collaboration** : Facile à partager avec des collaborateurs  

## 🔧 Personnalisation

### Modifier les Métadonnées
Dans l'en-tête du document :
```latex
\title{\textbf{Votre Titre} \\
\large Sous-titre}

\author{Votre Nom \\
\small \href{mailto:votre.email@example.com}{votre.email@example.com}}
```

### Ajouter des Images
Pour ajouter une nouvelle image :
1. Uploader l'image dans le dossier `img_tp1/`
2. L'inclure dans le LaTeX :
```latex
\begin{figure}[H]
    \centering
    \includegraphics[width=0.8\textwidth]{img_tp1/nom_de_votre_image.png}
    \caption{Description de l'image}
    \label{fig:nom_reference}
\end{figure}
```

## 📝 Configuration de Compilation

### Paramètres Recommandés
- **Compilateur** : pdfLaTeX
- **Bibliographie** : BibTeX
- **Packages** : Tous inclus automatiquement

### Ordre de Compilation
Overleaf gère automatiquement :
1. pdfLaTeX (première passe)
2. BibTeX (bibliographie)
3. pdfLaTeX (références croisées)
4. pdfLaTeX (finalisation)

## 🚨 Résolution de Problèmes

### Images ne s'affichent pas
- ✅ Vérifier que le dossier `img_tp1/` existe
- ✅ Vérifier les noms des fichiers (sensible à la casse)
- ✅ S'assurer que toutes les images sont uploadées

### Erreurs de Compilation
- ✅ Vérifier que `references.bib` est présent
- ✅ Attendre la fin de l'upload avant compilation
- ✅ Consulter les logs pour détails d'erreurs

### Bibliographie manquante
- ✅ S'assurer que `references.bib` est dans le dossier racine
- ✅ Vérifier les citations avec `\cite{}`

## 📊 Taille des Fichiers

| Fichier | Taille Approximative |
|---------|---------------------|
| `rapport_tp1_imrad.tex` | ~30 KB |
| `references.bib` | ~2 KB |
| Dossier `img_tp1/` | ~2-3 MB total |
| **Total** | **~3 MB** |

## 🎯 Checklist de Vérification

Avant compilation finale :

- [ ] Document principal `rapport_tp1_imrad.tex` uploadé
- [ ] Fichier `references.bib` uploadé
- [ ] Dossier `img_tp1/` créé
- [ ] Toutes les 9 images PNG uploadées
- [ ] Noms des fichiers respectent la casse exacte
- [ ] Première compilation réussie

## 📞 Support

Pour toute question :
1. Consulter la documentation Overleaf
2. Vérifier les logs de compilation
3. Contacter l'auteur via les informations dans le document

---

**Bon usage du rapport LaTeX avec Overleaf ! 🎓📄**

## 🔄 Mise à Jour des Images

Si vous modifiez les images :
1. Supprimer l'ancienne image dans Overleaf
2. Uploader la nouvelle version avec le même nom
3. Recompiler le document

Le rapport sera automatiquement mis à jour ! ✨
