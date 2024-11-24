a = None
while a is None:
    try:
        a = float(input("Podaj a: "))
    except ValueError:
        print("Podaj poprawną wartośc liczbową.")

b = ''
while b == '':
    try:
        b = float(input("Podaj b: "))
    except ValueError:
        print("Podaj poprawną wartość liczbową.")
op = input("Operator (+/-/*/:)")

if op == '+':
    print(a,'+',b,'=',a+b)
elif op == '-':
    print(f"{a}-{b}={a-b}")
elif op == '*':
    print(str(a)+'*'+str(b)+'='+str(a*b))
elif op == ':':
    if b != 0:
        print(f"{a}:{b}={a/b:.4f}")
    else:
        print("Nie dzieli sie przez zero!")