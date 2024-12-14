from vehicle import Vehicle

class Electric(Vehicle):
    def __init__(self, mark, model, year, distance, battery, color):
        super().__init__(mark, model, year, color)
        self.distance = distance
        self.battery = battery

    def change_color_2(self,new_color):
        self.color = new_color.upper()


if __name__ == "__main__":
    electric = Electric('Tesla', '3', 2024, 200, 50, "niebieski")
    print(electric.mark)
    electric.hong()
    print(electric.color)
    electric.change_color("fioletowy")
    print(electric.color)
    electric.change_color_2("fioletowy")
    print(electric.color)
