class Vehicle:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.mark} {self.model} {self.year}"

    def hong(self):
        print(f"Samochód {self.mark} trąbi")


if __name__ == "__main__":
    vehicle = Vehicle("Fiat", "126p", 1970)
    print(vehicle)