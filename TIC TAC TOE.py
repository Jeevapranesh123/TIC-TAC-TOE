#TIC TAC TOE
theboard={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
count=0

def display(board):

    line = "--+---+--"
    print("          ",board[1],"|",board[2],"|",board[3])
    print("          ",line.rjust(4))
    print("          ",board[4], "|", board[5],"|", board[6])
    print("          ",line.rjust(4))
    print("          ",board[7], "|", board[8], "|", board[9])
    print("\n")


# display(theboard)

print("\n ")

def user1input():
    print("   ----------User-1----------\n")
    print("Select the position you want to Fill:(X)")
    row1=int(input())
    print("\n")
    return row1

def user2input():
    print("   ----------User-2----------\n")
    print("Select the position you want to Fill:(O)")
    row2 = int(input())
    print("\n")
    return row2


def updateuser1():
    global count
    r1=user1input()
    if r1<=9:
        print("Enter a Valid Number")
        turn = "X"
        if theboard[r1] == " ":
            theboard.update({r1: turn})
            count += 1
            display(theboard)

    elif r1>9:
        print("Position Invalid, Enter a ValidPosition")
        updateuser1()
    else:
        print("Position already Filled:")
        updateuser1()
    condition(count,theboard)
    # display(theboard)


def updateuser2():
    global count
    r2= user2input()
    if r2<=9:
        turn = "O"
        if theboard[r2] == " ":
            theboard.update({r2: turn})
            count += 1
            display(theboard)
    elif r2>9:
        print("Position Invalid, Enter a ValidPosition")
        updateuser2()
    else:
        print("Position already Filled:")
        updateuser2()
    condition(count,theboard)



win=False

def condition(count,theBoard):
    global win
    while count>=5 and count<=9:
        if count >= 5:
            if theBoard[1] == theBoard[2] == theBoard[3] != ' ':  # across the top
                display(theBoard)
                win=True
                break
            elif theBoard[4] == theBoard[5] == theBoard[6] != ' ':  # across the middle
                display(theBoard)
                win = True
                break
            elif theBoard[7] == theBoard[8] == theBoard[9] != ' ':  # across the bottom
                display(theBoard)
                win = True
                break
            elif theBoard[1] == theBoard[4] == theBoard[7] != ' ':  # down the left side
                display(theBoard)
                win = True
                break
            elif theBoard[2] == theBoard[5] == theBoard[8] != ' ':  # down the middle
                display(theBoard)
                win = True
                break
            elif theBoard[3] == theBoard[6] == theBoard[9] != ' ':  # down the right side
                display(theBoard)
                win = True
                break
            elif theBoard[1] == theBoard[5] == theBoard[9] != ' ':  # diagonal
                display(theBoard)
                win = True
                break
            elif theBoard[3] == theBoard[5] == theBoard[7] != ' ':  # diagonal
                display(theBoard)
                win = True
                break

            # if count==9 and win==False:
            #     print("Game Draw")

            break

def game():
    while win == False:
        updateuser1()
        # display(theboard)
        if count == 9 and win == False:
            print("----------------Game Draw----------------")
            break
        if win == True:
            print("----------------Game Over---------------- \n\n -------Congratulations: User-1 Won-----")
            break
        updateuser2()
        if count == 9 and win == False:
            print("----------------Game Draw----------------")
            break
        # display(theboard)
        if win == True:
            print("----------------Game Over---------------- \n\n -------Congratulations: User-2 Won-----")
            break


print("Hey Welcome to the TIC TAC TOE Game :)\n ")
display(theboard)
game()

print("\nThank You For Playing,Have a Great Day")

