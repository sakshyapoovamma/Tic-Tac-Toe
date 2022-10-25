pos=[1,2,3,4,5,6,7,8,9]
c=[[" ","|"," ","|"," "],["—","|","—","|","—"],[" ","|"," ","|"," "],["—","|","—","|","—"],[" ","|"," ","|"," "]]
print("Welcome to the game of Tic-Tac-Toe")
while True:
    count=0
    for q in range(5):
        for r in range(5):
            print(c[q][r],end="")
        print("")
    print("Enter your choice: ")
    print("1.How to play?")
    print("2.Let's begin!")
    print("3.Exit")
    n=int(input())
    if n==1:
        print("How to play?")
        print("The game is played on a grid that's 3 squares by 3 squares each square numbered as shown below:")
        d=[["1","|","2","|","3"],["—","|","—","|","—"],["4","|","5","|","6"],["—","|","—","|","—"],["7","|","8","|","9"]]
        for q in range(5):
            for r in range(5):
                print(d[q][r],end="")
            print("")
        print('Players pick their symbols "x" or "o".Player 1 starts. Players take turns putting their symbols in empty squares.')
        print("The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner.")
        print("When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.")
        continue
    elif n==3:
        print("Exit")
        print("Thanks for playing.")
        break
    elif n==2:
        print("Go ahead!",end="")
    else:
        print("Invalid option")
        continue
    print("Enter Player 1 choice: ")
    print("1.x")
    print("2.o")

    p=int(input(""))
    if p==1:
        print("Player 1 selected 1.Player 1 plays x")
        print("Player 2 plays o")
    elif p==2:
        print("Player 1 selected 2.Player 1 plays o")
        print("Player 2 plays x")
    turn = 0
    while count==0:
        if c[0][0]==c[0][2] and c[0][2]==c[0][4]:
            if c[0][0]=="x":
                count=1
                break
            elif c[0][0]=="o":
                count=2
                break
        if c[2][0]==c[2][2] and c[2][2]==c[2][4]:
            if c[2][0]=="x":
                count=1
                break
            elif c[2][0]=="o":
                count=2
                break
        if c[4][0]==c[4][2] and c[4][2]==c[4][4]:
            if c[4][0]=="x":
                count=1
                break
            elif c[4][0]=="o":
                count=2
                break
        if c[0][0]==c[2][0] and c[2][0]==c[4][0]:
            if c[0][0]=="x":
                count=1
                break
            elif c[0][0]=="o":
                count=2
                break
        if c[0][2]==c[2][2] and c[2][2]==c[4][2]:
            if c[0][2]=="x":
                count=1
                break
            if c[0][2]=="o":
                count=2
                break
        if c[0][4]==c[2][4] and c[2][4]==c[4][4]:
            if c[0][4]=="x":
                count=1
                break
            elif c[0][4]=="o":
                count=2
                break
        if c[0][0]==c[2][2] and c[2][2]==c[4][4]:
            if c[0][0]=="x":
                count=1
                break
            elif c[0][0]=="o":
                count=2
                break
        if c[0][4]==c[2][2] and c[2][2]==c[4][0]:
            if c[0][4]=="x":
                count=1
                break
            elif c[0][4]=="o":
                count=2
                break
        if c[0][0]!=" " and  c[0][2]!=" " and c[0][4]!=" " and c[2][0]!=" " and c[2][2]!=" " and c[2][4]!=" " and c[4][0]!=" " and c[4][2]!=" " and c[4][4]!=" ":
            count=3
            break

        if turn==0:
            p1 = int(input("Enter the square number"))
            if p1 in pos:
                if p == 1:
                    if p1 == 1:
                        c[0][0] = "x"
                        pos.remove(1)
                    elif p1 == 2:
                        c[0][2] = "x"
                        pos.remove(2)
                    elif p1 == 3:
                        c[0][4] = "x"
                        pos.remove(3)
                    elif p1 == 4:
                        c[2][0] = "x"
                        pos.remove(4)
                    elif p1 == 5:
                        c[2][2] = "x"
                        pos.remove(5)
                    elif p1 == 6:
                        c[2][4] = "x"
                        pos.remove(6)
                    elif p1 == 7:
                        c[4][0] = "x"
                        pos.remove(7)
                    elif p1 == 8:
                        c[4][2] = "x"
                        pos.remove(8)
                    elif p1 == 9:
                        c[4][4] = "x"
                        pos.remove(9)
                    for q in range(5):
                        for r in range(5):
                            print(c[q][r], end="")
                        print("")
                elif p == 2:
                    if p1 == 1:
                        c[0][0] = "o"
                        pos.remove(1)
                    elif p1 == 2:
                        c[0][2] = "o"
                        pos.remove(2)
                    elif p1 == 3:
                        c[0][4] = "o"
                        pos.remove(3)
                    elif p1 == 4:
                        c[2][0] = "o"
                        pos.remove(4)
                    elif p1 == 5:
                        c[2][2] = "o"
                        pos.remove(5)
                    elif p1 == 6:
                        c[2][4] = "o"
                        pos.remove(6)
                    elif p1 == 7:
                        c[4][0] = "o"
                        pos.remove(7)
                    elif p1 == 8:
                        c[4][2] = "o"
                        pos.remove(8)
                    elif p1 == 9:
                        c[4][4] = "o"
                        pos.remove(9)
                    for q in range(5):
                        for r in range(5):
                            print(c[q][r], end="")
                        print("")
            else:
                print("Invalid Option")
                turn=0
                continue
            turn+=1



        if c[0][0]==c[0][2] and c[0][2]==c[0][4]:
            if c[0][0]=="x":
                count=1
                break
            elif c[0][0]=="o":
                count=2
                break
        if c[2][0]==c[2][2] and c[2][2]==c[2][4]:
            if c[2][0]=="x":
                count=1
                break
            elif c[2][0]=="o":
                count=2
                break
        if c[4][0]==c[4][2] and c[4][2]==c[4][4]:
            if c[4][0]=="x":
                count=1
                break
            elif c[4][0]=="o":
                count=2
                break
        if c[0][0]==c[2][0] and c[2][0]==c[4][0]:
            if c[0][0]=="x":
                count=1
                break
            elif c[0][0]=="o":
                count=2
                break
        if c[0][2]==c[2][2] and c[2][2]==c[4][2]:
            if c[0][2]=="x":
                count=1
                break
            if c[0][2]=="o":
                count=2
                break
        if c[0][4]==c[2][4] and c[2][4]==c[4][4]:
            if c[0][4]=="x":
                count=1
                break
            elif c[0][4]=="o":
                count=2
                break
        if c[0][0]==c[2][2] and c[2][2]==c[4][4]:
            if c[0][0]=="x":
                count=1
                break
            elif c[0][0]=="o":
                count=2
                break
        if c[0][4]==c[2][2] and c[2][2]==c[4][0]:
            if c[0][4]=="x":
                count=1
                break
            elif c[0][4]=="o":
                count=2
                break
        if c[0][0]!=" " and  c[0][2]!=" " and c[0][4]!=" " and c[2][0]!=" " and c[2][2]!=" " and c[2][4]!=" " and c[4][0]!=" " and c[4][2]!=" " and c[4][4]!=" ":
            count=3
            break
        if turn==1:
            p2 = int(input("Enter the square number"))
            if p2 in pos:
                if p == 2:
                    if p2 == 1:
                        c[0][0] = "x"
                        pos.remove(1)
                    elif p2 == 2:
                        c[0][2] = "x"
                        pos.remove(2)
                    elif p2 == 3:
                        c[0][4] = "x"
                        pos.remove(3)
                    elif p2 == 4:
                        c[2][0] = "x"
                        pos.remove(4)
                    elif p2 == 5:
                        c[2][2] = "x"
                        pos.remove(5)
                    elif p2 == 6:
                        c[2][4] = "x"
                        pos.remove(6)
                    elif p2 == 7:
                        c[4][0] = "x"
                        pos.remove(7)
                    elif p2 == 8:
                        c[4][2] = "x"
                        pos.remove(8)
                    elif p2 == 9:
                        c[4][4] = "x"
                        pos.remove(9)
                    for q in range(5):
                        for r in range(5):
                            print(c[q][r], end="")
                        print("")
                elif p == 1:
                    if p2 == 1:
                        c[0][0] = "o"
                        pos.remove(1)
                    elif p2 == 2:
                        c[0][2] = "o"
                        pos.remove(2)
                    elif p2 == 3:
                        c[0][4] = "o"
                        pos.remove(3)
                    elif p2 == 4:
                        c[2][0] = "o"
                        pos.remove(4)
                    elif p2 == 5:
                        c[2][2] = "o"
                        pos.remove(5)
                    elif p2 == 6:
                        c[2][4] = "o"
                        pos.remove(6)
                    elif p2 == 7:
                        c[4][0] = "o"
                        pos.remove(7)
                    elif p2 == 8:
                        c[4][2] = "o"
                        pos.remove(8)
                    elif p2 == 9:
                        c[4][4] = "o"
                        pos.remove(9)
                    for q in range(5):
                        for r in range(5):
                            print(c[q][r], end="")
                        print("")

            else:
                print("Invalid Option")
                turn=1
                continue
            turn=0



    if count==1:
        if p==1:
            print("Player 1 wins")
            print("Thanks for playing")
            break
        elif p==2:
            print("Player 2 wins")
            print("Thanks for playing")
            break
    if count==2:
        if p==2:
            print("Player 1 wins")
            print("Thanks for playing")
            break
        if p==1:
            print("Player 2 wins")
            print("Thanks for playing")
            break
    if count==3:
        print("It's a tie")
        print("Thanks for playing")
        break