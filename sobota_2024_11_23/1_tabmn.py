for b in range(0,11):
    for a in range(0,11):
        if a==0 and b==0:
            print("*", end="\t")
        elif a==0:
            print(b, end="\t")
        elif b==0:
            print(a, end="\t")
        else:
            print(a*b, end="\t")
    print()