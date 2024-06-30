from PIL import Image, ImageDraw, ImageFont

# Create a new image with a white background
image = Image.new('RGB', (200, 100), color='white')

# Load a font
font = ImageFont.truetype('arial.ttf', size=36)

# Initialize ImageDraw object
draw = ImageDraw.Draw(image)

# Add text
text = "Sunset"
text_width, text_height = draw.textsize(text, font=font)
x = (image.width - text_width) // 2
y = (image.height - text_height) // 2
draw.text((x, y), text, font=font, fill='black')

# Save image
image.save('SunsetWebsite/images/sunset_logo.png')
