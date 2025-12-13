# Quick Reference Guide - Open Brush MCP Commands

## 🎨 DRAWING

### draw_paths
Draw multiple paths
```json
{
  "paths": "[[[0,0,0],[1,0,0]],[[0,0,1],[1,0,1]]]"
}
```

### draw_path
Draw a simple path
```json
{
  "path": "[0,0,0],[1,0,0],[1,1,0]"
}
```

### draw_polygon
Draw a polygon
```json
{
  "sides": 6,
  "radius": 2.5,
  "angle": 45
}
```

### draw_text
Draw text
```json
{
  "text": "Hello World"
}
```

## 🖌️ BRUSH

### brush_set_type
Change brush type
```json
{
  "brush_type": "ink"
}
```
Common types: ink, marker, light, fire, snow, stars, etc.

### brush_set_size
Set size
```json
{
  "size": 0.5
}
```

### brush_move
Move brush (absolute)
```json
{
  "x": 0,
  "y": 1,
  "z": 0
}
```

### brush_translate
Move brush (relative)
```json
{
  "x": 0.5,
  "y": 0,
  "z": 0
}
```

### brush_rotate
Absolute rotation
```json
{
  "x": 0,
  "y": 90,
  "z": 0
}
```

### brush_turn
Relative rotation
```json
{
  "x": 0,
  "y": 45,
  "z": 0
}
```

### brush_draw
Draw a straight line
```json
{
  "length": 2.0
}
```

## 🎨 COLOR

### color_set_rgb
Color in RGB (0-1)
```json
{
  "r": 1.0,
  "g": 0.0,
  "b": 0.0
}
```

### color_set_hsv
Color in HSV (0-1)
```json
{
  "h": 0.5,
  "s": 1.0,
  "v": 1.0
}
```

### color_set_html
HTML/CSS color
```json
{
  "color": "darkblue"
}
```
or
```json
{
  "color": "#FF5500"
}
```

## 🧊 3D MODELS

### model_import
Import local model
```json
{
  "filename": "Andy.glb"
}
```

### model_web_import
Import from URL
```json
{
  "url": "https://example.com/model.obj"
}
```

### model_icosa_import
Import from Icosa Gallery
```json
{
  "model_id": "9L2Lt-sxzdp"
}
```

### model_position
Position a model
```json
{
  "index": 0,
  "x": 1.0,
  "y": 2.0,
  "z": 3.0
}
```

### model_scale
Scale a model
```json
{
  "index": 0,
  "scale": 2.0
}
```

## 💾 SAVE/LOAD

### save_as
Save with a name
```json
{
  "filename": "my_creation"
}
```

### load_named
Load by name
```json
{
  "filename": "my_creation"
}
```

### load_user
Load by index
```json
{
  "slot": 0
}
```
(0 = most recent)

## 📷 CAMERA

### camera_move
Move camera (absolute)
```json
{
  "x": 0,
  "y": 2,
  "z": -5
}
```

### camera_rotate
Rotate camera
```json
{
  "x": 0,
  "y": 180,
  "z": 0
}
```

## ✂️ SELECTION

### selection_select_all
Select all
```json
{}
```

### selection_delete
Delete selection
```json
{}
```

### selection_duplicate
Duplicate selection
```json
{}
```

## 📑 LAYERS

### layer_create
Create a layer
```json
{
  "name": "My Layer"
}
```

### layer_set
Activate a layer
```json
{
  "layer": 1
}
```

### layer_show / layer_hide
Show/Hide a layer
```json
{
  "layer": 1
}
```

## 📐 GUIDES

### guide_add
Add a guide
```json
{
  "guide_type": "cube"
}
```
Types: cube, sphere, capsule, cone, ellipsoid

### guide_position
Position a guide
```json
{
  "index": 0,
  "x": 0,
  "y": 1,
  "z": 0
}
```

## 🔄 SYMMETRY

### symmetry_mode
Symmetry mode
```json
{
  "mode": "quad"
}
```
Modes: none, single, double, quad, radial

### symmetry_position
Widget position
```json
{
  "x": 0,
  "y": 0,
  "z": 0
}
```

## 🔧 UTILITIES

### undo
Undo last action
```json
{}
```

### redo
Redo last action
```json
{}
```

---

## 💡 WORKFLOW EXAMPLES

### Create a colored square
1. `color_set_html` with `{"color": "red"}`
2. `brush_set_type` with `{"brush_type": "ink"}`
3. `brush_set_size` with `{"size": 0.5}`
4. `draw_polygon` with `{"sides": 4, "radius": 2, "angle": 45}`

### Import and position a model
1. `model_import` with `{"filename": "Andy.glb"}`
2. `model_position` with `{"index": 0, "x": 0, "y": 1, "z": 2}`
3. `model_scale` with `{"index": 0, "scale": 1.5}`

### Create a spiral
1. `brush_move` to starting position
2. Loop:
   - `brush_translate` small step forward
   - `brush_turn` Y rotation by a few degrees
   - `brush_draw` with small length

### Working with layers
1. `layer_create` with `{"name": "Background"}`
2. Draw background
3. `layer_create` with `{"name": "Foreground"}`
4. `layer_set` with `{"layer": 1}`
5. Draw foreground
6. `layer_hide` with `{"layer": 0}` to hide background

---

**Note**: All angles are in degrees. Coordinates follow Unity coordinate system (Y up).
