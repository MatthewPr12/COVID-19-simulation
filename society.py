from arrays import Array2D

class Human():
    pass

class Society:
    HUMAN = Human()
    EMPTY = None
    def __init__(self, num_rows, num_cols, residents):
        self.grid = Array2D(num_rows, num_cols)
        self.num_of_residents = residents
        self.num_of_infeded = 0
        self.num_of_recovered = 0
        self.num_of_dead = 0

    def get_neighbors(self, row, col):
        counter = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if self.is_human(i + row, j + col):
                        counter += 1
                except AssertionError:
                    pass
        if self.is_human(row, col):
            counter -= 1
        return counter

    def is_human(self, row, col):
        return True if isinstance(self.grid[row, col], Human()) else False
