from PIL import ImageDraw, Image
import random


def image_filter_noise(pixel, i, j):
    """Добавление шумов на изображение"""
    r, g, b = 0, 0, 0
    for y in range(j):
        for x in range(i):
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if r > 64:
                r -= random.randint(0, 64)
            if g > 64:
                g -= random.randint(0, 64)
            if b > 64:
                b -= random.randint(0, 64)
            return r, g, b


def image_filter_bright(pixel, i, j, value=random.randint(0, 64)):
    """Увеличение яркости на изображении"""
    r, g, b = 0, 0, 0
    for y in range(j):
        for x in range(i):
            r = pixel[0] + value
            g = pixel[1] + value
            b = pixel[2] + value
            return r, g, b


def image_filter_dark(pixel, i, j, value=random.randint(0, 64)):
    """Затемнение изображения"""
    r, g, b = 0, 0, 0
    for y in range(j):
        for x in range(i):
            r = pixel[0] - value
            g = pixel[1] - value
            b = pixel[2] - value
            return r, g, b


def image_filter_warm(pixel, i, j, value=random.randint(0, 32)):
    """Добавляем тепло на фото"""
    r, g, b = 0, 0, 0
    for y in range(j):
        for x in range(i):
            r = pixel[0] + value
            g = pixel[1] + value
            b = pixel[2]
            return r, g, b


def image_filter_cold(pixel, i, j, value=random.randint(0, 32)):
    """Делаем фото более холодным"""
    r, g, b = 0, 0, 0
    for y in range(j):
        for x in range(i):
            r = pixel[0]
            g = pixel[1] + value
            b = pixel[2] + value
            return r, g, b


def image_filter_grey(pixel, i, j):
    """Создание фото в градациях серого"""
    r, g, b = 0, 0, 0
    for y in range(j):
        for x in range(i):
            r = (pixel[0] + pixel[1] + pixel[2]) / 3
            g = (pixel[0] + pixel[1] + pixel[2]) / 3
            b = (pixel[0] + pixel[1] + pixel[2]) / 3
            return int(r), int(g), int(b)


def image_filter_contrast(pixel, i, j, value=15):
    """Создание контраста на изображении"""
    white = (255, 255, 255)
    black = (0, 0, 0)
    # r, g, b = 0, 0, 0
    for y in range(j):
        for x in range(i):
            sr_w = int(abs(255 - sum(pixel)/3))
            sr_b = int(abs(0 - sum(pixel) / 3))
            if sr_w <= sr_b:
                return image_filter_bright(pixel, i, j, value)
            else:
                return image_filter_dark(pixel, i, j, value)


def make_new_picture(filename):
    image = Image.open(filename)
    x, y = image.size
    res_picture = Image.new('RGB', (x, y), (0, 0, 0))
    pixels = image.load()
    pixels2 = res_picture.load()
    value = random.randint(1, 16)
    for i in range(x):
        for j in range(y):
            # pixels2[i, j] = image_filter_noise(pixels[i, j], x, y)
            # pixels2[i, j] = image_filter_bright(pixels[i, j], x, y, 30)
            # pixels2[i, j] = image_filter_bright(pixels[i, j], x, y)
            # pixels2[i, j] = image_filter_warm(pixels[i, j], x, y)
            # pixels2[i, j] = image_filter_cold(pixels[i, j], x, y)
            # pixels2[i, j] = image_filter_grey(pixels[i, j], x, y)
            #pixels2[i, j] = image_filter_dark(pixels[i, j], x, y)
            pixels2[i, j] = image_filter_contrast(pixels[i, j], x, y, value)

    res_picture.save('res_filter.png', "PNG")


make_new_picture('anaglyph031.jpg')
