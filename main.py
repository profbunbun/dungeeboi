import pygame
import sys

from game.levels.dungeon import Dungeon  
from game.entities.player import Player  

# List of dungeon filenames
dungeon_filenames = ["dungeon_floor_1.txt", "dungeon_floor_2.txt", "dungeon_floor_3.txt", "dungeon_floor_4.txt", "dungeon_floor_5.txt"]
current_floor = 0

# Initialize the first dungeon
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
    print(f"Player Position: {player.x}, {player.y}")


    # Check if the player is on the stairs and not just transported
    if dungeon.is_exit(player.x, player.y) and not player.just_transported:
        stair_type = dungeon.dungeon[player.y][player.x]  # 'U' or 'D'
        if stair_type == 'U':
            current_floor += 1
        elif stair_type == 'D':
            current_floor -= 1

        if 0 <= current_floor < len(dungeon_filenames):
            dungeon.reset_dungeon( dungeon_filenames[current_floor])
            player.dungeon = dungeon
            new_stair_type = 'D' if stair_type == 'U' else 'U'
            stairs_position = player.find_stairs(new_stair_type)
            if stairs_position:
                player.x, player.y = stairs_position
            else:
                player.reset_position()
            player.just_transported = True  # Set the flag after floor transition
        else:
            print("End of dungeon sequence reached")
            break

# Quit pygame
pygame.quit()
sys.exit()