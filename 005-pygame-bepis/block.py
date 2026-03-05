from colors import Colors
from position import Position
import pygame

class Block:
    def __init__(self, id: int):
        self.id = id
        self.cells = dict()
        self.cell_size = 30
        self.rotation_state = 0

        self.column_offset = 0
        self.row_offset = 0

        self.colors = Colors.get_cell_colors()

    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns
    
    def get_cell_positions(self):
        current_tiles = self.cells[self.rotation_state]
        moved_tiles = [Position(tile.row + self.row_offset, tile.column + self.column_offset) for tile in current_tiles]
        return moved_tiles


    def draw(self, screen):
        
        # Returns the list of Positions(x, y) in our defined rotation state
        tiles = self.get_cell_positions()

        for tile in tiles:
            tile_rect = pygame.Rect(tile.column * self.cell_size + 1, tile.row * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)