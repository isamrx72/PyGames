""" draw_rect1.py """
import sys
import pygame
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((400, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255, 255, 255))

        # 赤：矩形（塗りつぶし）
        pygame.draw.rect(SURFACE, (255, 0, 0), (20, 20, 100, 50))

        # 赤：矩形（太さ3）
        pygame.draw.rect(SURFACE, (255, 0, 0), (200, 150, 150, 30), 3)

        # 緑：矩形
        pygame.draw.rect(SURFACE, (0, 255, 0), ((20, 100), (100, 50)))

        # 青：矩形、Rectオブジェクト
        rect0 = Rect(200, 60, 150, 80)
        pygame.draw.rect(SURFACE, (0, 0, 255), rect0)

        # 黄：矩形、Rectオブジェクト
        rect1 = Rect((20, 180), (100, 50))
        pygame.draw.rect(SURFACE, (255, 255, 0), rect1)

        pygame.display.update()
        FPSCLOCK.tick(3)

if __name__ == '__main__':
    main()
