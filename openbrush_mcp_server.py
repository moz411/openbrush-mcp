#!/usr/bin/env python3
"""
Serveur MCP pour l'API Open Brush
Expose toutes les commandes Open Brush comme des outils MCP
"""

import asyncio
import httpx
from typing import Any, Dict, List, Optional
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Configuration
API_BASE_URL = "http://localhost:40074/api/v1"

# Création du serveur MCP
app = Server("openbrush-mcp")


async def call_openbrush_api(params: Dict[str, Any]) -> str:
    """
    Appelle l'API Open Brush avec les paramètres fournis
    """
    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(API_BASE_URL, params=params)
            response.raise_for_status()
            return response.text
    except httpx.HTTPError as e:
        return f"Erreur HTTP: {str(e)}"
    except Exception as e:
        return f"Erreur: {str(e)}"


@app.list_tools()
async def list_tools() -> List[Tool]:
    """
    Liste tous les outils disponibles basés sur l'API Open Brush
    """
    return [
        # === DRAWING COMMANDS ===
        Tool(
            name="draw_paths",
            description="Dessine une série de chemins à la position actuelle du pinceau",
            inputSchema={
                "type": "object",
                "properties": {
                    "paths": {
                        "type": "string",
                        "description": "JSON: [[[x1,y1,z1],[x2,y2,z2],...], [[x1,y1,z1],...]]"
                    }
                },
                "required": ["paths"]
            }
        ),
        Tool(
            name="draw_path",
            description="Dessine un chemin à la position actuelle du pinceau",
            inputSchema={
                "type": "object",
                "properties": {
                    "path": {
                        "type": "string",
                        "description": "JSON: [x1,y1,z1],[x2,y2,z2],..."
                    }
                },
                "required": ["path"]
            }
        ),
        Tool(
            name="draw_stroke",
            description="Dessine un trait exact avec orientation et pression",
            inputSchema={
                "type": "object",
                "properties": {
                    "stroke": {
                        "type": "string",
                        "description": "JSON: [x,y,z,pitch,yaw,roll,pressure],..."
                    }
                },
                "required": ["stroke"]
            }
        ),
        Tool(
            name="draw_polygon",
            description="Dessine un polygone à la position actuelle du pinceau",
            inputSchema={
                "type": "object",
                "properties": {
                    "sides": {"type": "integer", "description": "Nombre de côtés"},
                    "radius": {"type": "number", "description": "Rayon du polygone"},
                    "angle": {"type": "number", "description": "Angle de rotation"}
                },
                "required": ["sides", "radius", "angle"]
            }
        ),
        Tool(
            name="draw_text",
            description="Dessine du texte à la position actuelle du pinceau",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Texte à dessiner"}
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="draw_svg_path",
            description="Dessine un chemin SVG à la position actuelle",
            inputSchema={
                "type": "object",
                "properties": {
                    "svg_path": {"type": "string", "description": "Chaîne de chemin SVG"}
                },
                "required": ["svg_path"]
            }
        ),
        
        # === BRUSH COMMANDS ===
        Tool(
            name="brush_set_type",
            description="Change le type de pinceau",
            inputSchema={
                "type": "object",
                "properties": {
                    "brush_type": {
                        "type": "string",
                        "description": "Nom ou GUID du pinceau (ex: 'ink', 'marker', 'light')"
                    }
                },
                "required": ["brush_type"]
            }
        ),
        Tool(
            name="brush_set_size",
            description="Définit la taille du pinceau",
            inputSchema={
                "type": "object",
                "properties": {
                    "size": {"type": "number", "description": "Taille du pinceau"}
                },
                "required": ["size"]
            }
        ),
        Tool(
            name="brush_add_size",
            description="Modifie la taille du pinceau par un montant",
            inputSchema={
                "type": "object",
                "properties": {
                    "amount": {"type": "number", "description": "Montant à ajouter"}
                },
                "required": ["amount"]
            }
        ),
        Tool(
            name="brush_set_path_smoothing",
            description="Définit le lissage des chemins du pinceau (0-1, défaut 0.1)",
            inputSchema={
                "type": "object",
                "properties": {
                    "amount": {"type": "number", "description": "Quantité de lissage (0 = aucun)"}
                },
                "required": ["amount"]
            }
        ),
        Tool(
            name="brush_move",
            description="Déplace le pinceau à une position absolue",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        Tool(
            name="brush_translate",
            description="Déplace le pinceau de manière relative",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        Tool(
            name="brush_rotate",
            description="Définit la rotation du pinceau",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "Rotation X (pitch)"},
                    "y": {"type": "number", "description": "Rotation Y (yaw)"},
                    "z": {"type": "number", "description": "Rotation Z (roll)"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        Tool(
            name="brush_turn",
            description="Tourne le pinceau de manière relative",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": []
            }
        ),
        Tool(
            name="brush_draw",
            description="Dessine une ligne droite de longueur spécifiée",
            inputSchema={
                "type": "object",
                "properties": {
                    "length": {"type": "number", "description": "Longueur de la ligne"}
                },
                "required": ["length"]
            }
        ),
        
        # === COLOR COMMANDS ===
        Tool(
            name="color_set_rgb",
            description="Définit la couleur en RGB (0-1)",
            inputSchema={
                "type": "object",
                "properties": {
                    "r": {"type": "number", "minimum": 0, "maximum": 1},
                    "g": {"type": "number", "minimum": 0, "maximum": 1},
                    "b": {"type": "number", "minimum": 0, "maximum": 1}
                },
                "required": ["r", "g", "b"]
            }
        ),
        Tool(
            name="color_set_hsv",
            description="Définit la couleur en HSV (0-1)",
            inputSchema={
                "type": "object",
                "properties": {
                    "h": {"type": "number", "minimum": 0, "maximum": 1},
                    "s": {"type": "number", "minimum": 0, "maximum": 1},
                    "v": {"type": "number", "minimum": 0, "maximum": 1}
                },
                "required": ["h", "s", "v"]
            }
        ),
        Tool(
            name="color_set_html",
            description="Définit la couleur avec une valeur HTML/CSS",
            inputSchema={
                "type": "object",
                "properties": {
                    "color": {
                        "type": "string",
                        "description": "Nom de couleur CSS ou valeur hex (ex: 'red', '#FF0000')"
                    }
                },
                "required": ["color"]
            }
        ),
        Tool(
            name="color_add_rgb",
            description="Ajoute des valeurs à la couleur actuelle (RGB)",
            inputSchema={
                "type": "object",
                "properties": {
                    "r": {"type": "number"},
                    "g": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["r", "g", "b"]
            }
        ),
        Tool(
            name="color_add_hsv",
            description="Ajoute des valeurs à la couleur actuelle (HSV)",
            inputSchema={
                "type": "object",
                "properties": {
                    "h": {"type": "number"},
                    "s": {"type": "number"},
                    "v": {"type": "number"}
                },
                "required": ["h", "s", "v"]
            }
        ),
        
        # === MODEL COMMANDS ===
        Tool(
            name="model_import",
            description="Importe un modèle 3D depuis Media Library/Models",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Nom du fichier modèle"}
                },
                "required": ["filename"]
            }
        ),
        Tool(
            name="model_web_import",
            description="Importe un modèle 3D depuis une URL ou fichier local",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "URL ou chemin du modèle"}
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="model_icosa_import",
            description="Importe un modèle depuis Icosa Gallery",
            inputSchema={
                "type": "object",
                "properties": {
                    "model_id": {"type": "string", "description": "ID du modèle Icosa"}
                },
                "required": ["model_id"]
            }
        ),
        Tool(
            name="model_select",
            description="Sélectionne un modèle 3D par index",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer", "description": "Index du modèle"}
                },
                "required": ["index"]
            }
        ),
        Tool(
            name="model_position",
            description="Déplace un modèle 3D aux coordonnées données",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["index", "x", "y", "z"]
            }
        ),
        Tool(
            name="model_rotation",
            description="Définit la rotation d'un modèle 3D",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["index", "x", "y", "z"]
            }
        ),
        Tool(
            name="model_scale",
            description="Définit l'échelle d'un modèle 3D",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "scale": {"type": "number"}
                },
                "required": ["index", "scale"]
            }
        ),
        Tool(
            name="model_delete",
            description="Supprime un modèle 3D par index",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer"}
                },
                "required": ["index"]
            }
        ),
        
        # === SAVE/LOAD COMMANDS ===
        Tool(
            name="save_overwrite",
            description="Sauvegarde la scène en écrasant la dernière sauvegarde",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="save_as",
            description="Sauvegarde la scène sous un nouveau nom",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Nom du fichier (sans .tilt)"}
                },
                "required": ["filename"]
            }
        ),
        Tool(
            name="save_new",
            description="Sauvegarde la scène dans un nouveau slot",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="load_user",
            description="Charge un sketch du dossier utilisateur par index",
            inputSchema={
                "type": "object",
                "properties": {
                    "slot": {"type": "integer", "description": "Index (0 = plus récent)"}
                },
                "required": ["slot"]
            }
        ),
        Tool(
            name="load_named",
            description="Charge un sketch par nom depuis le dossier utilisateur",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Nom du fichier"}
                },
                "required": ["filename"]
            }
        ),
        Tool(
            name="new_scene",
            description="Crée une nouvelle scène vide",
            inputSchema={"type": "object", "properties": {}}
        ),
        
        # === CAMERA COMMANDS ===
        Tool(
            name="camera_move",
            description="Déplace la caméra à une position absolue",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        Tool(
            name="camera_translate",
            description="Déplace la caméra de manière relative",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        Tool(
            name="camera_rotate",
            description="Définit la rotation de la caméra",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        Tool(
            name="camera_turn",
            description="Tourne la caméra de manière relative",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": []
            }
        ),
        Tool(
            name="spectator_move",
            description="Déplace la caméra spectateur",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        
        # === SELECTION COMMANDS ===
        Tool(
            name="selection_select_all",
            description="Sélectionne tous les traits",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="selection_invert",
            description="Inverse la sélection",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="selection_delete",
            description="Supprime la sélection actuelle",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="selection_duplicate",
            description="Duplique la sélection actuelle",
            inputSchema={"type": "object", "properties": {}}
        ),
        
        # === LAYER COMMANDS ===
        Tool(
            name="layer_create",
            description="Crée un nouveau calque",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Nom du calque"}
                },
                "required": []
            }
        ),
        Tool(
            name="layer_set",
            description="Définit le calque actif",
            inputSchema={
                "type": "object",
                "properties": {
                    "layer": {"type": "integer", "description": "Numéro du calque"}
                },
                "required": ["layer"]
            }
        ),
        Tool(
            name="layer_show",
            description="Affiche un calque",
            inputSchema={
                "type": "object",
                "properties": {
                    "layer": {"type": "integer"}
                },
                "required": ["layer"]
            }
        ),
        Tool(
            name="layer_hide",
            description="Cache un calque",
            inputSchema={
                "type": "object",
                "properties": {
                    "layer": {"type": "integer"}
                },
                "required": ["layer"]
            }
        ),
        
        # === GUIDE COMMANDS ===
        Tool(
            name="guide_add",
            description="Ajoute un guide à la scène",
            inputSchema={
                "type": "object",
                "properties": {
                    "guide_type": {
                        "type": "string",
                        "enum": ["cube", "sphere", "capsule", "cone", "ellipsoid"],
                        "description": "Type de guide"
                    }
                },
                "required": ["guide_type"]
            }
        ),
        Tool(
            name="guide_position",
            description="Déplace un guide aux coordonnées données",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["index", "x", "y", "z"]
            }
        ),
        Tool(
            name="guide_scale",
            description="Définit l'échelle non-uniforme d'un guide",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer"},
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["index", "x", "y", "z"]
            }
        ),
        
        # === SYMMETRY COMMANDS ===
        Tool(
            name="symmetry_mode",
            description="Définit le mode de symétrie",
            inputSchema={
                "type": "object",
                "properties": {
                    "mode": {
                        "type": "string",
                        "enum": ["none", "single", "double", "quad", "radial"],
                        "description": "Mode de symétrie"
                    }
                },
                "required": ["mode"]
            }
        ),
        Tool(
            name="symmetry_position",
            description="Déplace le widget de symétrie",
            inputSchema={
                "type": "object",
                "properties": {
                    "x": {"type": "number"},
                    "y": {"type": "number"},
                    "z": {"type": "number"}
                },
                "required": ["x", "y", "z"]
            }
        ),
        
        # === UTILITY COMMANDS ===
        Tool(
            name="undo",
            description="Annule la dernière action",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="redo",
            description="Refait la dernière action annulée",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="show_help",
            description="Affiche l'aide de l'API",
            inputSchema={"type": "object", "properties": {}}
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> List[TextContent]:
    """
    Gère les appels d'outils et les traduit en appels API Open Brush
    """
    
    # Mapping des noms d'outils vers les commandes API
    command_map = {
        # Drawing
        "draw_paths": lambda args: {"draw.paths": args["paths"]},
        "draw_path": lambda args: {"draw.path": args["path"]},
        "draw_stroke": lambda args: {"draw.stroke": args["stroke"]},
        "draw_polygon": lambda args: {"draw.polygon": f"{args['sides']},{args['radius']},{args['angle']}"},
        "draw_text": lambda args: {"draw.text": args["text"]},
        "draw_svg_path": lambda args: {"draw.svg.path": args["svg_path"]},
        
        # Brush
        "brush_set_type": lambda args: {"brush.type": args["brush_type"]},
        "brush_set_size": lambda args: {"brush.size.set": str(args["size"])},
        "brush_add_size": lambda args: {"brush.size.add": str(args["amount"])},
        "brush_set_path_smoothing": lambda args: {"brush.pathsmoothing": str(args["amount"])},
        "brush_move": lambda args: {"brush.move": f"{args['x']},{args['y']},{args['z']}"},
        "brush_translate": lambda args: {"brush.translate": f"{args['x']},{args['y']},{args['z']}"},
        "brush_rotate": lambda args: {"brush.rotate": f"{args['x']},{args['y']},{args['z']}"},
        "brush_turn": lambda args: {
            "brush.turn.x": str(args.get("x", 0)),
            "brush.turn.y": str(args.get("y", 0)),
            "brush.turn.z": str(args.get("z", 0))
        },
        "brush_draw": lambda args: {"brush.draw": str(args["length"])},
        
        # Color
        "color_set_rgb": lambda args: {"color.set.rgb": f"{args['r']},{args['g']},{args['b']}"},
        "color_set_hsv": lambda args: {"color.set.hsv": f"{args['h']},{args['s']},{args['v']}"},
        "color_set_html": lambda args: {"color.set.html": args["color"]},
        "color_add_rgb": lambda args: {"color.add.rgb": f"{args['r']},{args['g']},{args['b']}"},
        "color_add_hsv": lambda args: {"color.add.hsv": f"{args['h']},{args['s']},{args['v']}"},
        
        # Model
        "model_import": lambda args: {"model.import": args["filename"]},
        "model_web_import": lambda args: {"model.webimport": args["url"]},
        "model_icosa_import": lambda args: {"model.icosaimport": args["model_id"]},
        "model_select": lambda args: {"model.select": str(args["index"])},
        "model_position": lambda args: {"model.position": f"{args['index']},{args['x']},{args['y']},{args['z']}"},
        "model_rotation": lambda args: {"model.rotation": f"{args['index']},{args['x']},{args['y']},{args['z']}"},
        "model_scale": lambda args: {"model.scale": f"{args['index']},{args['scale']}"},
        "model_delete": lambda args: {"model.delete": str(args["index"])},
        
        # Save/Load
        "save_overwrite": lambda args: {"save.overwrite": ""},
        "save_as": lambda args: {"save.as": args["filename"]},
        "save_new": lambda args: {"save.new": ""},
        "load_user": lambda args: {"load.user": str(args["slot"])},
        "load_named": lambda args: {"load.named": args["filename"]},
        "new_scene": lambda args: {"scene.new": ""},
        
        # Camera
        "camera_move": lambda args: {"camera.move": f"{args['x']},{args['y']},{args['z']}"},
        "camera_translate": lambda args: {"camera.translate": f"{args['x']},{args['y']},{args['z']}"},
        "camera_rotate": lambda args: {"camera.rotate": f"{args['x']},{args['y']},{args['z']}"},
        "camera_turn": lambda args: {
            "camera.turn.x": str(args.get("x", 0)),
            "camera.turn.y": str(args.get("y", 0)),
            "camera.turn.z": str(args.get("z", 0))
        },
        "spectator_move": lambda args: {"spectator.move": f"{args['x']},{args['y']},{args['z']}"},
        
        # Selection
        "selection_select_all": lambda args: {"selection.all": ""},
        "selection_invert": lambda args: {"selection.invert": ""},
        "selection_delete": lambda args: {"selection.delete": ""},
        "selection_duplicate": lambda args: {"selection.duplicate": ""},
        
        # Layers
        "layer_create": lambda args: {"layer.create": args.get("name", "")},
        "layer_set": lambda args: {"layer.set": str(args["layer"])},
        "layer_show": lambda args: {"layer.show": str(args["layer"])},
        "layer_hide": lambda args: {"layer.hide": str(args["layer"])},
        
        # Guides
        "guide_add": lambda args: {"guide.add": args["guide_type"]},
        "guide_position": lambda args: {"guide.position": f"{args['index']},{args['x']},{args['y']},{args['z']}"},
        "guide_scale": lambda args: {"guide.scale": f"{args['index']},{args['x']},{args['y']},{args['z']}"},
        
        # Symmetry
        "symmetry_mode": lambda args: {"symmetry.mode": args["mode"]},
        "symmetry_position": lambda args: {"symmetry.position": f"{args['x']},{args['y']},{args['z']}"},
        
        # Utility
        "undo": lambda args: {"undo": ""},
        "redo": lambda args: {"redo": ""},
        "show_help": lambda args: {"help": ""},
    }
    
    if name not in command_map:
        return [TextContent(type="text", text=f"Outil inconnu: {name}")]
    
    try:
        # Convertir les arguments en paramètres API
        params = command_map[name](arguments)
        
        # Appeler l'API Open Brush
        result = await call_openbrush_api(params)
        
        return [TextContent(
            type="text",
            text=f"Commande exécutée avec succès: {name}\nRésultat: {result}"
        )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Erreur lors de l'exécution de {name}: {str(e)}"
        )]


async def main():
    """Point d'entrée principal du serveur MCP"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
