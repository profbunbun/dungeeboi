import pygame
import sys

from dungeon import Dungeon  
from player import Player  

# List of dungeon filenames
dungeon_filenames = ["dungeon_floor_1.txt", "dungeon_floor_2.txt", "dungeon_floor_3.txt", "dungeon_floor_4.txt", "dungeon_floor_5.txt"]
current_floor = 0

pygame.init()

# Load the first dungeon
dungeon = Dungeon(dungeon_filenames[current_floor])
player = Player(dungeon) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move(0, -1)
            elif event.key == pygame.K_DOWN:
                player.move(0, 1)
            elif event.key == pygame.K_LEFT:
                player.move(-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.move(1, 0)

    dungeon.draw_dungeon(player.x, player.y)

    if dungeon.is_exit(player.x, player.y):
        current_floor += 1
        if current_floor < len(dungeon_filenames):
            print(f"Moving to floor {current_floor + 1}")
            dungeon.reset_dungeon(dungeon_filenames[current_floor])
            player.reset_position()
            player.dungeon = dungeon
        else:
            print("Congratulations! You've completed the dungeon!")
            break

# Quit pygame
pygame.quit()
sys.exit()
