class Car:
    def __init__(self, mark, model, year, color):
        self._mark = mark     # pole "chronione"
        self._model = model
        self._year = year
        self.__color = color  # pole "prywatne"
    def change_color(self, new_color):
        self.__color = new_color


car = Car("BMW", "3", 1999, "czerwony")

car._model = "13"
print(car._model)


# w taki sposób można jednak dostać sie do danych pól prywatnych
#    _NazwaKlasy__polePrywatne
car._Car__color = "niebieski"
print(car._Car__color)
