import pygame
import random
from time import sleep

class GameOfLife:
    def __init__(self, width, height, cell_size=10):
        self.width = width
        self.height = height
        self.grid = [[random.randint(0,1) for x in range(self.width)] for y in range(self.height)]
        pygame.init()
        self.screen = pygame.display.set_mode((self.width*cell_size, self.height*cell_size))
        pygame.display.set_caption("Aplikacja pygame")

    def set_cell(self, x, y):
        self.grid[y-1][x-1] = not self.grid[y-1][x-1]

    def count_neighbords(self, x, y):
        count = 0
        for j in range(y - 1, y + 2):
            if j == self.height:
                j = 0
            for i in range(x - 1, x + 2):
                if i == self.width:
                    i = 0
                if self.grid[j][i] and (x != i or y != j):
                    count += 1
        return count

    def update(self):
        new_grid = [[0 for x in range(self.width)] for y in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == 1:
                    if self.count_neighbords(x, y) == 2 or self.count_neighbords(x, y) == 3:
                        new_grid[y][x] = 1
                else:
                    if self.count_neighbords(x, y) == 3:
                        new_grid[y][x] = 1
        self.grid = new_grid

    def display(self):
        for y in self.grid:
            for x in y:
                if x == 0:
                    print('`', end=" ")
                else:
                    print('*', end=" ")
            print()

    def run(self):
        while True:
            game.display()
            game.update()
            sleep(1)


game = GameOfLife(50,50)
game.run()

