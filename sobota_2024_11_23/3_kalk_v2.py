import re

s = input("Podaj działanie matematyczne (np. 2+2, 2-3, 4*7, 3:4): ")

lista = re.split(r'([+\-*:])', s)
if len(lista) == 3:
    print("Poprawne działenie")
    a = float(lista[0])
    b = float(lista[2])
    op = lista[1]
    if op == '+':
        print(a, '+', b, '=', a + b)
    elif op == '-':
        print(f"{a}-{b}={a - b}")
    elif op == '*':
        print(str(a) + '*' + str(b) + '=' + str(a * b))
    elif op == ':':
        if b != 0:
            print(f"{a}:{b}={a / b:.4f}")
        else:
            print("Nie dzieli sie przez zero!")
    else:
        print("Błąd")
else:
    print("Niepoprawne działanie!")
    # todo przypadek 5 elementów w liście np -5*7

# lista = s.split("+")
# if len(lista) == 2:
#     print("Wykryte dodawanie!")
#     a = float(lista[0])
#     b = float(lista[1])
#     print(f"{a}+{b}={a+b}")
# lista = s.split("-")
# if len(lista) == 2:
#     print("Wykryte odejmowanie!")
# lista = s.split("*")
# if len(lista) == 2:
#     print("Wykryte mnożenie!")
# lista = s.split(":")
# if len(lista) == 2:
#     print("Wykryte dzielenie!")
