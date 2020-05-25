import pygame as pg
from pygame.locals import *
from settings import *

'''def draw_text(surface, text, size, x, y):
    font_name = pg.font.match_font(FONT_NAME, False, False)
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.x = x * TILE_SIZE
    text_rect.y = y * TILE_SIZE
    surface.blit(text_surface, text_rect)'''

#pg.init()

grid =   [[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

#screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


class Solver:

    def __init__(self, grid):
        self.grid = grid

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return i, j
        return False

    def is_valid(self, row, col, num):
        return self.valid_row(row, num) and self.valid_col(col, num) and self.valid_box(row, col, num)

    def valid_row(self, row, num):
        for i in range(9):
            if self.grid[row][i] == num:
                return False
        return True

    def valid_col(self, col, num):
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        return True

    def valid_box(self, row, col, num):
        for i in range(3):
            for j in range(3):
                row_check = i + (row - (row % 3))
                col_check = j + (col - (col % 3))
                if self.grid[row_check][col_check] == num:
                    return False
        return True

    def print_grid(self): 
        for i in range(9): 
            for j in range(9): 
                print(str(self.grid[i][j]) + " ", end="")
            print('\n')

    def solve(self):

        indices = [0, 0]

        if not self.find_empty():
            return True
        indices = self.find_empty()

        row = indices[0]
        col = indices[1]

        for i in range(1, 10):
            if self.is_valid(row, col, i):
                self.grid[row][col] = i
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False


def main():
    solver = Solver(grid)
    solver.solve()
    solver.print_grid()

main()



