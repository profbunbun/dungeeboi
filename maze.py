import pygame
import sys

# Initialize pygame
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (111, 111, 111)

class Dungeon:
    def __init__(self, filename):
        self.load_dungeon(filename)
        self.create_window()

    def load_dungeon(self, filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Parse dungeon dimensions from the first line
        self.m, self.n = map(int, lines[0].strip().split())

        # Create a 2D grid to represent the dungeon
        self.dungeon = [list(line.strip()) for line in lines[1:]]

    def create_window(self):
        self.square_size = 10  # Size of each square in pixels
        self.window_width = self.n * self.square_size
        self.window_height = self.m * self.square_size
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Dungeon")

    def draw_dungeon(self, player_x, player_y):
        self.window.fill(WHITE)
        for y, row in enumerate(self.dungeon):
            for x, cell in enumerate(row):
                color = WHITE  # Path
                if cell == '#':
                    color = BLACK  # Walls
                elif cell == 'D':
                    color = YELLOW  # Doors
                elif cell == 'S':
                    color = RED  # Stairs

                pygame.draw.rect(self.window, color, (x * self.square_size, y * self.square_size, self.square_size, self.square_size))

        # Draw the player
        pygame.draw.rect(self.window, GREY, (player_x * self.square_size, player_y * self.square_size, self.square_size, self.square_size))
        pygame.display.update()

    def is_exit(self, x, y):
        return self.dungeon[y][x] == 'S' 
