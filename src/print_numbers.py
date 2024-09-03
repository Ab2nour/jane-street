def palindrom():
    a = 23
    i = 1

    while True:
        a = 23 * i

        i += 1

        if a > 10**7:
            break
        str_a = str(a)

        # if str_a[::-1] == str_a:
        #     print(a)

        if a > 10**6:
            if str_a[::-1] == str_a:
                if str_a[0] == str_a[1]:
                    if str_a[0] in ("1", "3", "7", "9"):
                        if str_a[2] in ("1", "3", "7", "9"):
                            if str_a[1] != str_a[2]:
                                print(a)

    print("0===================")
    for i in range(300):
        if 10_000 > 88 * i >= 1000:
            if str(88 * i)[0] in ("1", "9"):
                print(88 * i)
    print("1===================")
    for i in range(300):
        if 1_000 > 88 * i >= 100:
            if str(88 * i)[1] == str(88 * i)[2]:
                print(88 * i)

    print("2===================")
    for i in range(20_000):
        if 100_000 > 88 * i >= 10_000:
            if str(88 * i)[1:4] in ("111", "999"):
                print(88 * i)

    print("3===================")
    for i in range(200_000):
        if 1_000_000 > 88 * i >= 100_000:
            if str(88 * i)[-4:-1] in ("111", "999"):
                print(88 * i)

    print("4===================")
    for i in range(1_000):
        if 10_000 > 88 * i >= 1_000:
            if str(88 * i)[1] == str(88 * i)[2]:
                print(88 * i)

    print("5===================")
    for i in range(1_000):
        if 10_000 > 37 * i >= 1_000:
            if str(37 * i)[1] == str(37 * i)[2] == str(37 * i)[3]:
                print(37 * i)

    print("6===================")
    for i in range(10_000):
        if 100_000 > 37 * i >= 10_000:
            if str(37 * i)[1] == str(37 * i)[2] == str(37 * i)[3] == str(37 * i)[4]:
                print(37 * i)

    print("7===================")
    for i in range(10_000):
        if 100_000 > 37 * i >= 10_000:
            if (
                str(37 * i)[2] == str(37 * i)[3] == str(37 * i)[4]
                and str(37 * i)[0] == "7"
            ):
                if str(37 * i)[2:5] in ("666", "888"):
                    print(37 * i)

    print("8===================")
    for i in range(10_000):
        if 10_000 > 37 * i >= 1_000:
            if str(37 * i)[2] == str(37 * i)[3] and str(37 * i)[0] == "7":
                if str(37 * i)[2:4] in ("66", "88"):
                    print(37 * i)

def print_carres():
    print("-------------------- carrés --------------------")
    for i in range(100):
        print(i**2)

palindrom()
print_carres()
