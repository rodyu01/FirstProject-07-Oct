from PIL import Image, ImageDraw
text = "Hello, PIL!!!"
color = (0, 0, 120)
img = Image.new('RGB', (100, 50), color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((10, 20), text)
img.save("pil-basic-example.png")