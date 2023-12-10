#Project Name: The perfect guess
def game(play):
    f = open("game.txt", "r")
    a = f.read()
    b = int(a)
    c = "Wohooo!!..You made highest score.."
    if b > play:
        with open ("game.txt","w") as f:
            f.write(str(play))

import random
r = random.randint(1, 100)
n = int(input("Guess a number: "))
a = 1
while r != n:
    if r == n:
        print("You had a perfect guess..")
        a += 1
    elif r < n:
        n = int(input("Enter a lesser value: "))
        a += 1
    else:
        n = int(input("Enter a greater value: "))
        a += 1
print(f"The divice has choosen {r}")
print(f"You had a perfect guess..!!\nThe score is {a}")
game(a)