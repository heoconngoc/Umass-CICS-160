class Map:
    def __init__(self, size):
        self.width, self.height = size
        self.grid = [["." for _ in range(self.width)] for _ in range(self.height)]

    def update(self, listOfVehicles):
        self.grid = [["." for _ in range(self.width)] for _ in range(self.height)]

        for vehicle in listOfVehicles:
            x, y = vehicle.getPosition()
            if 0 <= x < self.width and 0 <= y < self.height:
                self.grid[y][x] = vehicle.getSymbol()

        self.render()

    def render(self):
        for row in self.grid:
            print(" ".join(row))
        print("\n" + "=" * (self.width * 2))
