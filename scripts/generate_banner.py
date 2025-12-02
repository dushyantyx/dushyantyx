import os
from PIL import Image, ImageDraw, ImageFont

# Make sure output folder exists
os.makedirs("output", exist_ok=True)

# Create frames for a simple moving text animation
frames = []
for i in range(10):
    img = Image.new('RGB', (800, 200), color=(0, 0, 0))  # black background
    d = ImageDraw.Draw(img)
    font = ImageFont.load_default()
    x = 50 + i*10  # move text to the right
    d.text((x, 80), "☁️ Dushyant | Akatsuki Code Ninja ☁️", fill=(255,0,0), font=font)
    frames.append(img)

# Save as animated GIF
frames[0].save("output/akatsuki_banner.gif", save_all=True, append_images=frames[1:], duration=200, loop=0)
