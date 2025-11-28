# COMPRESSOR - Rapport de Projet

## 1. 📋 Présentation du Projet

### **Objectif Principal**
Implémenter l'algorithme de compression LZW (Lempel-Ziv-Welch) pour compresser et décompresser du texte avec analyse des performances.

### **Contexte**
Projet réalisé dans le cadre du cours B1 Algorithmique 2025/2026.

## 2. 🏗️ Architecture Technique

### **2.1 Algorithme LZW**
L'algorithme LZW fonctionne en construisant dynamiquement un dictionnaire des séquences rencontrées dans le texte.

### **2.2 Structure des Données**
```python
# Dictionnaire initial : caractères ASCII
dictionnaire = {'A': 65, 'B': 66, ..., 'a': 97, ...}
dictionnaire_inverse = {65: 'A', 66: 'B', ...}