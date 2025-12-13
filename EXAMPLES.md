# Exemples de Scripts Open Brush

Ce fichier contient des exemples de scripts que vous pouvez demander à Claude d'exécuter via le serveur MCP.

## 🌈 Exemple 1 : Arc-en-ciel

"Crée un arc-en-ciel avec 7 arcs de couleurs différentes"

Étapes :
1. Définir le pinceau en type "ink" avec taille 0.3
2. Pour chaque couleur (rouge, orange, jaune, vert, bleu, indigo, violet) :
   - Changer la couleur
   - Dessiner un arc (polygone avec nombreux côtés)
   - Déplacer le pinceau légèrement

## 🏗️ Exemple 2 : Grille 3D

"Crée une grille 3D de 5x5x5 cubes"

Étapes :
1. Ajouter un guide cube à l'origine
2. Pour x de 0 à 4 :
   - Pour y de 0 à 4 :
     - Pour z de 0 à 4 :
       - Dupliquer le guide
       - Positionner à (x*2, y*2, z*2)

## ✍️ Exemple 3 : Texte avec effet néon

"Écris 'HELLO' avec un effet néon lumineux"

Étapes :
1. Changer le pinceau en "light" ou "neon"
2. Définir la couleur en cyan vif
3. Définir une taille de 1.0
4. Dessiner le texte "HELLO"

## 🌸 Exemple 4 : Fleur géométrique

"Crée une fleur géométrique avec 12 pétales"

Étapes :
1. Définir la couleur en rose
2. Positionner le pinceau au centre (0, 0, 0)
3. Pour i de 0 à 11 :
   - Dessiner un polygone à 4 côtés (losange)
   - Tourner le pinceau de 30 degrés autour de Y
   - Répéter

## 🌀 Exemple 5 : Spirale ascendante

"Dessine une spirale qui monte vers le ciel"

Étapes :
1. Définir le pinceau en "ink", couleur bleue
2. Position de départ : (0, 0, 0)
3. Pour 100 itérations :
   - Activer le dessin forcé
   - Translater (0.1, 0.05, 0) - avance et monte
   - Tourner de 10 degrés autour de Y
   - Dessiner une petite ligne

## 🎯 Exemple 6 : Cible concentrique

"Crée une cible avec cercles concentriques de couleurs alternées"

Étapes :
1. Pour rayon de 5 à 1 (décroissant de 1) :
   - Alterner couleur entre rouge et blanc
   - Dessiner un polygone à 32 côtés (cercle)
   - Changer la taille du pinceau

## 🏛️ Exemple 7 : Temple avec colonnes

"Construis un temple grec avec 6 colonnes"

Étapes :
1. Créer le sol : rectangle plat
2. Pour chaque colonne (6 colonnes espacées) :
   - Importer un guide capsule
   - Positionner verticalement
   - Étirer en hauteur (scale)
3. Créer le toit : grand rectangle au-dessus

## 🎨 Exemple 8 : Palette de couleurs

"Crée une palette montrant toutes les couleurs primaires et secondaires"

Étapes :
1. Définir les couleurs : rouge, jaune, bleu, vert, orange, violet
2. Pour chaque couleur, à des positions espacées :
   - Changer la couleur
   - Dessiner un carré (polygone à 4 côtés)

## 🌳 Exemple 9 : Arbre fractal simple

"Dessine un arbre fractal à 3 niveaux"

Étapes :
1. Fonction récursive de branche :
   - Dessiner une ligne (tronc)
   - Si niveau > 0 :
     - Tourner de +30 degrés
     - Appeler récursivement avec niveau-1
     - Tourner de -60 degrés
     - Appeler récursivement avec niveau-1
     - Tourner de +30 degrés (remettre)

## 🎪 Exemple 10 : Scène de système solaire

"Crée un mini système solaire avec le Soleil et 3 planètes"

Étapes :
1. Soleil :
   - Couleur jaune, pinceau "fire"
   - Grande sphère au centre (guide sphere)
2. Pour chaque planète (3 planètes) :
   - Couleur différente (bleu, rouge, vert)
   - Guide sphere de taille décroissante
   - Positionner en orbite autour du soleil
   - Distance croissante

## 📦 Exemple 11 : Boîte avec décoration

"Dessine une boîte cadeau avec un ruban"

Étapes :
1. Créer un guide cube pour la boîte
2. Couleur rouge pour le ruban
3. Dessiner deux lignes qui se croisent sur le dessus
4. Ajouter un nœud (deux boucles) au centre

## 🌊 Exemple 12 : Vagues océaniques

"Crée des vagues stylisées"

Étapes :
1. Pinceau "ink" bleu clair
2. Pour 5 vagues :
   - Dessiner une courbe sinusoïdale (chemin SVG ou points)
   - Position Y légèrement différente
   - Transparence variable

## 💫 Exemple 13 : Constellation d'étoiles

"Dessine une constellation avec 10 étoiles connectées"

Étapes :
1. Créer 10 points aléatoires dans l'espace
2. Dessiner des petites étoiles (polygones à 5 branches) à chaque point
3. Connecter certaines étoiles avec des lignes fines

## 🏰 Exemple 14 : Château simple

"Construis un château avec 4 tours d'angle"

Étapes :
1. Murs : 4 guides cube pour les murs
2. Tours : 4 guides cylinder aux coins
3. Créneaux : petits cubes sur le haut des murs
4. Porte : guide capsule horizontal au centre

## 🎼 Exemple 15 : Portée musicale avec notes

"Dessine une portée musicale avec quelques notes"

Étapes :
1. Dessiner 5 lignes horizontales parallèles (portée)
2. Ajouter une clé de sol (SVG path ou dessin manuel)
3. Placer des notes (ellipses) sur la portée

---

## 💡 Conseils pour créer vos propres scripts

1. **Planifiez d'abord** : Décomposez votre idée en étapes simples
2. **Utilisez les coordonnées** : Comprenez le système (Y vers le haut)
3. **Testez progressivement** : Créez étape par étape
4. **Sauvegardez régulièrement** : Utilisez `save_as` souvent
5. **Expérimentez** : Essayez différents pinceaux et couleurs
6. **Combinez les guides** : Mélangez cubes, sphères, capsules
7. **Utilisez la symétrie** : Pour des motifs répétitifs
8. **Pensez en 3D** : N'oubliez pas l'axe Z !

---

## 🎯 Demandes exemple à faire à Claude

Voici comment formuler vos demandes :

### Simple
"Dessine un cube rouge de taille 2"

### Moyen
"Crée une pyramide en empilant 4 niveaux de cubes, chaque niveau plus petit"

### Avancé
"Génère un mandala symétrique avec 8 axes de symétrie, utilisant des polygones de différentes tailles et couleurs alternées"

### Très avancé
"Crée une scène de ville miniature avec 10 bâtiments de hauteurs variables, des routes entre eux, et quelques arbres (guides capsule verts)"

---

**Astuce** : Plus vous êtes précis dans votre demande, meilleur sera le résultat !
