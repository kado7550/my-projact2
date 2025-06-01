import pygame
import sys
import numpy as np

# 설정
BOARD_SIZE = 15
CELL_SIZE = 40
MARGIN = 60
SCREEN_SIZE = BOARD_SIZE * CELL_SIZE + MARGIN * 2
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WOOD = (222, 184, 135)

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))
pygame.display.set_caption("오목 게임 - Pygame")
font = pygame.font.SysFont(None, 36)

# 게임 상태
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
turn = 1  # 1: 흑, 2: 백
winner = 0

def draw_board():
    screen.fill(WOOD)
    
    # 격자선 그리기
    for i in range(BOARD_SIZE):
        pygame.draw.line(screen, BLACK, 
                         (MARGIN, MARGIN + i * CELL_SIZE),
                         (SCREEN_SIZE - MARGIN, MARGIN + i * CELL_SIZE), 1)
        pygame.draw.line(screen, BLACK, 
                         (MARGIN + i * CELL_SIZE, MARGIN),
                         (MARGIN + i * CELL_SIZE, SCREEN_SIZE - MARGIN), 1)

    # 별점 (천원 포함)
    star_points = [(3, 3), (3, 11), (7, 7), (11, 3), (11, 11)]
    for x, y in star_points:
        px = MARGIN + x * CELL_SIZE
        py = MARGIN + y * CELL_SIZE
        pygame.draw.circle(screen, BLACK, (px, py), 4)

def draw_stones():
    for x in range(BOARD_SIZE):
        for y in range(BOARD_SIZE):
            if board[x, y] == 1:  # 흑
                color = BLACK
            elif board[x, y] == 2:  # 백
                color = WHITE
            else:
                continue
            px = MARGIN + x * CELL_SIZE
            py = MARGIN + y * CELL_SIZE
            pygame.draw.circle(screen, color, (px, py), 16)
            pygame.draw.circle(screen, BLACK, (px, py), 16, 1)

def check_winner(x, y):
    player = board[x, y]
    directions = [(1, 0), (0, 1), (1, 1), (1, -1)]

    for dx, dy in directions:
        count = 1
        for dir in [1, -1]:
            nx, ny = x, y
            while True:
                nx += dx * dir
                ny += dy * dir
                if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[nx, ny] == player:
                    count += 1
                else:
                    break
        if count >= 5:
            return player
    return 0

def get_board_pos(mouse_pos):
    mx, my = mouse_pos
    if not (MARGIN <= mx < SCREEN_SIZE - MARGIN and MARGIN <= my < SCREEN_SIZE - MARGIN):
        return None
    x = int(round((mx - MARGIN) / CELL_SIZE))
    y = int(round((my - MARGIN) / CELL_SIZE))
    return x, y

def show_winner(winner):
    msg = "흑(●) 승리!" if winner == 1 else "백(○) 승리!"
    text = font.render(msg, True, BLACK)
    screen.blit(text, (SCREEN_SIZE // 2 - 80, 20))

# 게임 루프
running = True
while running:
    draw_board()
    draw_stones()
    if winner:
        show_winner(winner)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and winner == 0:
            pos = get_board_pos(pygame.mouse.get_pos())
            if pos:
                x, y = pos
                if board[x, y] == 0:
                    board[x, y] = turn
                    winner = check_winner(x, y)
                    if not winner:
                        turn = 2 if turn == 1 else 1

pygame.quit()
sys.exit()
