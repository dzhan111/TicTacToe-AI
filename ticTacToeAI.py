board  = {1: 'X', 2: ' ', 3: ' ',
          4: ' ', 5: ' ', 6: ' ',
          7: ' ', 8: ' ', 9: ' '}

def printBoard(board):
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print("----------")
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print("----------")
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
   



def spaceIsFree(position):
    if(board[position] == ' '):
        return True
    else:
        return False


def insertLetter(letter, position):
    if(spaceIsFree(position)):
        board[position] = letter
        printBoard(board)
        #check win / draw

        if(checkDraw()):
            print("draw!")
        elif(checkWin()):
            if(letter == 'X'):
                print("X wins")
            else:
                print("O wins")
    else:
        print('space is full. choose new space')
        position = int(input("Enter new position: "))
        insertLetter(letter,position)
        return


def checkDraw():
    for key in board.keys():
        if(key == ' '):
            return False
        
    return True


def checkWin():
    #horizontal rows
    if(board[1] == board[2] and board[2] == board[3] and board[3] != " "):
        return True
    elif(board[4] == board[5] and board[5] == board[6] and board[6] != " "):
        return True
    elif(board[7] == board[8] and board[8] == board[9] and board[9] != " "):
        return True
    
    #vertical rows
    elif(board[1] == board[4] and board[4] == board[7] and board[7] != " "):
        return True
    elif(board[2] == board[5] and board[5] == board[8] and board[8] != " "):
        return True
    elif(board[3] == board[6] and board[6] == board[9] and board[9] != " "):
        return True
    
    #diagonals
    elif(board[1] == board[5] and board[5] == board[9] and board[9] != " "):
        return True
    elif(board[3] == board[5] and board[5] == board[7] and board[7] != " "):
        return True
    else:
        return False

