from vehicle import Vehicle

class Electric(Vehicle):
    def __init__(self, mark, model, year, distance, battery, color):
        super().__init__(mark, model, year, color)
        self.distance = distance
        self.battery = battery


if __name__ == "__main__":
    electric = Electric('Tesla', '3', 2024, 200, 50, "niebieski")
    print(electric.mark)
    electric.hong()
    print(electric.color)