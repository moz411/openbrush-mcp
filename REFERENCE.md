# Guide de Référence Rapide - Commandes Open Brush MCP

## 🎨 DESSIN (Drawing)

### draw_paths
Dessine plusieurs chemins
```json
{
  "paths": "[[[0,0,0],[1,0,0]],[[0,0,1],[1,0,1]]]"
}
```

### draw_path
Dessine un chemin simple
```json
{
  "path": "[0,0,0],[1,0,0],[1,1,0]"
}
```

### draw_polygon
Dessine un polygone
```json
{
  "sides": 6,
  "radius": 2.5,
  "angle": 45
}
```

### draw_text
Dessine du texte
```json
{
  "text": "Hello World"
}
```

## 🖌️ PINCEAU (Brush)

### brush_set_type
Change le type de pinceau
```json
{
  "brush_type": "ink"
}
```
Types courants: ink, marker, light, fire, snow, stars, etc.

### brush_set_size
Définit la taille
```json
{
  "size": 0.5
}
```

### brush_move
Déplace le pinceau (absolu)
```json
{
  "x": 0,
  "y": 1,
  "z": 0
}
```

### brush_translate
Déplace le pinceau (relatif)
```json
{
  "x": 0.5,
  "y": 0,
  "z": 0
}
```

### brush_rotate
Rotation absolue
```json
{
  "x": 0,
  "y": 90,
  "z": 0
}
```

### brush_turn
Rotation relative
```json
{
  "x": 0,
  "y": 45,
  "z": 0
}
```

### brush_draw
Dessine une ligne droite
```json
{
  "length": 2.0
}
```

## 🎨 COULEUR (Color)

### color_set_rgb
Couleur en RGB (0-1)
```json
{
  "r": 1.0,
  "g": 0.0,
  "b": 0.0
}
```

### color_set_hsv
Couleur en HSV (0-1)
```json
{
  "h": 0.5,
  "s": 1.0,
  "v": 1.0
}
```

### color_set_html
Couleur HTML/CSS
```json
{
  "color": "darkblue"
}
```
ou
```json
{
  "color": "#FF5500"
}
```

## 🧊 MODÈLES 3D (Models)

### model_import
Importe un modèle local
```json
{
  "filename": "Andy.glb"
}
```

### model_web_import
Importe depuis URL
```json
{
  "url": "https://exemple.com/model.obj"
}
```

### model_icosa_import
Importe depuis Icosa Gallery
```json
{
  "model_id": "9L2Lt-sxzdp"
}
```

### model_position
Positionne un modèle
```json
{
  "index": 0,
  "x": 1.0,
  "y": 2.0,
  "z": 3.0
}
```

### model_scale
Échelle d'un modèle
```json
{
  "index": 0,
  "scale": 2.0
}
```

## 💾 SAUVEGARDE/CHARGEMENT

### save_as
Sauvegarde sous un nom
```json
{
  "filename": "ma_creation"
}
```

### load_named
Charge par nom
```json
{
  "filename": "ma_creation"
}
```

### load_user
Charge par index
```json
{
  "slot": 0
}
```
(0 = plus récent)

## 📷 CAMÉRA

### camera_move
Déplace la caméra (absolu)
```json
{
  "x": 0,
  "y": 2,
  "z": -5
}
```

### camera_rotate
Rotation caméra
```json
{
  "x": 0,
  "y": 180,
  "z": 0
}
```

## ✂️ SÉLECTION

### selection_select_all
Sélectionne tout
```json
{}
```

### selection_delete
Supprime la sélection
```json
{}
```

### selection_duplicate
Duplique la sélection
```json
{}
```

## 📑 CALQUES

### layer_create
Crée un calque
```json
{
  "name": "Mon Calque"
}
```

### layer_set
Active un calque
```json
{
  "layer": 1
}
```

### layer_show / layer_hide
Affiche/Cache un calque
```json
{
  "layer": 1
}
```

## 📐 GUIDES

### guide_add
Ajoute un guide
```json
{
  "guide_type": "cube"
}
```
Types: cube, sphere, capsule, cone, ellipsoid

### guide_position
Positionne un guide
```json
{
  "index": 0,
  "x": 0,
  "y": 1,
  "z": 0
}
```

## 🔄 SYMÉTRIE

### symmetry_mode
Mode de symétrie
```json
{
  "mode": "quad"
}
```
Modes: none, single, double, quad, radial

### symmetry_position
Position du widget
```json
{
  "x": 0,
  "y": 0,
  "z": 0
}
```

## 🔧 UTILITAIRES

### undo
Annule la dernière action
```json
{}
```

### redo
Refait la dernière action
```json
{}
```

---

## 💡 EXEMPLES DE WORKFLOWS

### Créer un carré coloré
1. `color_set_html` avec `{"color": "red"}`
2. `brush_set_type` avec `{"brush_type": "ink"}`
3. `brush_set_size` avec `{"size": 0.5}`
4. `draw_polygon` avec `{"sides": 4, "radius": 2, "angle": 45}`

### Importer et positionner un modèle
1. `model_import` avec `{"filename": "Andy.glb"}`
2. `model_position` avec `{"index": 0, "x": 0, "y": 1, "z": 2}`
3. `model_scale` avec `{"index": 0, "scale": 1.5}`

### Créer une spirale
1. `brush_move` à position de départ
2. Boucle:
   - `brush_translate` un petit pas en avant
   - `brush_turn` rotation Y de quelques degrés
   - `brush_draw` avec petite longueur

### Travailler avec des calques
1. `layer_create` avec `{"name": "Background"}`
2. Dessiner le fond
3. `layer_create` avec `{"name": "Foreground"}`
4. `layer_set` avec `{"layer": 1}`
5. Dessiner le premier plan
6. `layer_hide` avec `{"layer": 0}` pour cacher le fond

---

**Note**: Tous les angles sont en degrés. Les coordonnées suivent le système de coordonnées Unity (Y vers le haut).
