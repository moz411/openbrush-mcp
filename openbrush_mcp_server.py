#!/usr/bin/env python3
"""
MCP Server for Open Brush API
Exposes all Open Brush commands as MCP tools
"""

import asyncio
import httpx
from typing import Any, Dict, List, Optional, Tuple
from mcp.server.fastmcp import FastMCP

# Configuration
API_BASE_URL = "http://localhost:40074/api/v1"

# Create MCP server
mcp = FastMCP("openbrush", json_response=True)


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








async def main():
    """Main entry point for MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await app.run(
            read_stream,
            write_stream,
            app.create_initialization_options()
        )


@mcp.tool()
async def draw_paths(paths: str) -> str:
    """Draws a series of paths at the current brush position"""
    params = {"draw.paths": paths}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: draw_paths"
    else:
        return f"✗ Failed (HTTP {status_code}): draw_paths"


@mcp.tool()
async def draw_path(path: str) -> str:
    """Draws a path at the current brush position"""
    params = {"draw.path": path}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: draw_path"
    else:
        return f"✗ Failed (HTTP {status_code}): draw_path"


@mcp.tool()
async def draw_stroke(stroke: str) -> str:
    """Draws an exact stroke with orientation and pressure"""
    params = {"draw.stroke": stroke}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: draw_stroke"
    else:
        return f"✗ Failed (HTTP {status_code}): draw_stroke"


@mcp.tool()
async def draw_polygon(sides: int, radius: float, angle: float) -> str:
    """Draws a polygon at the current brush position"""
    params = {"draw.polygon": f"{sides},{radius},{angle}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: draw_polygon"
    else:
        return f"✗ Failed (HTTP {status_code}): draw_polygon"


@mcp.tool()
async def draw_text(text: str) -> str:
    """Draws text at the current brush position"""
    params = {"draw.text": text}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: draw_text"
    else:
        return f"✗ Failed (HTTP {status_code}): draw_text"


@mcp.tool()
async def draw_svg_path(svg_path: str) -> str:
    """Draws an SVG path at the current position"""
    params = {"draw.svg.path": svg_path}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: draw_svg_path"
    else:
        return f"✗ Failed (HTTP {status_code}): draw_svg_path"


# Brush commands
@mcp.tool()
async def brush_set_type(brush_type: str) -> str:
    """Change brush type"""
    params = {"brush.type": brush_type}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_set_type"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_set_type"


@mcp.tool()
async def brush_set_size(size: float) -> str:
    """Sets brush size"""
    params = {"brush.size.set": str(size)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_set_size"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_set_size"


@mcp.tool()
async def brush_add_size(amount: float) -> str:
    """Modifies brush size by an amount"""
    params = {"brush.size.add": str(amount)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_add_size"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_add_size"


@mcp.tool()
async def brush_set_path_smoothing(amount: float) -> str:
    """Sets brush path smoothing (0-1, default 0.1)"""
    params = {"brush.pathsmoothing": str(amount)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_set_path_smoothing"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_set_path_smoothing"


@mcp.tool()
async def brush_move(x: float, y: float, z: float) -> str:
    """Moves brush to absolute position"""
    params = {"brush.move.to": f"{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_move"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_move"


@mcp.tool()
async def brush_translate(x: float, y: float, z: float) -> str:
    """Moves brush relatively"""
    params = {"brush.move.by": f"{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_translate"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_translate"


@mcp.tool()
async def brush_turn(x: float = 0, y: float = 0, z: float = 0) -> str:
    """Turns brush relatively"""
    params = {
        "brush.turn.x": str(x),
        "brush.turn.y": str(y),
        "brush.turn.z": str(z)
    }
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_turn"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_turn"


@mcp.tool()
async def brush_draw(length: float) -> str:
    """Draws a straight line of specified length"""
    params = {"brush.draw": str(length)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: brush_draw"
    else:
        return f"✗ Failed (HTTP {status_code}): brush_draw"


# Color commands
@mcp.tool()
async def color_set_rgb(r: float, g: float, b: float) -> str:
    """Sets color in RGB (0-1)"""
    params = {"color.set.rgb": f"{r},{g},{b}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: color_set_rgb"
    else:
        return f"✗ Failed (HTTP {status_code}): color_set_rgb"


@mcp.tool()
async def color_set_hsv(h: float, s: float, v: float) -> str:
    """Sets color in HSV (0-1)"""
    params = {"color.set.hsv": f"{h},{s},{v}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: color_set_hsv"
    else:
        return f"✗ Failed (HTTP {status_code}): color_set_hsv"


@mcp.tool()
async def color_set_html(color: str) -> str:
    """Sets color with HTML/CSS value"""
    params = {"color.set.html": color}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: color_set_html"
    else:
        return f"✗ Failed (HTTP {status_code}): color_set_html"


@mcp.tool()
async def color_add_rgb(r: float, g: float, b: float) -> str:
    """Adds values to current color (RGB)"""
    params = {"color.add.rgb": f"{r},{g},{b}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: color_add_rgb"
    else:
        return f"✗ Failed (HTTP {status_code}): color_add_rgb"


@mcp.tool()
async def color_add_hsv(h: float, s: float, v: float) -> str:
    """Adds values to current color (HSV)"""
    params = {"color.add.hsv": f"{h},{s},{v}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: color_add_hsv"
    else:
        return f"✗ Failed (HTTP {status_code}): color_add_hsv"


# Model commands
@mcp.tool()
async def model_import(filename: str) -> str:
    """Imports a 3D model from Media Library/Models"""
    params = {"model.import": filename}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_import"
    else:
        return f"✗ Failed (HTTP {status_code}): model_import"


@mcp.tool()
async def model_web_import(url: str) -> str:
    """Imports a 3D model from URL or local file"""
    params = {"model.webimport": url}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_web_import"
    else:
        return f"✗ Failed (HTTP {status_code}): model_web_import"


@mcp.tool()
async def model_icosa_import(model_id: str) -> str:
    """Imports a model from Icosa Gallery"""
    params = {"model.icosaimport": model_id}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_icosa_import"
    else:
        return f"✗ Failed (HTTP {status_code}): model_icosa_import"


@mcp.tool()
async def model_select(index: int) -> str:
    """Selects a 3D model by index"""
    params = {"model.select": str(index)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_select"
    else:
        return f"✗ Failed (HTTP {status_code}): model_select"


@mcp.tool()
async def model_position(index: int, x: float, y: float, z: float) -> str:
    """Moves a 3D model to given coordinates"""
    params = {"model.position": f"{index},{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_position"
    else:
        return f"✗ Failed (HTTP {status_code}): model_position"


@mcp.tool()
async def model_rotation(index: int, x: float, y: float, z: float) -> str:
    """Sets a 3D model's rotation"""
    params = {"model.rotation": f"{index},{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_rotation"
    else:
        return f"✗ Failed (HTTP {status_code}): model_rotation"


@mcp.tool()
async def model_scale(index: int, scale: float) -> str:
    """Sets a 3D model's scale"""
    params = {"model.scale": f"{index},{scale}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_scale"
    else:
        return f"✗ Failed (HTTP {status_code}): model_scale"


@mcp.tool()
async def model_delete(index: int) -> str:
    """Deletes a 3D model by index"""
    params = {"model.delete": str(index)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: model_delete"
    else:
        return f"✗ Failed (HTTP {status_code}): model_delete"


# Save/Load commands
@mcp.tool()
async def save_overwrite() -> str:
    """Saves the scene by overwriting the last save"""
    params = {"save.overwrite": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: save_overwrite"
    else:
        return f"✗ Failed (HTTP {status_code}): save_overwrite"


@mcp.tool()
async def save_as(filename: str) -> str:
    """Saves the scene with a new name"""
    params = {"save.as": filename}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: save_as"
    else:
        return f"✗ Failed (HTTP {status_code}): save_as"


@mcp.tool()
async def save_new() -> str:
    """Saves the scene in a new slot"""
    params = {"save.new": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: save_new"
    else:
        return f"✗ Failed (HTTP {status_code}): save_new"


@mcp.tool()
async def load_user(slot: int) -> str:
    """Loads a sketch from user folder by index"""
    params = {"load.user": str(slot)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: load_user"
    else:
        return f"✗ Failed (HTTP {status_code}): load_user"


@mcp.tool()
async def load_named(filename: str) -> str:
    """Loads a sketch by name from user folder"""
    params = {"load.named": filename}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: load_named"
    else:
        return f"✗ Failed (HTTP {status_code}): load_named"


@mcp.tool()
async def new_scene() -> str:
    """Creates a new empty scene"""
    params = {"new": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: new_scene"
    else:
        return f"✗ Failed (HTTP {status_code}): new_scene"


# Camera commands
@mcp.tool()
async def camera_move(x: float, y: float, z: float) -> str:
    """Moves camera to absolute position"""
    params = {"user.move.to": f"{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: camera_move"
    else:
        return f"✗ Failed (HTTP {status_code}): camera_move"


@mcp.tool()
async def camera_translate(x: float, y: float, z: float) -> str:
    """Moves camera relatively"""
    params = {"user.move.by": f"{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: camera_translate"
    else:
        return f"✗ Failed (HTTP {status_code}): camera_translate"


@mcp.tool()
async def camera_rotate(x: float, y: float, z: float) -> str:
    """Sets camera rotation"""
    params = {"user.direction": f"{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: camera_rotate"
    else:
        return f"✗ Failed (HTTP {status_code}): camera_rotate"


@mcp.tool()
async def camera_turn(x: float = 0, y: float = 0, z: float = 0) -> str:
    """Turns camera relatively"""
    params = {
        "user.turn.x": str(x),
        "user.turn.y": str(y),
        "user.turn.z": str(z)
    }
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: camera_turn"
    else:
        return f"✗ Failed (HTTP {status_code}): camera_turn"


@mcp.tool()
async def spectator_move(x: float, y: float, z: float) -> str:
    """Moves spectator camera"""
    params = {"spectator.move.to": f"{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: spectator_move"
    else:
        return f"✗ Failed (HTTP {status_code}): spectator_move"


# Selection commands
@mcp.tool()
async def selection_select_all() -> str:
    """Selects all strokes"""
    params = {"select.all": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: selection_select_all"
    else:
        return f"✗ Failed (HTTP {status_code}): selection_select_all"


@mcp.tool()
async def selection_invert() -> str:
    """Inverts selection"""
    params = {"selection.invert": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: selection_invert"
    else:
        return f"✗ Failed (HTTP {status_code}): selection_invert"


@mcp.tool()
async def selection_delete() -> str:
    """Deletes current selection"""
    params = {"selection.delete": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: selection_delete"
    else:
        return f"✗ Failed (HTTP {status_code}): selection_delete"


@mcp.tool()
async def selection_duplicate() -> str:
    """Duplicates current selection"""
    params = {"selection.duplicate": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: selection_duplicate"
    else:
        return f"✗ Failed (HTTP {status_code}): selection_duplicate"


# Layer commands
@mcp.tool()
async def layer_create() -> str:
    """Creates a new layer"""
    params = {"layer.add": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: layer_create"
    else:
        return f"✗ Failed (HTTP {status_code}): layer_create"


@mcp.tool()
async def layer_set(layer: int) -> str:
    """Sets active layer"""
    params = {"layer.activate": str(layer)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: layer_set"
    else:
        return f"✗ Failed (HTTP {status_code}): layer_set"


@mcp.tool()
async def layer_show(layer: int) -> str:
    """Shows a layer"""
    params = {"layer.show": str(layer)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: layer_show"
    else:
        return f"✗ Failed (HTTP {status_code}): layer_show"


@mcp.tool()
async def layer_hide(layer: int) -> str:
    """Hides a layer"""
    params = {"layer.hide": str(layer)}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: layer_hide"
    else:
        return f"✗ Failed (HTTP {status_code}): layer_hide"


# Guide commands
@mcp.tool()
async def guide_add(guide_type: str) -> str:
    """Adds a guide to the scene"""
    params = {"guide.add": guide_type}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: guide_add"
    else:
        return f"✗ Failed (HTTP {status_code}): guide_add"


@mcp.tool()
async def guide_position(index: int, x: float, y: float, z: float) -> str:
    """Moves a guide to given coordinates"""
    params = {"guide.position": f"{index},{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: guide_position"
    else:
        return f"✗ Failed (HTTP {status_code}): guide_position"


@mcp.tool()
async def guide_scale(index: int, x: float, y: float, z: float) -> str:
    """Sets non-uniform scale of a guide"""
    params = {"guide.scale": f"{index},{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: guide_scale"
    else:
        return f"✗ Failed (HTTP {status_code}): guide_scale"


# Symmetry commands
@mcp.tool()
async def symmetry_mode(mode: str) -> str:
    """Sets symmetry mode"""
    params = {"symmetry.mode": mode}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: symmetry_mode"
    else:
        return f"✗ Failed (HTTP {status_code}): symmetry_mode"


@mcp.tool()
async def symmetry_position(x: float, y: float, z: float) -> str:
    """Moves symmetry widget"""
    params = {"symmetry.position": f"{x},{y},{z}"}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: symmetry_position"
    else:
        return f"✗ Failed (HTTP {status_code}): symmetry_position"


# Utility commands
@mcp.tool()
async def undo() -> str:
    """Undoes last action"""
    params = {"undo": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: undo"
    else:
        return f"✗ Failed (HTTP {status_code}): undo"


@mcp.tool()
async def redo() -> str:
    """Redoes last undone action"""
    params = {"redo": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: redo"
    else:
        return f"✗ Failed (HTTP {status_code}): redo"


@mcp.tool()
async def show_help() -> str:
    """Shows API help"""
    params = {"help": None}
    status_code, url = await call_openbrush_api(params)
    if status_code == 200:
        return "✓ Command executed: show_help"
    else:
        return f"✗ Failed (HTTP {status_code}): show_help"


if __name__ == "__main__":
    mcp.run()

