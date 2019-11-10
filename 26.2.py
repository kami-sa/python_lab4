from PIL import ImageDraw, Image


# создание изображения
def board(value, size):
    new_image = Image.new("RGB", (value * size, value * size), (255, 255, 255))
    draw = ImageDraw.Draw(new_image)
    flag = 0
    x, y = 0, 0
    while y != size*value:
        while x != size*value:
            if flag:
                r, g, b = 255, 255, 255
                print('рисуем белый')
            else:
                r, g, b = 0, 0, 0
                print('рисуем черный')
            draw.rectangle((x, y, x+size, y+size), fill=(r, g, b), width=50)
            flag = not flag
            x += size
        x = 0
        y += size
        flag = not flag
    new_image.save('res1.png', "PNG")


board(8, 50)
