# Open Brush Script Examples

This file contains example scripts that you can ask Claude to execute via the MCP server.

## 🌈 Example 1: Rainbow

"Create a rainbow with 7 arcs of different colors"

Steps:
1. Set brush to "ink" type with size 0.3
2. For each color (red, orange, yellow, green, blue, indigo, violet):
   - Change color
   - Draw an arc (polygon with many sides)
   - Move brush slightly

## 🏗️ Example 2: 3D Grid

"Create a 3D grid of 5x5x5 cubes"

Steps:
1. Add a cube guide at origin
2. For x from 0 to 4:
   - For y from 0 to 4:
     - For z from 0 to 4:
       - Duplicate the guide
       - Position at (x*2, y*2, z*2)

## ✍️ Example 3: Neon Text Effect

"Write 'HELLO' with a neon glowing effect"

Steps:
1. Change brush to "light" or "neon"
2. Set color to bright cyan
3. Set size to 1.0
4. Draw the text "HELLO"

## 🌸 Example 4: Geometric Flower

"Create a geometric flower with 12 petals"

Steps:
1. Set color to pink
2. Position brush at center (0, 0, 0)
3. For i from 0 to 11:
   - Draw a 4-sided polygon (diamond)
   - Rotate brush 30 degrees around Y
   - Repeat

## 🌀 Example 5: Ascending Spiral

"Draw a spiral that goes up to the sky"

Steps:
1. Set brush to "ink", blue color
2. Starting position: (0, 0, 0)
3. For 100 iterations:
   - Enable forced drawing
   - Translate (0.1, 0.05, 0) - advance and go up
   - Rotate 10 degrees around Y
   - Draw a small line

## 🎯 Example 6: Concentric Target

"Create a target with concentric circles of alternating colors"

Steps:
1. For radius from 5 to 1 (decreasing by 1):
   - Alternate color between red and white
   - Draw a 32-sided polygon (circle)
   - Change brush size

## 🏛️ Example 7: Temple with Columns

"Build a Greek temple with 6 columns"

Steps:
1. Create floor: flat rectangle
2. For each column (6 spaced columns):
   - Import a capsule guide
   - Position vertically
   - Stretch in height (scale)
3. Create roof: large rectangle above

## 🎨 Example 8: Color Palette

"Create a palette showing all primary and secondary colors"

Steps:
1. Define colors: red, yellow, blue, green, orange, purple
2. For each color, at spaced positions:
   - Change color
   - Draw a square (4-sided polygon)

## 🌳 Example 9: Simple Fractal Tree

"Draw a fractal tree with 3 levels"

Steps:
1. Recursive branch function:
   - Draw a line (trunk)
   - If level > 0:
     - Rotate +30 degrees
     - Recursively call with level-1
     - Rotate -60 degrees
     - Recursively call with level-1
     - Rotate +30 degrees (reset)

## 🎪 Example 10: Solar System Scene

"Create a mini solar system with the Sun and 3 planets"

Steps:
1. Sun:
   - Yellow color, "fire" brush
   - Large sphere at center (sphere guide)
2. For each planet (3 planets):
   - Different color (blue, red, green)
   - Sphere guide of decreasing size
   - Position in orbit around sun
   - Increasing distance

## 📦 Example 11: Gift Box with Decoration

"Draw a gift box with a ribbon"

Steps:
1. Create a cube guide for the box
2. Red color for the ribbon
3. Draw two crossing lines on top
4. Add a knot (two loops) at center

## 🌊 Example 12: Ocean Waves

"Create stylized ocean waves"

Steps:
1. "ink" brush light blue
2. For 5 waves:
   - Draw a sinusoidal curve (SVG path or points)
   - Slightly different Y position
   - Variable transparency

## 💫 Example 13: Star Constellation

"Draw a constellation with 10 connected stars"

Steps:
1. Create 10 random points in space
2. Draw small stars (5-pointed polygons) at each point
3. Connect certain stars with thin lines

## 🏰 Example 14: Simple Castle

"Build a castle with 4 corner towers"

Steps:
1. Walls: 4 cube guides for walls
2. Towers: 4 cylinder guides at corners
3. Battlements: small cubes on top of walls
4. Door: horizontal capsule guide at center

## 🎼 Example 15: Musical Staff with Notes

"Draw a musical staff with some notes"

Steps:
1. Draw 5 parallel horizontal lines (staff)
2. Add a treble clef (SVG path or manual drawing)
3. Place notes (ellipses) on the staff

---

## 💡 Tips for creating your own scripts

1. **Plan first**: Break down your idea into simple steps
2. **Use coordinates**: Understand the system (Y up)
3. **Test gradually**: Create step by step
4. **Save regularly**: Use `save_as` often
5. **Experiment**: Try different brushes and colors
6. **Combine guides**: Mix cubes, spheres, capsules
7. **Use symmetry**: For repetitive patterns
8. **Think in 3D**: Don't forget the Z axis!

---

## 🎯 Example requests to make to Claude

Here's how to phrase your requests:

### Simple
"Draw a red cube of size 2"

### Medium
"Create a pyramid by stacking 4 levels of cubes, each level smaller"

### Advanced
"Generate a symmetrical mandala with 8 axes of symmetry, using polygons of different sizes and alternating colors"

### Very Advanced
"Create a miniature city scene with 10 buildings of variable heights, roads between them, and some trees (green capsule guides)"

---

**Tip**: The more precise you are in your request, the better the result!
