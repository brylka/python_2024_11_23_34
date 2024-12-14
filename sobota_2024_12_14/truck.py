from car import Electric

class ElectricTruck(Electric):
    def __init__(self, mark, model, year, distance, battery, color, capacity):
        super().__init__(mark, model, year, distance, battery, color)
        self.capacity = capacity
    def load(self, value):
        if value < self.capacity:
            print(f"Samochód {self.mark} został załadowany")
        else:
            print(f"Przekroczona ładowność samochodu {self.mark}")

    def __str__(self):
        return f"{super().__str__()} ładowność: {self.capacity}"

if __name__ == "__main__":
    truck = ElectricTruck("BMW", "truck", 2023, 200, 100, "czarny", 500)
    print(truck)
    truck.load(400)