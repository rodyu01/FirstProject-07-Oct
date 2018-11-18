from PIL import Image, ImageDraw
text = "vivat Wikipedia!!!"
color = (0, 0, 120)
img = Image.new('RGB', (500, 300), color)
imgDrawer = ImageDraw.Draw(img)
imgDrawer.text((100, 100), text)
img.save("c:\\temp\\pil-basic-example.png")
