"""
import pygame
pygame.display.set_mode((600, 400))

При запуске программа создаёт и сразу же закрывает окно размером 600 x 400 пикселей.
Чтобы окно не закрывалось, можно сделать так:

import pygame as pg
pg.display.set_mode((600, 400))         #   НО таким образом программа зависнет. Окно будет создано, но его никак не получится закрыть.
                                        #   Программу придётся завершить через терминал или закрыть окно через диспетчер задач.
while 1:
    pass

Чтобы окно могло закрываться, можно сделать так:

import pygame as pg
pg.display.set_mode((600, 400))
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()

Окно закроется, но с ошибкой. Почему? Потому что pygame.quit() отключает (деинициализирует) pygame,
но не завершает работу программы. Таким образом, после выполнения этой функции отключаются модули библиотеки pygame,
но выхода из цикла и программы не происходит. Программа продолжает работу и переходит к следующей итерации
цикла while (или продолжает выполнять тело данной итерации, если оно еще не закончилось).

В данном случае происходит переход к следующей итерации цикла while.
И здесь выполнить функцию get() модуля event оказывается уже невозможным.
Возникает исключение и программа завершается. По-сути программу завершает не функция pygame.quit(),
а выброшенное, но не обработанное, исключение.

Эту проблему можно решить через sys.exit():

import pygame as pg
import sys
pg.display.set_mode((600, 400))
while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            pg.quit()       # Сначала отключается pygame    (Не обязательно для завершения программы)
            sys.exit()      # Затем происходит выход из программы   (Если оставить только sys.exit(), то автоматически выключится и pygame)

Другой вариант – не допустить следующей итерации цикла. Для этого потребуется дополнительная переменная:

import pygame as pg
pg.display.set_mode((600, 400))
play = True
while play:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            play = False

В этом случае завершится текущая итерация цикла, но новая уже не начнется.
Если в основной ветке ниже по течению нет другого кода, программа завершит свою работу.

Нередко код основной ветки программы помещают в функцию, например, main().
Она выполняется, если файл запускается как скрипт, а не импортируется как модуль.
В этом случае для завершения программы проще использовать оператор return, который осуществляет выход из функции:

import pygame as pg
def main():
    pg.display.set_mode((600, 400))
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                return
if __name__ == "__main__":
    main()
"""
