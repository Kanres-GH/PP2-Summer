import pygame
import sys
from random import randint
FPS = 60
pygame.init()
pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()
 
# если надо до цикла отобразить
# какие-то объекты, обновляем экран
pygame.display.update()
 
# главный цикл
while True:
    pygame.display.set_caption(str(randint(1000,9999)))
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()