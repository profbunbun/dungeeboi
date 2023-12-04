import pygame
import sys
from dungeon import Dungeon  # Import the Dungeon class from your dungeon script
from player import Player  # Import the Player class (ensure it's compatible with Dungeon)

# Initialize pygame
pygame.init()

# Create a Dungeon and Player instance
dungeon = Dungeon("dungeon.txt")
player = Player(dungeon)  # Make sure the Player class is adapted for Dungeon

# Main loop
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
        print("Congratulations! You've found the stairs!")
        break

# Quit pygame
pygame.quit()
sys.exit()
