'''
1 for snake
-1 for water
0 for gun
'''
import random
random_number = random.choice([-1, 0, 1])


computer = random_number # Computer's choice a Random number
you = input("Enter your choice (s for snake, w for water, g for gun): ")
youDict = {"s": 1, "w": -1, "g": 0}
revDict={1:"Snake", -1:"Water",0:"Gun"}
print(f"You Choose {revDict[youDict[you]]}:")
print(f"Computer Choose {revDict[computer]}:")

num = youDict[you]
if computer == num:
    print("It's a draw!")
else:
    if computer == -1 and num == 1:
        print("You Win!")
    elif computer == -1 and num == 0:
        print("You Lost!")
    elif computer == 1 and num == -1:
        print("You Lost!")
    elif computer == 1 and num == 0:
        print("You Win!")
    elif computer == 0 and num == 1:
        print("You Lost!")
    elif computer == 0 and num == -1:
        print("You Win!")
    else:
        print("Something went wrong!")
