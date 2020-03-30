import pygame
import json
import enum

class SurfaceObject(enum.Enum):
    EMPTY = 0
    MUD = 1
    OIL_SPILL = 2
    OIL_POWER = 3
    FINISH = 4
    BOOST = 5
    PLAYER = 6
    OPPONENT = 7

def read_config():
    with open("config.json") as f:
        print("file open")
        config = json.load(f)
    return config

def get_round_as_string(round):
    rnd_str = str(round)
    if len(rnd_str) == 3:
        return rnd_str
    elif len(rnd_str) == 2:
        return "0"+rnd_str
    else:
        return "00"+rnd_str

def read_json(round, config):
    rnd_as_str = get_round_as_string(round)
    player_file = config["FolderPrepend"]+rnd_as_str+'/'+config["Player"]+'/JsonMap.json'
    with open(player_file) as f:
        player_data = json.load(f)

    opponent_file = config["FolderPrepend"]+rnd_as_str+'/'+config["Opponent"]+'/JsonMap.json'
    with open(opponent_file) as f:
        opponent_data = json.load(f)

    return player_data, opponent_data

def populate_grid(grid, player_world, opponent_world, player_id = 1, opponent_id = 2):
    player_offset = player_world[0][0]["position"]["x"]
    # offset = 0
    for row in player_world:
        for cell in row:
            
            # print(cell["position"]["y"]+2, cell["position"]["x"]-player_offset, player_offset)
            grid[cell["position"]["y"]+2][cell["position"]["x"]-player_offset] = SurfaceObject(cell["surfaceObject"])
        
            if cell["occupiedByPlayerId"] == player_id:
                grid[cell["position"]["y"]+2][cell["position"]["x"]-player_offset] = SurfaceObject.PLAYER
            if cell["occupiedByPlayerId"] == opponent_id:
                grid[cell["position"]["y"]+2][cell["position"]["x"]-player_offset] = SurfaceObject.OPPONENT   

    opponent_offset = opponent_world[0][0]["position"]["x"]
    for row in opponent_world:
        for cell in row:
            
            grid[cell["position"]["y"]+10][cell["position"]["x"]-opponent_offset] = SurfaceObject(cell["surfaceObject"])
        
            if cell["occupiedByPlayerId"] == player_id:
                grid[cell["position"]["y"]+10][cell["position"]["x"]-opponent_offset] = SurfaceObject.PLAYER
            if cell["occupiedByPlayerId"] == opponent_id:
                grid[cell["position"]["y"]+10][cell["position"]["x"]-opponent_offset] = SurfaceObject.OPPONENT   
    return grid, player_offset, opponent_offset

def display_text(screen, font, config, player, opponent, textcolor):
    cellSurf = font.render(f'PLAYER1: {config["Player"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (  10, 15)
    screen.blit(cellSurf, cellRect)

    cellSurf = font.render(f'PLAYER2: {config["Opponent"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 215)
    screen.blit(cellSurf, cellRect)

    cellSurf = font.render(f'PLAYER: {config["Player"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 400)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'Speed: {player["player"]["speed"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 420)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'State: {player["player"]["state"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 440)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'Powerups: {player["player"]["powerups"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 460)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'Boosting: {player["player"]["boosting"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 480)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'PLAYER: {config["Opponent"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 600)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'Speed: {opponent["player"]["speed"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 620)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'State: {opponent["player"]["state"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 640)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'Powerups: {opponent["player"]["powerups"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = (10, 660)
    screen.blit(cellSurf, cellRect) 

    cellSurf = font.render(f'Boosting: {opponent["player"]["boosting"]}', True, textcolor)
    cellRect = cellSurf.get_rect()
    cellRect.topleft = ( 10, 680)
    screen.blit(cellSurf, cellRect) 