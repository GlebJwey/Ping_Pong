from pygame import *

init()

okno_x = 1280
okno_y = 720

okno = display.set_mode((okno_x, okno_y))
display.set_caption('Пинг понг')

bg = image.load('D:/Пользователи/rigl3/Изображения/Материал для программирования/background.png')

clock = time.Clock()

FPS = 120
game = True
while game:

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()

    clock.tick(FPS)

quit()