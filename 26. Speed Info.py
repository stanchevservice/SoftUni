import math

figure = (input())

if figure == "square":
    number = float(input())
    number = math.pow(number, 2)
    print(f"{number:.3f}")
elif figure == "rectangle":
    number = float(input())
    number1 = float(input())
    area = number1 * number
    print(f"{area:.3f}")
elif figure == "circle":
    number = float(input())
    area = math.pi * math.pow(number, 2)
    print(f"{area:.3f}")
elif figure == "triangle":
    number = float(input())
    number1 = float(input())
    area = (number1 * number) / 2
    print(f"{area:.3f}")
