from pprint import pprint

class Point:
    
    def __init__(self, row, column):
        self.row = row
        self.column = column


class Grid:

    def __init__(self, rows:int, columns:int):
        self.grid = []

    def create_grid(self):
        self.grid = [[[0] for x in range(self.columns)] for y in range(self.rows)]
        return self.grid

    def add_points_to_grid(self, *points):
        for point in points:
            self.grid[point.row][point.column] = 2


class Wall:

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2


ponto_1 = Point(3, 1)
ponto_2 = Point(3, 5)

grid = Grid(10,10)
printable_grid = grid.add_points_to_grid(ponto_1, ponto_2)

pprint(printable_grid)
