import random
from time import sleep

class GameOfLife:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for x in range(self.width)] for y in range(self.height)]
        # self.grid = []
        #
        # for y in range(self.height):
        #     row = []
        #     for x in range(self.width):
        #         row.append(0)
        #     self.grid.append(row)

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

        # for j in range(max(0,y-1),min(self.height,y+2)):
        #     for i in range(max(0,x-1),min(self.width,x+2)):
        #         if self.grid[j][i] and (x != i or y != j):
        #             count += 1
        return count

    def update(self):
        new_grid = [[0 for x in range(self.width)] for y in range(self.height)]
        # new_grid = []
        # for y in range(self.height):
        #     row = []
        #     for x in range(self.width):
        #         row.append(0)
        #     new_grid.append(row)

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




game = GameOfLife(10,10)
game.set_cell(3,0)
game.set_cell(4,0)
game.set_cell(5,0)
# game.set_cell(22,23)
# game.set_cell(23,24)

while True:
    game.display()
    game.update()
    sleep(1)