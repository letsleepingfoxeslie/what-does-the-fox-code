import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.ROWS = 20
        self.COLUMNS = 10
        self.CELL_SIZE = 30
        self.GRID = [[0 for c in range(self.COLUMNS)] for r in range(self.ROWS)]
        self.COLORS = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                print(self.GRID[row][column], end = " ")
            print()

    def is_inside(self, row: int, column: int) -> bool:
        if (row >= 0 and row < self.ROWS) and (column >= 0 and column < self.COLUMNS):
            return 
        return False

    def draw(self, screen):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                cell_value = self.GRID[row][column]
                cell_rect = pygame.Rect(column * self.CELL_SIZE + 1, row * self.CELL_SIZE + 1, self.CELL_SIZE - 1, self.CELL_SIZE - 1)
                pygame.draw.rect(screen, self.COLORS[cell_value], cell_rect)