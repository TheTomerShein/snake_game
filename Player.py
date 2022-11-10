import random
import pygame


class Player:
    def __init__(self, screen, max_w, max_h, sx, sy):
        self.sx = sx
        self.sy = sy
        self.max_w = max_w
        self.max_h = max_h
        self.color = (100, 100, 100)
        self.index_x = random.randint(0, self.max_w - 1)
        self.index_y = random.randint(0, self.max_h - 1)
        self.sticky_note = None
        print("player - ", self.index_x, self.index_y)
        self.player_rect = pygame.draw.rect(screen, self.color,
                                            (self.index_x * self.sx,
                                             self.index_y * self.sy,
                                             self.sx,
                                             self.sy), 0)
        self.body = [(self.index_x * self.sx, self.index_y * self.sy)]
        self.last_move = []

    def draw(self, screen):
        for x, y in self.body:
            pygame.draw.rect(screen, self.color,
                             (x, y,
                              self.sx,
                              self.sy), 0)

    def handle_head_and_body_collision(self):
        return self.body[0] in self.body[1:]

    def handle_touching_limits(self):
        if self.index_x >= self.max_w or self.index_x < 0 or self.index_y >= self.max_h or self.index_y < 0:
            return True
        return False

    def handle_keys(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.sticky_note != 'right':
            self.index_x -= 1
            self.sticky_note = 'left'
        elif key[pygame.K_RIGHT] and self.sticky_note != 'left':
            self.index_x += 1
            self.sticky_note = 'right'
        elif key[pygame.K_UP] and self.sticky_note != 'down':
            self.index_y -= 1
            self.sticky_note = 'up'
        elif key[pygame.K_DOWN] and self.sticky_note != 'up':
            self.index_y += 1
            self.sticky_note = 'down'
        elif self.sticky_note == 'right':
            self.index_x += 1
        elif self.sticky_note == 'left':
            self.index_x -= 1
        elif self.sticky_note == 'up':
            self.index_y -= 1
        elif self.sticky_note == 'down':
            self.index_y += 1

        self.body.pop()
        self.body.insert(0, (self.index_x * self.sx, self.index_y * self.sy))

    def increase_body(self):
        self.body.append(self.body[-1])
