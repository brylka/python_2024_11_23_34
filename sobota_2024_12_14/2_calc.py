class Calc:
    @staticmethod
    def add(a, b):
        try:
            return a + b
        except TypeError:
            return "Błędne dane"
    @staticmethod
    def sub(a,b):
        try:
            return a - b
        except TypeError:
            return "Błędne dane"
    @staticmethod
    def mul(a,b):
        try:
            return float(a) * float(b)
        except TypeError:
            return "Błędne dane"
    @staticmethod
    def div(a,b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Błąd dzielenia przez zero"
        except TypeError:
            return "Błędne dane"


print(f"Dodawanie: {Calc.add(4.5,2)}")
print(f"Odejmowanie: {Calc.sub(4,2)}")
print(f"Mnożenie: {Calc.mul(4,5)}")
print(f"Dzielenie: {Calc.div(4,2)}")


