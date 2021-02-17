# qutini iciga 3 xil rang chizadi
import turtle

def temperature_color(temp):
    # Change this code!
    if temp < 20:
        return "blue"
    if temp < 50:
        return "purple"
    if temp >= 50:
        return "red"
    return "green"

def draw_temperature(temp):
    t = turtle.Turtle()
    t.penup()
    t.back(100)
    t.width(20)
    t.pendown()
    for n in range(temp):
        t.color(temperature_color(n))
        t.forward(1)

def draw_therm_box():
    t = turtle.Turtle()
    t.speed(0)
    t.color("gray")
    t.penup()
    t.back(120)
    t.pendown()
    t.left(90)
    for side in [20, 240, 40, 240, 20]:
        t.forward(side)
        t.right(90)
    t.hideturtle()

draw_therm_box()
draw_temperature(120)

# subsring aniqlaydi
def is_substring(substring, string):
    index = 0
    while index < len(string):
         
         print(string[index : index + len(substring)] == substring)
         index += 1
    return False
print(is_substring('bad', 'abracadabra'))
print(is_substring('dab', 'abracadabra'))

# substring necci marta borligini sanaydi
def count_substring(string, target):
    index = 0
    total = 0
    while index < len(string):
        if string[index: index + len(target)] == target:
            total += 1
        index += 1
    return total
print(count_substring("aaaa", "aa"))
# qitti yaaxshiroq varianti
def count_substring(string, target):
    total = 0
    index = 0
    while index < len(string):
        if string[index : index + len(target)] == target:
            total += 1
            index += len(target)   # <- This is the key line
        else:
            index += 1
    return total
print(count_substring('AAAA', "AA"))