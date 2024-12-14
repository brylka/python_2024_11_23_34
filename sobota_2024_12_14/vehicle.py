class Vehicle:
    def __init__(self, mark, model, year, color=None):
        self.mark = mark
        self.model = model
        self.year = year
        self.color = color
    def __str__(self):
        return f"{self.mark} {self.model} {self.year} {self.color}"

    def hong(self):
        print(f"Samochód {self.mark} trąbi")

    def change_color(self,new_color):
        self.color = new_color


if __name__ == "__main__":
    vehicle = Vehicle("Fiat", "126p", 1970, "zielony")
    print(vehicle)