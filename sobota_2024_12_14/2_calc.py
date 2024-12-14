class Calc:
    @staticmethod
    def add(a, b):
        return a + b
    @staticmethod
    def sub(a,b):
        return a - b
    @staticmethod
    def mul(a,b):
        return a * b
    @staticmethod
    def div(a,b):
        try:
            return a / b
        except ZeroDivisionError:
            return "Błąd dzielenia przez zero"
        except TypeError:
            return "Błędne dane"


print(f"Dodawanie: {Calc.add(4,2)}")
print(f"Odejmowanie: {Calc.sub(4,2)}")
print(f"Mnożenie: {Calc.mul(4,2)}")
print(f"Dzielenie: {Calc.div('4',0)}")


