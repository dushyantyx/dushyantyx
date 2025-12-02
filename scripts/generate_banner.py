import os
from PIL import Image, ImageDraw, ImageFont

# Create output folder if it doesn't exist
os.makedirs("output", exist_ok=True)

# GIF settings
width, height = 800, 200
frames = []
num_frames = 40
text = "☁️ Dushyant | Akatsuki Code Ninja ☁️"

# Load font (default)
font = ImageFont.load_default()

# Kunai positions for multiple kunai flying
kunai_positions = [(i*20 % width, 20 + (i%3)*30) for i in range(5)]

for i in range(num_frames):
    img = Image.new("RGB", (width, height), color=(0, 0, 0))  # black bg
    draw = ImageDraw.Draw(img)
    
    # Red clouds sliding left
    for j in range(6):
        cloud_x = (j*150 - i*7) % width
        cloud_y = 50 + (j%2)*30
        draw.ellipse([cloud_x, cloud_y, cloud_x+120, cloud_y+60], fill=(200,0,0))
    
    # Text pulsing and sliding
    pulse = int(200 * (0.5 + 0.5*((i%10)/10))) + 55  # 55-255
    text_x = -200 + i*15  # slide in from left
    text_y = 140
    draw.text((text_x, text_y), text, font=font, fill=(pulse,0,0))
    
    # Multiple Kunai flying across
    for k, (kx, ky) in enumerate(kunai_positions):
        kunai_x = (kx + i*12 + k*50) % width
        draw.text((kunai_x, ky), "🗡️", font=font, fill=(255,255,255))
    
    frames.append(img)

# Save animated GIF
frames[0].save(
    "output/akatsuki_banner.gif",
    save_all=True,
    append_images=frames[1:],
    duration=100,
    loop=0
)
