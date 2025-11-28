# COMPRESSOR - Questionnement Algorithmique

## 1. COMPRÉHENSION DU PROBLÈME

### Q1: Quel est l'objectif principal du programme ?
**R:** Créer un compresseur de texte utilisant l'algorithme LZW (Lempel-Ziv-Welch) pour réduire la taille des données textuelles.

### Q2: Quelles sont les DONNÉES D'ENTRÉE (input) ?
**R:** 
- Texte à compresser (saisie utilisateur ou fichier)
- Données compressées à décompresser (liste de codes)
- Commandes de l'interface utilisateur

### Q3: Quelles sont les DONNÉES DE SORTIE (output) ?
**R:**
- Données compressées (liste de codes numériques)
- Texte décompressé (restitution de l'original)
- Taux de compression (pourcentage)
- Messages d'information et d'erreur

### Q4: Comment savoir si le résultat est correct ?
**R:** Vérifier que :
- Le texte décompressé est identique à l'original
- Le taux de compression est calculé correctement
- L'algorithme gère correctement les répétitions
- Les données compressées peuvent être sauvegardées/chargées

## 2. IDENTIFICATION DES DONNÉES

### Q5: Quelles variables dois-je créer ?
**R:**
- `dictionnaire` : mapping chaîne → code
- `dictionnaire_inverse` : mapping code → chaîne  
- `code_suivant` : prochain code disponible
- `texte_original` : texte à compresser
- `donnees_compressees` : résultat de la compression

### Q6: Quels types de données utiliser ?
**R:**
- **Dictionnaires** pour les mappings
- **Listes** pour les données compressées
- **Chaînes** pour le texte
- **Entiers** pour les codes
- **Flottants** pour les taux

### Q7: Ai-je besoin de structures complexes ?
**R: Oui -**
- **Dictionnaire dynamique** qui s'agrandit pendant la compression
- **Algorithme LZW** avec gestion des cas particuliers
- **Système de fichier** pour sauvegarde/chargement

## 3. DÉFINITION DES RÈGLES

### Q8: Quelles règles spécifiques implémenter ?
**R: Algorithme LZW :**
- **Initialisation** : dictionnaire avec caractères ASCII
- **Compression** : recherche des séquences les plus longues
- **Décompression** : reconstruction du dictionnaire
- **Gestion des codes** : attribution séquentielle

### Q9: Comment gérer les cas spéciaux ?
**R:**
- **Texte vide** : retourner liste vide
- **Caractères spéciaux** : inclus dans l'ASCII étendu
- **Codes manquants** : gestion d'erreur robuste
- **Dictionnaire plein** : théoriquement illimité dans cette implémentation

## 4. DÉCOMPOSITION DU PROBLÈME

### Q10: Quelles sont les étapes principales ?
**R: Pour la compression :**
1. Initialiser le dictionnaire
2. Parcourir le texte caractère par caractère
3. Chercher la plus longue séquence connue
4. Ajouter les nouveaux motifs au dictionnaire
5. Produire les codes de compression

### Q11: Quelles conditions/boucles utiliser ?
**R:**
- **Boucle POUR** : parcours du texte
- **Condition SI** : vérification présence dans dictionnaire
- **Boucle TANT QUE** : interface utilisateur principale
- **Conditions multiples** : gestion des commandes

## 5. EXEMPLES CONCRETS

### Q12: Comment fonctionne la compression sur "ABABABA" ?
**R:**
- **A** → code 65 (déjà dans dict)
- **AB** → nouveau code 256
- **B** → code 66
- **BA** → nouveau code 257
- **AB** → code 256 (déjà connu)
- **ABA** → nouveau code 258
- Résultat : [65, 66, 256, 258]

### Q13: Comment calculer le taux de compression ?
**R:**
- Taille originale : nombre de caractères × 1 octet
- Taille compressée : nombre de codes × 2 octets
- Taux = (1 - taille_compressée/taille_originale) × 100

## RÉSUMÉ DE LA DÉMARCHE

**Avant de coder, je dois :**
1. ✅ Comprendre parfaitement l'algorithme LZW
2. ✅ Planifier la structure des données
3. ✅ Prévoir l'interface utilisateur
4. ✅ Anticiper les cas limites
5. ✅ Prévoir les tests de validation

**L'algorithme LZW est efficace pour les textes avec répétitions !**