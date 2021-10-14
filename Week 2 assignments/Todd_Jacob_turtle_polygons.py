import turtle
flag = 0
trigger = True
def poly():
    x = turtle.getscreen()
    y = turtle.Turtle()
    print("what color would you like it?")
    color = input()
    x.bgcolor(color)
    print("how many sides?")
    z = int(input())
    sides = z
    print((sides-2)*180/sides)
    y.shape("turtle")
    while flag < z:
        y.forward(sides*10)                                                                 #lines 16 and 17 are from https://www.geeksforgeeks.org/draw-any-polygon-in-turtle-python/ I could not figure out how to make the shape so I had to look it up
        y.right(360 / sides)
        z = z - 1
    print("would you like to try again? 1 for yes 0 for no")
    w = int(input())
    if w == 0:
        trigger = False

def main():
    while trigger == True:
        poly()




main()