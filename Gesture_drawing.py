import pyglet
import os
import sys
import random


images_path, seconds = sys.argv[1:]
seconds = int(seconds)


window = pyglet.window.Window(resizable=True)
image = None  # image is a sprite
image_aspect = 1.0


def walker(walker_path):
    files = os.listdir(walker_path)
    image_files = []
    for f in files:
        if '.jpg' in f.lower() or '.png' in f.lower() or '.jpeg' in f.lower():
            image_files.append(os.path.join(walker_path, f))
    return image_files


def load_image(path):
    image = pyglet.image.load(path)
    image = pyglet.sprite.Sprite(img=image)
    image_aspect = float(image.width)/image.height
    return (image, image_aspect)


def recalc_size():
    global image
    global image_aspect
    w, h = window.get_size()

    if image_aspect >= 1.0: A = {'x': 1.0, 'y': 1.0 / image_aspect}
    if image_aspect <  1.0: A = {'x': image_aspect, 'y': 1.0}

    fillX = w / A['x']
    fillY = h / A['y']

    if fillX <= fillY:
        image.width = w
        image.height = w * (1.0 / image_aspect)
    if fillY < fillX:
        image.height = h
        image.width = h * image_aspect

    # center 
    offset_width = (w - image.width + 0.001) / 2.0
    offset_height = (h - image.height + 0.001) / 2.0
    image.x = offset_width
    image.y = offset_height


@window.event
def on_draw():
    window.clear()

    recalc_size()

    global image
    image.draw()


image_files = walker(images_path)

def choose_image(dt):
    chosen = random.choice(image_files)
    global image
    global image_aspect
    im, imas = load_image(chosen)
    image = im
    image_aspect = imas

choose_image(0)
pyglet.clock.schedule_interval(choose_image, seconds)   # called twice a second

pyglet.app.run()
