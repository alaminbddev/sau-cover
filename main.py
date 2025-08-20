from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps
import random
import math
import numpy as np

# Create a premium image with dark elegant background
width, height = 1200, 1200
image = Image.new("RGB", (width, height), (10, 15, 25))  # Deep blue-black background
draw = ImageDraw.Draw(image)

# Generate a starry background effect
for _ in range(1000):
    x = random.randint(0, width-1)
    y = random.randint(0, height-1)
    brightness = random.randint(100, 255)
    size = random.randint(1, 2)
    draw.ellipse((x, y, x+size, y+size), fill=(brightness, brightness, brightness))

# Add a subtle gradient overlay for depth
for y in range(height):
    gradient = int(30 * (y / height))
    draw.line((0, y, width, y), fill=(10+gradient, 15+gradient, 25+gradient))

# Sample names for circular arrangement
names = ["Alen", "Jui", "Rahim", "Karim", "Sadia", "Tania", "Fahim", "Nadia", "Sakib", "Rima",
         "Alex", "Maria", "David", "Sophia", "James", "Emma", "John", "Olivia", "Robert", "Ava",
         "Liam", "Noah", "Oliver", "Elijah", "William", "Benjamin", "Lucas", "Henry", "Alexander"]

# Function to draw text along a circular path
def draw_circular_text(draw, center_x, center_y, radius, text, font, fill=(200, 200, 200), angle_offset=0, reverse=False):
    # Split text into characters
    chars = list(text)
    # Calculate the angle for each character
    angle_step = 360 / len(chars)
    
    for i, char in enumerate(chars):
        # Calculate angle in radians
        if reverse:
            angle = math.radians(angle_offset - i * angle_step)
        else:
            angle = math.radians(angle_offset + i * angle_step)
        
        # Calculate position
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # Draw the character
        draw.text((x, y), char, fill=fill, font=font, anchor="mm")

# Draw main department text in circular arrangements
center_x, center_y = width // 2, height // 2

# Draw "DEPARTMENT OF" in inner circle
draw_circular_text(draw, center_x, center_y, 180, "DEPARTMENT OF", 
                  ImageFont.load_default(), fill=(220, 180, 60), angle_offset=90)

# Draw "MATHEMATICS" in middle circle
draw_circular_text(draw, center_x, center_y, 250, "MATHEMATICS", 
                  ImageFont.load_default(), fill=(220, 200, 100), angle_offset=90, reverse=True)

# Draw "UNIVERSITY OF RAJSHAHI" in outer circle
draw_circular_text(draw, center_x, center_y, 320, "UNIVERSITY OF RAJSHAHI", 
                  ImageFont.load_default(), fill=(180, 180, 220), angle_offset=90)

# Draw batch information in the center
draw.text((center_x, center_y-20), "BATCH", fill=(255, 255, 255), font=ImageFont.load_default(), anchor="mm")
draw.text((center_x, center_y+20), "∞ - 68", fill=(255, 215, 0), font=ImageFont.load_default(), anchor="mm")

# Draw names in multiple circular arrangements with different styles
for i in range(4):
    radius = 380 + i * 70
    # Select a subset of names for this circle
    circle_names = names[i*7:(i+1)*7]
    
    # Draw names in a circle with alternating colors
    for j, name in enumerate(circle_names):
        angle = math.radians(j * (360 / len(circle_names)))
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        
        # Create a color gradient based on position
        r = int(150 + 100 * math.cos(angle))
        g = int(150 + 100 * math.sin(angle))
        b = int(200 - 100 * math.cos(angle))
        
        # Draw the name with a slight shadow effect
        draw.text((x+1, y+1), name.upper(), fill=(r//3, g//3, b//3), font=ImageFont.load_default(), anchor="mm")
        draw.text((x, y), name.upper(), fill=(r, g, b), font=ImageFont.load_default(), anchor="mm")

# Add decorative mathematical elements
# Draw golden ratio spiral
def draw_golden_spiral(draw, center_x, center_y, max_radius):
    a = 5  # Start radius
    b = 0.2  # Growth factor
    
    points = []
    for angle in range(0, 1080, 5):  # 3 full rotations
        rad = math.radians(angle)
        r = a * math.exp(b * rad)
        x = center_x + r * math.cos(rad)
        y = center_y + r * math.sin(rad)
        points.append((x, y))
    
    # Draw the spiral
    if len(points) > 1:
        draw.line(points, fill=(180, 160, 50), width=2)

draw_golden_spiral(draw, center_x, center_y, 350)

# Draw mathematical symbols in decorative pattern
symbols = ["∞", "π", "∑", "∫", "√", "Δ", "∇", "∂", "±", "≈", "≠", "≡", "∈", "∀", "∃", "∴", "α", "β", "γ", "θ", "σ", "μ", "λ", "ω"]
for i in range(150):
    symbol = random.choice(symbols)
    angle = math.radians(random.randint(0, 360))
    distance = random.randint(400, 550)
    x = center_x + distance * math.cos(angle)
    y = center_y + distance * math.sin(angle)
    size = random.randint(15, 25)
    
    # Vary opacity based on distance from center
    alpha = random.randint(80, 180)
    color = (random.randint(150, 220), random.randint(150, 220), random.randint(150, 220))
    
    draw.text((x, y), symbol, fill=color, font=ImageFont.load_default())

# Add geometric shapes for visual interest
# Draw concentric circles
for r in range(100, 600, 50):
    draw.ellipse((center_x - r, center_y - r, center_x + r, center_y + r), 
                 outline=(40, 50, 70), width=1)

# Draw radial lines
for i in range(0, 360, 30):
    angle = math.radians(i)
    x1 = center_x + 100 * math.cos(angle)
    y1 = center_y + 100 * math.sin(angle)
    x2 = center_x + 550 * math.cos(angle)
    y2 = center_y + 550 * math.sin(angle)
    draw.line((x1, y1, x2, y2), fill=(40, 50, 70), width=1)

# Apply premium visual effects
# Add a subtle glow effect by creating a blurred version and overlaying it
blurred = image.filter(ImageFilter.GaussianBlur(radius=3))
image = Image.blend(image, blurred, alpha=0.2)

# Apply emboss effect for depth
image = image.filter(ImageFilter.EMBOSS)

# Enhance contrast
enhancer = ImageEnhance.Contrast(image)
image = enhancer.enhance(1.2)

# Enhance color saturation
enhancer = ImageEnhance.Color(image)
image = enhancer.enhance(1.3)

# Add a vignette effect (darken edges)
vignette = Image.new("RGB", (width, height), (0, 0, 0))
mask = Image.new("L", (width, height), 0)
mask_draw = ImageDraw.Draw(mask)
mask_draw.ellipse((center_x-700, center_y-700, center_x+700, center_y+700), fill=255)
mask = mask.filter(ImageFilter.GaussianBlur(radius=350))
image = Image.composite(image, vignette, mask)

# Add a subtle film grain effect for premium texture
noise = Image.effect_noise((width, height), random.randint(20, 40))
image = Image.blend(image, noise, alpha=0.03)

# Add a border
border_width = 20
image = ImageOps.expand(image, border=border_width, fill=(30, 35, 45))
draw = ImageDraw.Draw(image)
draw.rectangle((border_width, border_width, width+border_width-1, height+border_width-1), 
               outline=(80, 90, 110), width=2)

# Final sharpening
image = image.filter(ImageFilter.SHARPEN)

# Show the premium circular text design
image.show()
