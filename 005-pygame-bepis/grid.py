import pygame

class Grid:
    def __init__(self):
        self.ROWS = 20
        self.COLUMNS = 10
        self.CELL_SIZE = 30
        self.GRID = [[0 for c in range(self.COLUMNS)] for r in range(self.ROWS)]
        self.COLORS = self.get_cell_colors()

    def print_grid(self):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                print(self.GRID[row][column], end = " ")
            print()
    
    def get_cell_colors(self):
        DARK_GRAY = (26, 31, 40)
        GREEN = (47, 230, 23)
        RED = (232, 18, 18)
        ORANGE = (226, 116, 17)
        YELLOW = (237, 234, 4)
        PURPLE = (166, 0, 247)
        CYAN = (21, 204, 209)
        BLUE = (13, 64, 216)

        return [DARK_GRAY, GREEN, RED, ORANGE, YELLOW, PURPLE, CYAN, BLUE]

    def draw(self, screen):
        for row in range(self.ROWS):
            for column in range(self.COLUMNS):
                cell_value = self.GRID[row][column]
                cell_rect = pygame.Rect(column * self.CELL_SIZE + 1, row * self.CELL_SIZE + 1, self.CELL_SIZE - 1, self.CELL_SIZE - 1)
                pygame.draw.rect(screen, self.COLORS[cell_value], cell_rect)