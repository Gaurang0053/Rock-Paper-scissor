try :
    c='y'
    while c=='y':
        print("enter your choice to start the game ")
        print("press 1 for A.I vs A.I")
        print("press 2 for A.I vs HUMAN")
        print("press 3 to show log")

        ch = int(input())
        if ch == 1:
            import time

            print('first A.I thinks')
            time.sleep(3)
            import random

            lst = ["paper", "rock", "scissors"]
            for i in lst:
                a = random.choice(lst)
            print(a)

            import time

            print('second A.I thinks')
            time.sleep(3)
            import random

            lst = ["paper", "rock", "scissors"]
            for i in lst:
                b = random.choice(lst)
            print(b)
            if a == "rock" and b == "paper":
                f = open("d:\\ game.txt", "a+")
                f.write("second A.I wins" + "\n")
                print("second A.I wins")
            if a == "paper" and b == "scissors":
                f = open("d:\\ game.txt", "a+")
                f.write("second A.I wins" + "\n")
                print("second A.I wins ")
            if a == "paper" and b == "rock":
                f = open("d:\\ game.txt", "a+")
                f.write("first A.I wins" + "\n")
                print("first A.I wins")
            if a == "rock" and b == "scissors":
                f = open("d:\\ game.txt", "a+")
                f.write("first A.I wins" + "\n")
                print("first A.I wins")
            if a == "scissors" and b == "rock":
                f = open("d:\\ game.txt", "a+")
                f.write("second A.I wins" + "\n")
                print("second A.I wins")
            if a == "scissors" and b == "paper":
                f = open("d:\\ game.txt", "a+")
                f.write("first A.I wins" + "\n")
                print("first A.I wins")
            if a == b:
                f = open("d:\\ game.txt", "a+")
                f.write("match drawn" + "\n")
                print("match drawn")

        if ch == 2:
            print("your turn")
            b = input()
            b.lower()
            if b != "rock" and b != "paper" and b != "scissors":
                print("wrong input")
                exit(0)

            import time

            print('A.I thinks')
            time.sleep(3)
            import random

            lst = ["paper", "rock", "scissors"]
            for i in lst:
                a = random.choice(lst)
            print(a)
            if a == "rock" and b == "paper":
                f = open("d:\\ game.txt", "a+")
                f.write("you wins" + "\n")
                print("you wins")
            if a == "paper" and b == "rock":
                f = open("d:\\ game.txt", "a+")
                f.write("A.I wins" + "\n")
                print("A.I wins")
            if a == "rock" and b == "scissors":
                f = open("d:\\ game.txt", "a+")
                f.write("A.I wins" + "\n")
                print("A.I wins")
            if a == "scissors" and b == "paper":
                f = open("d:\\ game.txt", "a+")
                f.write("A.I wins" + "\n")
                print("A.I wins")
            if a == "paper" and b == "scissors":
                f = open("d:\\ game.txt", "a+")
                f.write("you wins" + "\n")
                print("you wins")
            if a == "scissors" and b == "rock":
                f = open("d:\\ game.txt", "a+")
                f.write("you wins" + "\n")
                print("you wins")
            if a == b:
                f = open("d:\\ game.txt", "a+")
                f.write("match drawn" + "\n")
                print("match drawn")
        if ch == 3:
            f = open("d:\\ game.txt", "a+")
            f.seek(0, 0)
            c = f.read()
            print(c)

        if ch > 3 or ch < 0:
            print("wrong choice")
        print("Do you want to continue press y ")
        c = input()
        if c != 'y':
            print('thankyou for playing ')

except Exception as e :
    print(e)


