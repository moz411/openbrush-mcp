#!/usr/bin/env python3
"""
MCP Server for Open Brush API
Exposes all Open Brush commands as MCP tools
"""

import asyncio
import httpx
from typing import Any, Dict, List, Optional, Tuple
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

# Configuration
API_BASE_URL = "http://localhost:40074/api/v1"

# Create MCP server
app = Server("openbrush-mcp")


async def call_openbrush_api(params: Dict[str, Any]) -> Tuple[int, str]:
    """
    Calls the Open Brush API with the provided parameters
    Returns: (status_code, url_called)
    """
    try:
        # Filter out None values to avoid sending =None
        filtered_params = {k: v for k, v in params.items() if v is not None}
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.get(API_BASE_URL, params=filtered_params)
            # Build the complete URL for debugging
            url = str(response.url)
            return (response.status_code, url)
    except httpx.HTTPError as e:
        return (-1, f"HTTP Error: {str(e)}")
    except Exception as e:
        return (-1, f"Error: {str(e)}")


@app.list_tools()
async def list_tools() -> List[Tool]:
    """
    Lists all available tools based on the Open Brush API
    """
    return [
        # === DRAWING COMMANDS ===
        Tool(
            name="draw_paths",
            description="Draws a series of paths at the current brush position",
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
            description="Draws a path at the current brush position",
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
            description="Draws an exact stroke with orientation and pressure",
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
            description="Draws a polygon at the current brush position",
            inputSchema={
                "type": "object",
                "properties": {
                    "sides": {"type": "integer", "description": "Number of sides"},
                    "radius": {"type": "number", "description": "Polygon radius"},
                    "angle": {"type": "number", "description": "Rotation angle"}
                },
                "required": ["sides", "radius", "angle"]
            }
        ),
        Tool(
            name="draw_text",
            description="Draws text at the current brush position",
            inputSchema={
                "type": "object",
                "properties": {
                    "text": {"type": "string", "description": "Text to draw"}
                },
                "required": ["text"]
            }
        ),
        Tool(
            name="draw_svg_path",
            description="Draws an SVG path at the current position",
            inputSchema={
                "type": "object",
                "properties": {
                    "svg_path": {"type": "string", "description": "SVG path string"}
                },
                "required": ["svg_path"]
            }
        ),
        
        # === BRUSH COMMANDS ===
        Tool(
            name="brush_set_type",
            description="Change brush type",
            inputSchema={
                "type": "object",
                "properties": {
                    "brush_type": {
                        "type": "string",
                        "description": "Brush name or GUID (e.g. 'ink', 'marker', 'light')"
                    }
                },
                "required": ["brush_type"]
            }
        ),
        Tool(
            name="brush_set_size",
            description="Sets brush size",
            inputSchema={
                "type": "object",
                "properties": {
                    "size": {"type": "number", "description": "Brush size"}
                },
                "required": ["size"]
            }
        ),
        Tool(
            name="brush_add_size",
            description="Modifies brush size by an amount",
            inputSchema={
                "type": "object",
                "properties": {
                    "amount": {"type": "number", "description": "Amount to add"}
                },
                "required": ["amount"]
            }
        ),
        Tool(
            name="brush_set_path_smoothing",
            description="Sets brush path smoothing (0-1, default 0.1)",
            inputSchema={
                "type": "object",
                "properties": {
                    "amount": {"type": "number", "description": "Smoothing amount (0 = none)"}
                },
                "required": ["amount"]
            }
        ),
        Tool(
            name="brush_move",
            description="Moves brush to absolute position",
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
            description="Moves brush relatively",
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
            name="brush_turn",
            description="Turns brush relatively",
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
            description="Draws a straight line of specified length",
            inputSchema={
                "type": "object",
                "properties": {
                    "length": {"type": "number", "description": "Line length"}
                },
                "required": ["length"]
            }
        ),
        
        # === COLOR COMMANDS ===
        Tool(
            name="color_set_rgb",
            description="Sets color in RGB (0-1)",
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
            description="Sets color in HSV (0-1)",
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
            description="Sets color with HTML/CSS value",
            inputSchema={
                "type": "object",
                "properties": {
                    "color": {
                        "type": "string",
                        "description": "CSS color name or hex value (e.g. 'red', '#FF0000')"
                    }
                },
                "required": ["color"]
            }
        ),
        Tool(
            name="color_add_rgb",
            description="Adds values to current color (RGB)",
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
            description="Adds values to current color (HSV)",
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
            description="Imports a 3D model from Media Library/Models",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Model filename"}
                },
                "required": ["filename"]
            }
        ),
        Tool(
            name="model_web_import",
            description="Imports a 3D model from URL or local file",
            inputSchema={
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "Model URL or path"}
                },
                "required": ["url"]
            }
        ),
        Tool(
            name="model_icosa_import",
            description="Imports a model from Icosa Gallery",
            inputSchema={
                "type": "object",
                "properties": {
                    "model_id": {"type": "string", "description": "Icosa model ID"}
                },
                "required": ["model_id"]
            }
        ),
        Tool(
            name="model_select",
            description="Selects a 3D model by index",
            inputSchema={
                "type": "object",
                "properties": {
                    "index": {"type": "integer", "description": "Model index"}
                },
                "required": ["index"]
            }
        ),
        Tool(
            name="model_position",
            description="Moves a 3D model to given coordinates",
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
            description="Sets a 3D model's rotation",
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
            description="Sets a 3D model's scale",
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
            description="Deletes a 3D model by index",
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
            description="Saves the scene by overwriting the last save",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="save_as",
            description="Saves the scene with a new name",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Filename (without .tilt)"}
                },
                "required": ["filename"]
            }
        ),
        Tool(
            name="save_new",
            description="Saves the scene in a new slot",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="load_user",
            description="Loads a sketch from user folder by index",
            inputSchema={
                "type": "object",
                "properties": {
                    "slot": {"type": "integer", "description": "Index (0 = most recent)"}
                },
                "required": ["slot"]
            }
        ),
        Tool(
            name="load_named",
            description="Loads a sketch by name from user folder",
            inputSchema={
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "Filename"}
                },
                "required": ["filename"]
            }
        ),
        Tool(
            name="new_scene",
            description="Creates a new empty scene",
            inputSchema={"type": "object", "properties": {}}
        ),
        
        # === CAMERA COMMANDS ===
        Tool(
            name="camera_move",
            description="Moves camera to absolute position",
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
            description="Moves camera relatively",
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
            description="Sets camera rotation",
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
            description="Turns camera relatively",
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
            description="Moves spectator camera",
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
            description="Selects all strokes",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="selection_invert",
            description="Inverts selection",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="selection_delete",
            description="Deletes current selection",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="selection_duplicate",
            description="Duplicates current selection",
            inputSchema={"type": "object", "properties": {}}
        ),
        
        # === LAYER COMMANDS ===
        Tool(
            name="layer_create",
            description="Creates a new layer",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {"type": "string", "description": "Layer name"}
                },
                "required": []
            }
        ),
        Tool(
            name="layer_set",
            description="Sets active layer",
            inputSchema={
                "type": "object",
                "properties": {
                    "layer": {"type": "integer", "description": "Layer number"}
                },
                "required": ["layer"]
            }
        ),
        Tool(
            name="layer_show",
            description="Shows a layer",
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
            description="Hides a layer",
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
            description="Adds a guide to the scene",
            inputSchema={
                "type": "object",
                "properties": {
                    "guide_type": {
                        "type": "string",
                        "enum": ["cube", "sphere", "capsule", "cone", "ellipsoid"],
                        "description": "Guide type"
                    }
                },
                "required": ["guide_type"]
            }
        ),
        Tool(
            name="guide_position",
            description="Moves a guide to given coordinates",
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
            description="Sets non-uniform scale of a guide",
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
            description="Sets symmetry mode",
            inputSchema={
                "type": "object",
                "properties": {
                    "mode": {
                        "type": "string",
                        "enum": ["none", "single", "double", "quad", "radial"],
                        "description": "Symmetry mode"
                    }
                },
                "required": ["mode"]
            }
        ),
        Tool(
            name="symmetry_position",
            description="Moves symmetry widget",
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
            description="Undoes last action",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="redo",
            description="Redoes last undone action",
            inputSchema={"type": "object", "properties": {}}
        ),
        Tool(
            name="show_help",
            description="Shows API help",
            inputSchema={"type": "object", "properties": {}}
        ),
    ]


@app.call_tool()
async def call_tool(name: str, arguments: Any) -> List[TextContent]:
    """
    Handles tool calls and translates them to Open Brush API calls
    """
    
    # Mapping of tool names to API commands
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
        "brush_move": lambda args: {"brush.move.to": f"{args['x']},{args['y']},{args['z']}"},
        "brush_translate": lambda args: {"brush.move.by": f"{args['x']},{args['y']},{args['z']}"},

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
        "save_overwrite": lambda args: {"save.overwrite": None},
        "save_as": lambda args: {"save.as": args["filename"]},
        "save_new": lambda args: {"save.new": None},
        "load_user": lambda args: {"load.user": str(args["slot"])},
        "load_named": lambda args: {"load.named": args["filename"]},
        "new_scene": lambda args: {"new": None},
        
        # Camera
        "camera_move": lambda args: {"user.move.to": f"{args['x']},{args['y']},{args['z']}"},
        "camera_translate": lambda args: {"user.move.by": f"{args['x']},{args['y']},{args['z']}"},
        "camera_rotate": lambda args: {"user.direction": f"{args['x']},{args['y']},{args['z']}"},
        "camera_turn": lambda args: {
            "user.turn.x": str(args.get("x", 0)),
            "user.turn.y": str(args.get("y", 0)),
            "user.turn.z": str(args.get("z", 0))
        },
        "spectator_move": lambda args: {"spectator.move.to": f"{args['x']},{args['y']},{args['z']}"},
        
        # Selection
        "selection_select_all": lambda args: {"select.all": None},
        "selection_invert": lambda args: {"selection.invert": None},
        "selection_delete": lambda args: {"selection.delete": None},
        "selection_duplicate": lambda args: {"selection.duplicate": None},
        
        # Layers
        "layer_create": lambda args: {"layer.add": None},
        "layer_set": lambda args: {"layer.activate": str(args["layer"])},
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
        "undo": lambda args: {"undo": None},
        "redo": lambda args: {"redo": None},
        "show_help": lambda args: {"help": None},
    }
    
    if name not in command_map:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]
    
    try:
        # Convert arguments to API parameters
        params = command_map[name](arguments)
        
        # Call Open Brush API
        status_code, url = await call_openbrush_api(params)
        
        if status_code == 200:
            return [TextContent(
                type="text",
                text=f"✓ Command executed: {name}"
            )]
        else:
            return [TextContent(
                type="text",
                text=f"✗ Failed (HTTP {status_code}): {name}"
            )]
    except Exception as e:
        return [TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]


async def main():
    """Main entry point for MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())

