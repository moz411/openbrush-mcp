# Serveur MCP pour Open Brush

Ce serveur MCP (Model Context Protocol) expose l'API d'Open Brush comme des outils utilisables par des LLMs via le protocole MCP.

## 📋 Prérequis

- Python 3.10 ou supérieur
- Open Brush en cours d'exécution avec l'API activée (port 40074)
- Accès à un client MCP (comme Claude Desktop)

## 🚀 Installation

1. **Cloner ou télécharger les fichiers**

2. **Installer les dépendances Python**
```bash
pip install -r requirements.txt
```

3. **Rendre le script exécutable (optionnel sur Linux/Mac)**
```bash
chmod +x openbrush_mcp_server.py
```

## ⚙️ Configuration

### Activer l'API dans Open Brush

1. Lancez Open Brush
2. Activez l'API HTTP dans les paramètres
3. L'API devrait être accessible sur `http://localhost:40074/api/v1`

### Configurer dans Claude Desktop

Ajoutez cette configuration à votre fichier de configuration MCP de Claude Desktop :

**Sur macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**Sur Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "openbrush": {
      "command": "python",
      "args": [
        "/chemin/vers/openbrush_mcp_server.py"
      ]
    }
  }
}
```

Remplacez `/chemin/vers/` par le chemin absolu vers le fichier.

## 📚 Outils Disponibles

Le serveur expose de nombreux outils organisés par catégorie :

### 🎨 Dessin (Drawing)
- `draw_paths` - Dessiner plusieurs chemins
- `draw_path` - Dessiner un chemin simple
- `draw_stroke` - Dessiner un trait avec orientation et pression
- `draw_polygon` - Dessiner un polygone
- `draw_text` - Dessiner du texte
- `draw_svg_path` - Dessiner un chemin SVG

### 🖌️ Pinceau (Brush)
- `brush_set_type` - Changer le type de pinceau
- `brush_set_size` - Définir la taille du pinceau
- `brush_add_size` - Modifier la taille du pinceau
- `brush_set_path_smoothing` - Définir le lissage
- `brush_move` - Déplacer le pinceau (position absolue)
- `brush_translate` - Déplacer le pinceau (relatif)
- `brush_rotate` - Rotation du pinceau (absolue)
- `brush_turn` - Rotation du pinceau (relative)
- `brush_draw` - Dessiner une ligne droite

### 🎨 Couleur (Color)
- `color_set_rgb` - Définir la couleur en RGB
- `color_set_hsv` - Définir la couleur en HSV
- `color_set_html` - Définir la couleur avec HTML/CSS
- `color_add_rgb` - Modifier la couleur (RGB)
- `color_add_hsv` - Modifier la couleur (HSV)

### 🧊 Modèles 3D (Models)
- `model_import` - Importer un modèle local
- `model_web_import` - Importer depuis une URL
- `model_icosa_import` - Importer depuis Icosa Gallery
- `model_select` - Sélectionner un modèle
- `model_position` - Positionner un modèle
- `model_rotation` - Rotation d'un modèle
- `model_scale` - Échelle d'un modèle
- `model_delete` - Supprimer un modèle

### 💾 Sauvegarde/Chargement (Save/Load)
- `save_overwrite` - Sauvegarder (écraser)
- `save_as` - Sauvegarder sous...
- `save_new` - Nouvelle sauvegarde
- `load_user` - Charger un sketch utilisateur
- `load_named` - Charger par nom
- `new_scene` - Nouvelle scène

### 📷 Caméra (Camera)
- `camera_move` - Déplacer la caméra (absolu)
- `camera_translate` - Déplacer la caméra (relatif)
- `camera_rotate` - Rotation caméra (absolue)
- `camera_turn` - Rotation caméra (relative)
- `spectator_move` - Déplacer la vue spectateur

### ✂️ Sélection (Selection)
- `selection_select_all` - Tout sélectionner
- `selection_invert` - Inverser la sélection
- `selection_delete` - Supprimer la sélection
- `selection_duplicate` - Dupliquer la sélection

### 📑 Calques (Layers)
- `layer_create` - Créer un calque
- `layer_set` - Définir le calque actif
- `layer_show` - Afficher un calque
- `layer_hide` - Cacher un calque

### 📐 Guides
- `guide_add` - Ajouter un guide (cube, sphere, etc.)
- `guide_position` - Positionner un guide
- `guide_scale` - Échelle d'un guide

### 🔄 Symétrie (Symmetry)
- `symmetry_mode` - Mode de symétrie
- `symmetry_position` - Position du widget de symétrie

### 🔧 Utilitaires
- `undo` - Annuler
- `redo` - Refaire
- `show_help` - Afficher l'aide API

## 💡 Exemples d'utilisation

Une fois le serveur configuré dans Claude Desktop, vous pouvez donner des instructions en langage naturel :

```
"Dessine un carré rouge de taille 2 à la position 0,0,0"
"Change le pinceau en 'ink' et définis la couleur en bleu"
"Crée un polygone à 6 côtés avec un rayon de 3"
"Importe le modèle 'Andy.glb' et positionne-le en 1,2,3"
"Sauvegarde la scène sous le nom 'ma_creation'"
```

## 🔍 Test du serveur

Pour tester manuellement le serveur :

```bash
python openbrush_mcp_server.py
```

Le serveur devrait démarrer et attendre des commandes sur stdin/stdout selon le protocole MCP.

## 🛠️ Dépannage

### L'API Open Brush n'est pas accessible
- Vérifiez qu'Open Brush est lancé
- Vérifiez que l'API HTTP est activée dans les paramètres
- Testez manuellement : `http://localhost:40074/api/v1?help`

### Le serveur MCP ne se connecte pas
- Vérifiez le chemin dans la configuration Claude Desktop
- Vérifiez que Python est dans le PATH
- Consultez les logs de Claude Desktop

### Les commandes échouent
- Vérifiez les paramètres fournis
- Consultez la documentation de l'API Open Brush
- Vérifiez les messages d'erreur retournés

## 📖 Ressources

- [Documentation Open Brush](https://docs.openbrush.app/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [API Open Brush complète](http://localhost:40074/help) (quand Open Brush est lancé)

## 🔒 Sécurité

⚠️ **Attention** : Ce serveur appelle une API locale. Assurez-vous de :
- Ne pas exposer le port 40074 sur internet
- Faire confiance aux commandes envoyées
- Sauvegarder vos créations régulièrement

## 📝 Licence

Ce serveur MCP est fourni tel quel pour faciliter l'utilisation d'Open Brush avec des LLMs.

## 🤝 Contribution

N'hésitez pas à :
- Signaler des bugs
- Proposer des améliorations
- Ajouter de nouveaux outils pour les commandes API manquantes

---

**Note** : Open Brush est un fork open-source de Tilt Brush de Google. Ce serveur MCP n'est pas affilié officiellement à Open Brush.
