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
UP_STAIRS_COLOR = (0, 255, 255)  # Cyan for upstairs
DOWN_STAIRS_COLOR = (255, 165, 0) 

class Dungeon:
    def __init__(self, filename):
        self.tile_size = 16  # Adjust to the size of your tiles in the tileset
        self.load_dungeon("game/" + filename)
        self.create_window()
        self.tileset = pygame.image.load('game\\assets\\DungeonTileset.png').convert_alpha()
        self.sprite_data = self.load_sprite_sheet('game\\assets\\tile_list.txt')
        self.tile_mapping = {
            '#': 'wall_mid', 
            ' ': 'floor_1',      
            'D': 'floor_stairs',
            'U': 'crate' 
                }

        
    def load_sprite_sheet(self, filename):
        sprite_data = {}
        with open(filename, 'r') as file:
            for line in file:
                parts = line.split()
                if len(parts) == 5:
                    name, x, y, width, height = parts
                    sprite_data[name] = (int(x), int(y), int(width), int(height))
        return sprite_data

    def get_sprite(self, ascii_symbol):
        sprite_name = self.tile_mapping.get(ascii_symbol)
        if sprite_name and sprite_name in self.sprite_data:
            x, y, width, height = self.sprite_data[sprite_name]
            return self.tileset.subsurface(pygame.Rect(x, y, width, height))
        return None

    
    def load_dungeon(self, filename):
        with open( filename, 'r') as file:
            lines = file.readlines()

        # Parse dungeon dimensions from the first line
        self.m, self.n = map(int, lines[0].strip().split())

        # Create a 2D grid to represent the dungeon
        self.dungeon = [list(line.strip()) for line in lines[1:]]
        

    def create_window(self):
        self.square_size = self.tile_size
        self.window_width = self.n * self.square_size
        self.window_height = self.m * self.square_size
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Dungeon")

    def draw_dungeon(self, player_x, player_y):
        self.window.fill(WHITE)
        for y, row in enumerate(self.dungeon):
            for x, cell in enumerate(row):
                sprite = self.get_sprite(cell)  # Assuming cell value corresponds to sprite names
                if sprite:
                    self.window.blit(sprite, (x * self.tile_size, y * self.tile_size))


        # Draw the player
        player_sprite = self.get_sprite('orc_shaman_idle_anim_f0')  # Replace with actual player sprite name
        if player_sprite:
            self.window.blit(player_sprite, (player_x * self.tile_size, player_y * self.tile_size))
        pygame.display.update()

    def is_exit(self, x, y):
        return self.dungeon[y][x] in ['U', 'D']

    def reset_dungeon(self, filename):
        self.load_dungeon(filename)
