from PIL import ImageDraw, Image
from random import choice


def makeanaglif(filename, delta):
    image = Image.open(filename)
    x, y = image.size
    res_picture = Image.new('RGB', (x, y), (0, 0, 0))
    draw = ImageDraw.Draw(res_picture)
    pixels2 = res_picture.load()
    pixels = image.load()
    r_im = Image.new('RGB', (x, y), (0, 0, 0))
    gb_im = Image.new('RGB', (x, y), (0, 0, 0))
    r_pix = r_im.load()
    gb_pix = gb_im.load()
    for i in range(x):
        for j in range(y):
            if pixels[i, j][0] > pixels[i, j][1] and pixels[i, j][0] > pixels[i, j][2]:  # если преобладает красный цвет
                r_pix[i, j] = pixels[i, j]
                gb_pix[i, j] = 255, 255, 255
            else:
                gb_pix[i, j] = pixels[i, j]
                r_pix[i, j] = 255, 255, 255

    for i in range(x + delta):
        for j in range(y):
            if r_pix[i, j] != (255, 255, 255):
                r = r_pix[i + delta, j][0]
                g = r_pix[i + delta, j][1]
                b = r_pix[i + delta, j][2]
            else:
                r = gb_pix[i, j][0]
                g = gb_pix[i, j][1]
                b = gb_pix[i, j][2]
            if r == (0 or 255) and g == (0 or 255) and b == (0 or 255):
                # pass
                r = choice((pixels2[i - 1, j][0], pixels2[i - 1, j - 1][0], pixels2[i, j - 1][0]))
                g = choice((pixels2[i - 1, j][1], pixels2[i - 1, j - 1][1], pixels2[i, j - 1][1]))
                b = choice((pixels2[i - 1, j][2], pixels2[i - 1, j - 1][2], pixels2[i, j - 1][2]))
            draw.point((i, j), (r, g, b))

    r_im.save('red.png', "PNG")
    gb_im.save('gb.png', "PNG")
    res_picture.save('anaglif.png', "PNG")


makeanaglif('anaglyph031.jpg', -47)
