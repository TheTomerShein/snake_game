import random
import pygame


class SnakeBoard:
    def __init__(self, name, height, width, sx, sy):
        self.screen_pointer = None
        self.board_name = name
        self.width = width
        self.height = height
        self.sx = sx
        self.sy = sy

    def build_screen(self):
        self.screen_pointer = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.board_name)

        LIGHT_GREEN = (144, 238, 144)
        self.screen_pointer.fill(LIGHT_GREEN)

    def building_net(self):
        for i in range((self.width + self.sx - 1) // self.sx):
            for j in range((self.height + self.sy - 1) // self.sy):
                c = (154, 221, 125) if (i + j) % 2 == 0 else (165, 230, 137)
                pygame.draw.rect(self.screen_pointer, c, (i * self.sx, j * self.sy, self.sx, self.sy))
