import os
from PIL import Image, ImageDraw, ImageFont

# Ensure output folder exists
os.makedirs("output", exist_ok=True)

# GIF parameters
width, height = 800, 200
frames = []
num_frames = 20
text = "☁️ Dushyant | Akatsuki Code Ninja ☁️"

# Load default font
font = ImageFont.load_default()

for i in range(num_frames):
    img = Image.new("RGB", (width, height), color=(0, 0, 0))  # black background
    draw = ImageDraw.Draw(img)
    
    # Draw moving red clouds (simplified ellipses)
    for j in range(5):
        cloud_x = (j*150 - i*10) % width  # move clouds left
        cloud_y = 50 + (j%2)*30
        draw.ellipse([cloud_x, cloud_y, cloud_x+100, cloud_y+50], fill=(200,0,0))  # Akatsuki red
    
    # Draw moving text
    text_x = 50 + i*10
    text_y = 140
    draw.text((text_x, text_y), text, font=font, fill=(255,0,0))
    
    frames.append(img)

# Save GIF
frames[0].save(
    "output/akatsuki_banner.gif",
    save_all=True,
    append_images=frames[1:],
    duration=150,
    loop=0
)
