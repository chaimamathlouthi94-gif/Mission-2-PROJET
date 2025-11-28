# CHESS - Rapport de Projet

## 1. 📋 Présentation du Projet

### **Objectif Principal**
Développer un jeu d'échecs fonctionnel en Python permettant à deux joueurs de s'affronter avec les règles classiques.

### **Contexte**
Projet réalisé dans le cadre du cours B1 Algorithmique 2025/2026.

## 2. 🏗️ Architecture Technique

### **2.1 Structure des Données**
```python
# Plateau représenté par un tableau 8x8
plateau = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  # Noirs
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    # ... lignes vides ...
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Blancs
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]