import random
def main():
    guessing_game()

def guessing_game():
    z = True
    x = random.randint(0,100)
    while z == True:
        print("what is your guess?")
        y = int(input())
        if y > x:
            print("to high")
        elif y == x:
            print("correct")
            z = False
        else:
            print("to low") 


main()
