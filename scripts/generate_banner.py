from PIL import Image, ImageDraw, ImageFont

# Create a simple red cloud banner
img = Image.new('RGB', (800, 200), color='black')
d = ImageDraw.Draw(img)
font = ImageFont.load_default()
d.text((50, 80), "☁️ Dushyant | Akatsuki Code Ninja ☁️", fill=(255,0,0), font=font)

img.save("output/akatsuki_banner.gif")
