# MCP Server for Open Brush

This MCP (Model Context Protocol) server exposes the Open Brush API as tools usable by LLMs via the MCP protocol.

## 📋 Prerequisites

- Python 3.10 or higher
- Open Brush running with API enabled (port 40074)
- Access to an MCP client (like Claude Desktop)

## 🚀 Installation

1. **Clone or download the files**

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Make the script executable (optional on Linux/Mac)**
```bash
chmod +x openbrush_mcp_server.py
```

## ⚙️ Configuration

### Enable API in Open Brush

1. Launch Open Brush
2. Enable HTTP API in settings
3. API should be accessible at `http://localhost:40074/api/v1`

### Configure in Claude Desktop

Add this configuration to your Claude Desktop MCP configuration file:

**On macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`

**On Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "openbrush": {
      "command": "python",
      "args": [
        "/path/to/openbrush_mcp_server.py"
      ]
    }
  }
}
```

Replace `/path/to/` with the absolute path to the file.

## 📚 Available Tools

The server exposes many tools organized by category:

### 🎨 Drawing
- `draw_paths` - Draw multiple paths
- `draw_path` - Draw a simple path
- `draw_stroke` - Draw a stroke with orientation and pressure
- `draw_polygon` - Draw a polygon
- `draw_text` - Draw text
- `draw_svg_path` - Draw an SVG path

### 🖌️ Brush
- `brush_set_type` - Change brush type
- `brush_set_size` - Set brush size
- `brush_add_size` - Modify brush size
- `brush_set_path_smoothing` - Set smoothing
- `brush_move` - Move brush (absolute position)
- `brush_translate` - Move brush (relative)
- `brush_rotate` - Rotate brush (absolute)
- `brush_turn` - Rotate brush (relative)
- `brush_draw` - Draw a straight line

### 🎨 Color
- `color_set_rgb` - Set color in RGB
- `color_set_hsv` - Set color in HSV
- `color_set_html` - Set color with HTML/CSS
- `color_add_rgb` - Modify color (RGB)
- `color_add_hsv` - Modify color (HSV)

### 🧊 3D Models
- `model_import` - Import local model
- `model_web_import` - Import from URL
- `model_icosa_import` - Import from Icosa Gallery
- `model_select` - Select model
- `model_position` - Position model
- `model_rotation` - Rotate model
- `model_scale` - Scale model
- `model_delete` - Delete model

### 💾 Save/Load
- `save_overwrite` - Save (overwrite)
- `save_as` - Save as...
- `save_new` - New save
- `load_user` - Load user sketch
- `load_named` - Load by name
- `new_scene` - New scene

### 📷 Camera
- `camera_move` - Move camera (absolute)
- `camera_translate` - Move camera (relative)
- `camera_rotate` - Rotate camera (absolute)
- `camera_turn` - Rotate camera (relative)
- `spectator_move` - Move spectator view

### ✂️ Selection
- `selection_select_all` - Select all
- `selection_invert` - Invert selection
- `selection_delete` - Delete selection
- `selection_duplicate` - Duplicate selection

### 📑 Layers
- `layer_create` - Create layer
- `layer_set` - Set active layer
- `layer_show` - Show layer
- `layer_hide` - Hide layer

### 📐 Guides
- `guide_add` - Add guide (cube, sphere, etc.)
- `guide_position` - Position guide
- `guide_scale` - Scale guide

### 🔄 Symmetry
- `symmetry_mode` - Symmetry mode
- `symmetry_position` - Symmetry widget position

### 🔧 Utilities
- `undo` - Undo
- `redo` - Redo
- `show_help` - Show API help

## 💡 Usage Examples

Once the server is configured in Claude Desktop, you can give natural language instructions:

```
"Draw a red square of size 2 at position 0,0,0"
"Change brush to 'ink' and set color to blue"
"Create a 6-sided polygon with radius 3"
"Import the model 'Andy.glb' and position it at 1,2,3"
"Save the scene as 'my_creation'"
```

## 🔍 Testing the Server

To manually test the server:

```bash
python openbrush_mcp_server.py
```

The server should start and wait for commands on stdin/stdout according to the MCP protocol.

## 🛠️ Troubleshooting

### Open Brush API not accessible
- Check that Open Brush is running
- Check that HTTP API is enabled in settings
- Test manually: `http://localhost:40074/api/v1?help`

### MCP server not connecting
- Check the path in Claude Desktop configuration
- Check that Python is in PATH
- Check Claude Desktop logs

### Commands failing
- Check provided parameters
- Check Open Brush API documentation
- Check returned error messages

## 📖 Resources

- [Open Brush Documentation](https://docs.openbrush.app/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Complete Open Brush API](http://localhost:40074/help) (when Open Brush is running)

## 🔒 Security

⚠️ **Warning**: This server calls a local API. Make sure to:
- Not expose port 40074 on the internet
- Trust sent commands
- Backup your creations regularly

## 📝 License

This MCP server is provided as-is to facilitate Open Brush usage with LLMs.

## 🤝 Contribution

Feel free to:
- Report bugs
- Suggest improvements
- Add new tools for missing API commands

---

**Note**: Open Brush is an open-source fork of Google's Tilt Brush. This MCP server is not officially affiliated with Open Brush.

