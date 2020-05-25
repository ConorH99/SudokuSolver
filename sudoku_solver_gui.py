import pygame as pg
from pygame.locals import *
from settings import *
import sys

class Grid:

    def __init__(self, time_delay=100):
        self.grid = BOARD
        self.rows = NUM_ROWS_COLS
        self.cols = NUM_ROWS_COLS
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.cell_size = TILE_SIZE
        self.font_name = FONT_NAME
        self.time_delay = time_delay
        pg.init()

    def run(self):
        running = True
        while running:
            self.draw()
            for event in pg.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.grid = BOARD
                        self.solve()
                if event.type == QUIT:
                    running = False
        pg.quit()

    def draw(self):
        self.screen.fill(WHITE)
        self.draw_grid()
        for i in range(self.rows):
            for j in range(self.cols):
                self.draw_num(i, j, BLACK, str(self.grid[i][j]))
        pg.display.flip()

    def draw_grid(self):
        for x in range(self.cols):
            if x % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            pg.draw.line(self.screen, BLACK, (x*self.cell_size, 0), (x*self.cell_size, SCREEN_HEIGHT), thickness)
        for y in range(self.rows):
            if y % 3 == 0:
                thickness = 3
            else:
                thickness = 1
            pg.draw.line(self.screen, BLACK, (0, y*self.cell_size), (SCREEN_WIDTH, y*self.cell_size), thickness)

    def draw_num(self, i, j, colour, num):
        if num == "0":
            numb = ""
        else:
            numb = num
        font_name = pg.font.match_font(self.font_name, False, False)
        font = pg.font.Font(font_name, 50)
        text_surface = font.render(numb, True, BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (((j * self.cell_size) + self.cell_size//2), ((i * self.cell_size) + self.cell_size//2))
        self.screen.blit(text_surface, text_rect)
 

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

        for event in pg.event.get():
            if event.type == QUIT:
                sys.exit()

        indices = [0, 0]

        if not self.find_empty():
            return True
            self.run()
        indices = self.find_empty()

        row = indices[0]
        col = indices[1]

        for i in range(1, 10):
            if self.is_valid(row, col, i):
                self.grid[row][col] = i
                self.draw()
                pg.time.delay(self.time_delay)
                if self.solve():
                    return True
                self.grid[row][col] = 0
                self.draw()
                pg.time.delay(self.time_delay)
        return False



def main():

    grid = Grid(150)
    grid.run()


main()