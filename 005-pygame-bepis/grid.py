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
    
    def is_empty(self, row, column) -> bool:
        return self.GRID[row][column] == 0

    def is_row_full(self, row) -> bool:
        for column in range(self.COLUMNS):
            if self.GRID[row][column] == 0:
                return False
        return True
    
    def clear_row(self, row):
        for column in range(self.COLUMNS):
            self.GRID[row][column] = 0
    
    def move_row_down(self, row, amount):
        for column in range(self.COLUMNS):
            self.GRID[row + amount][column] = self.GRID[row][column]
            self.GRID[row][column] = 0
    
    def clear_full_rows(self) -> int:
        completed = 0

        # Check every row in reverse order
        for row in range(self.ROWS - 1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                self.GRID[row][column] = 0

    def draw(self, screen):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                cell_value = self.GRID[row][column]
                cell_rect = pygame.Rect(column * self.CELL_SIZE + 1, row * self.CELL_SIZE + 1, self.CELL_SIZE - 1, self.CELL_SIZE - 1)
                pygame.draw.rect(screen, self.COLORS[cell_value], cell_rect)