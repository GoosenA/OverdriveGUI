import pygame
import utils
import os

from utils import SurfaceObject
from pathlib import Path

BLACK = (0,0,0)
WHITE = (255,255,255)
PLAYER = (0,255,0)
OPPONENT = (255,0,0)
GREY = (150,150,150)
MUD = (128,120,98)
OIL = (66,66,66)
PU_BOOST = (12,188,194)
PU_OIL = (13,19,189)

WIDTH = 30
HEIGHT = 20
MARGIN = 5
ROWS = 15
COLUMNS = 26
WINDOW_SIZE = [1000,800]

grid = []

for row in range(ROWS):
    grid.append([])
    for column in range(COLUMNS):
        grid[row].append(0)


pygame.init()

screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption("Array backed grid")
FONT_SIZE = 15
FONT = pygame.font.SysFont('freesans', FONT_SIZE)
done = False

clock = pygame.time.Clock()
config = utils.read_config()

round = 1
user_exit = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            user_exit = True

    print(f'ROUND: {round}')
    f = Path(config["FolderPrepend"]+"/Round "+utils.get_round_as_string(round))/config["GlobalState"]
    if round > 0 and not f.exists():
        print("File not found")
        done = True
        break

    try:
        player, opponent = utils.read_json(round, config)
    except Exception as e:
        done = True
        print("Exception while reading game state file.")
        print(e)
        break

    player_world = player["worldMap"]
    opponent_world = opponent["worldMap"]

    grid, offset, opponent_offset = utils.populate_grid(grid, player_world, opponent_world)

    screen.fill(BLACK)
    # Draw the grid
    for row in range(ROWS):
        for column in range(COLUMNS):
            color = WHITE

            if row == 0 or row == 8:
                color = BLACK
            if row == 1 or row == 9:
                color = GREY
            if row == 2 or row == 7 or row == 10:
                color = BLACK
            if grid[row][column] == SurfaceObject.PLAYER:
                color = PLAYER
            if grid[row][column] == SurfaceObject.OPPONENT:
                color = OPPONENT
            if grid[row][column]  == SurfaceObject.MUD:
                color = MUD
            if grid[row][column]  == SurfaceObject.OIL_SPILL:
                color = OIL
            if grid[row][column]  == SurfaceObject.BOOST:
                color = PU_BOOST
            if grid[row][column]  == SurfaceObject.OIL_POWER:
                color = PU_OIL
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            if row == 2:
                cellSurf = FONT.render(f'{offset+column}', True, BLACK)
                cellRect = cellSurf.get_rect()
                cellRect.topleft = ( column*(MARGIN+WIDTH)+MARGIN, row*(HEIGHT-1)-MARGIN)
                screen.blit(cellSurf, cellRect)

            if row == 12:
                cellSurf = FONT.render(f'{opponent_offset+column}', True, BLACK)
                cellRect = cellSurf.get_rect()
                cellRect.topleft = ( column*(MARGIN+WIDTH)+MARGIN, row*(HEIGHT)-MARGIN)
                screen.blit(cellSurf, cellRect)

    utils.display_text(screen, FONT, config, player, opponent, WHITE)

    # Limit to 60 frames per second
    clock.tick(config["game_speed"])

    pygame.display.update()
    round += 1

running = True
if user_exit == True:
    running = False
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()