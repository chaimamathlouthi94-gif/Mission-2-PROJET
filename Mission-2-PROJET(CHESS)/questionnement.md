# CHESS - Questionnement Algorithmique

## 1. COMPRÉHENSION DU PROBLÈME

### Q1: Quel est l'objectif principal du programme ?
**R:** Créer un jeu d'échecs fonctionnel où deux joueurs peuvent jouer avec les règles classiques des échecs.

### Q2: Quelles sont les DONNÉES D'ENTRÉE (input) ?
**R:** 
- Les coups des joueurs en notation échecs (ex: "e2 e4")
- Les commandes spéciales ("score", "coups e2", "quit", "reset")

### Q3: Quelles sont les DONNÉES DE SORTIE (output) ?
**R:**
- L'affichage du plateau après chaque coup
- La liste des coups légaux possibles
- Le score des joueurs (basé sur les pièces capturées)
- Les messages de confirmation ou d'erreur

### Q4: Comment savoir si le résultat est correct ?
**R:** Vérifier que :
- Les pièces se déplacent selon leurs règles officielles
- Les coups illégaux sont rejetés avec un message d'erreur
- Le score est correctement calculé après chaque prise
- L'alternance des joueurs fonctionne correctement

## 2. IDENTIFICATION DES DONNÉES

### Q5: Quelles variables dois-je créer ?
**R:**
- `plateau` : tableau 8x8 pour représenter l'échiquier
- `joueur_actuel` : string pour savoir à qui c'est le tour
- `score_blanc`, `score_noir` : entiers pour le score
- `partie_terminee` : booléen pour l'état du jeu
- `historique_coups` : liste pour sauvegarder les coups

### Q6: Quels types de données utiliser ?
**R:**
- **Tableau 2D 8x8** de caractères pour le plateau
- **Chaînes de caractères** pour la notation des positions
- **Entiers** pour les scores
- **Booléen** pour l'état de la partie
- **Liste** pour l'historique des coups

### Q7: Ai-je besoin de structures complexes ?
**R: Oui -**
- **Dictionnaire** pour les valeurs des pièces
- **Fonctions de conversion** entre notation échecs et indices
- **Algorithmes spécifiques** par type de pièce pour les déplacements

## 3. DÉFINITION DES RÈGLES

### Q8: Quelles règles spécifiques implémenter ?
**R: Règles de base pour commencer :**
- **Pions** : avance d'1 case, 2 cases au premier coup, prise en diagonale
- **Tours** : déplacement horizontal et vertical
- **Cavaliers** : mouvement en "L"
- **Fous** : déplacement diagonal
- **Dame** : combine tour + fou
- **Roi** : déplacement d'1 case dans toutes directions

### Q9: Comment gérer les cas spéciaux ?
**R:**
- **Vérification propriétaire** : un joueur ne peut déplacer que ses pièces
- **Cases occupées** : impossible de traverser les pièces
- **Prise** : possible seulement sur pièce adverse
- **Alternance** : changement de joueur après chaque coup valide

## 4. DÉCOMPOSITION DU PROBLÈME

### Q10: Quelles sont les étapes principales ?
**R:**
1. **Initialisation** : créer le plateau, placer les pièces
2. **Affichage** : montrer le plateau et les informations
3. **Saisie** : récupérer la commande du joueur
4. **Validation** : vérifier si le coup est légal
5. **Exécution** : déplacer la pièce si valide
6. **Mise à jour** : scores, historique, changement de joueur
7. **Boucle** : répéter jusqu'à fin de partie

### Q11: Quelles conditions/boucles utiliser ?
**R:**
- **Boucle TANT QUE** : pour la partie principale
- **Conditions SI/SINON** : pour valider les coups et commandes
- **Boucle POUR** : pour parcourir le plateau et générer les coups

## 5. EXEMPLES CONCRETS

### Q12: Comment représenter un coup simple ?
**R: Exemple "e2 e4" :**
- **Position départ** : ligne 6, colonne 4 (e2)
- **Position arrivée** : ligne 4, colonne 4 (e4)
- **Vérification** : 
  - La case e2 contient-elle un pion blanc ?
  - Le déplacement e2→e4 est-il autorisé pour un pion ?
  - La case e4 est-elle libre ?

### Q13: Comment générer les coups légaux pour un pion en e2 ?
**R:**
1. Vérifier case devant (e3) - si libre → coup légal
2. Vérifier case 2 devant (e4) - si premier mouvement → coup légal  
3. Vérifier cases diagonales (d3, f3) - si pièce adverse → coup légal

## RÉSUMÉ DE LA DÉMARCHE

**Avant de coder, je dois :**
1. ✅ Comprendre exactement ce que le programme doit faire
2. ✅ Identifier toutes les données nécessaires  
3. ✅ Connaître les règles à implémenter
4. ✅ Décomposer le problème en petites étapes
5. ✅ Prévoir des exemples de test

**Cette réflexion préalable me permettra de coder plus efficacement !**