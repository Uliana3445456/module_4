def d(a):
    return a == (a[::-1])
while True:
    a = input()
    print(f"{a} True" if d(a) else "False")