class Temp:
    @staticmethod
    def cel_to_fah(c):
        try:
            return (float(c) * 9/5) + 32
        except ValueError:
            return "Błędne dane"
    @staticmethod
    def cel_to_kel(c):
        try:
            return float(c) + 273.15
        except ValueError:
            return "Błędne dane"

print(f"25'C to F: {Temp.cel_to_fah("25")}")
print(f"25'C to K: {Temp.cel_to_kel(25)}")
