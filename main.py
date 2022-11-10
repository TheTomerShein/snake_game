import threading
import time

import schedule as schedule

import Candy
import SnakeBoard
import Player
import pygame


def food_collision(p: Player, c: Candy):
    if p.index_x == c.index_x and p.index_y == c.index_y:
        return True
    return False


if __name__ == '__main__':
    pygame.init()

    MATRIX = 20
    SCREEN_HEIGHT, SCREEN_WIDTH = 700, 700

    sx, sy = int(SCREEN_WIDTH / MATRIX), int(SCREEN_HEIGHT / MATRIX)
    max_w = (SCREEN_WIDTH + sx - 1) // sx
    max_h = (SCREEN_HEIGHT + sy - 1) // sy

    board = SnakeBoard.SnakeBoard('Snake By Tomer Shein', width=SCREEN_WIDTH, height=SCREEN_HEIGHT, sx=sx, sy=sy)
    board.build_screen()

    player = Player.Player(board.screen_pointer, max_w=max_w, max_h=max_h, sx=sx, sy=sy)

    clock = pygame.time.Clock()

    candy = Candy.Candy(board.screen_pointer, max_w=max_w, max_h=max_h, sx=sx, sy=sy)

    schedule.every(0.7).seconds.do(candy.animate)

    # t = threading.Thread(target=player.handle_head_and_body_collision, daemon=True)
    # t.start()

    while True:
        clock.tick(9)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        board.building_net()
        player.handle_keys()
        player.draw(board.screen_pointer)
        candy.draw(board.screen_pointer)
        schedule.run_pending()

        if player.handle_touching_limits() or player.handle_head_and_body_collision():
            pygame.quit()
            quit()

        if food_collision(player, candy):
            candy.kill()
            candy.respawn(board.screen_pointer, player)
            player.increase_body()

        pygame.display.update()
