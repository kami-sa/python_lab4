from PIL import ImageDraw, Image

# создание изображения
new_image = Image.new("RGB", (512, 200), (0, 0, 0))
draw = ImageDraw.Draw(new_image)
r, g, b = 0, 0, 0
for y in range(200):
    for x in range(512):
        draw.point((x, y), (r, g, b))
        r += 1
    r = 0
new_image.save('res.png', "PNG")
