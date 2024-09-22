import math
print("Введите обьем шара - ", end = " ")
v = int(input())
r = ((3 * v) / (4 * math.pi)) ** (1 / 3)
print (f"рАдиус шара - {r}")