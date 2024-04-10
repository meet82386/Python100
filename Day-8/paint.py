import math
def calculate(h, w):
    area = h*w
    paint_cans = area/5.0
    return math.ceil(paint_cans)

h = int(input("Enter height of wall: "))
w = int(input("Enter width of wall: "))

print(f"Paint cans needed: {calculate(h, w)}")