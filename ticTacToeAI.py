board  = {1: ' ', 2: ' ', 3: ' ',
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
        print()
        printBoard(board)
        print()
        #check win / draw

        if(checkWin()):
            if(letter == 'X'):
                print("X wins")
            else:
                print("O wins")
            exit()
        if(checkDraw()):
            print("draw!")
            exit()
        
    else:
        print('space is full. choose new space')
        position = int(input("Enter new position: "))
        insertLetter(letter,position)
        return


def checkDraw():
    for value in board.values():
        if(value == ' '):
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



player = 'O'
comp = 'X'

def playerMove():
    position = int(input("Insert a position for O : "))
    insertLetter(player,position)
    return



#minimax algorithm

def compMove():
    #update these variables with the best move
    bestScore = -1000
    bestMove = 0

    #see all available moves
    for key in board.keys():
        if(board[key] == ' '):
            board[key] = comp
            score = minimax(board,0,False)
            #undo board
            board[key] = ' '

            #if current best move, update the bests
            if(score > bestScore):
                bestScore = score
                bestMove = key

    #at the end, insert letter at best move we found
    insertLetter(comp, bestMove)
    return


def minimax(board, depth, isMaximizing):
    if(checkWhoWon(comp)):
        return 1
    elif(checkWhoWon(player)):
        return -1
    elif(checkDraw()):
        return 0
    
    if(isMaximizing):
        #find the best score again, for this move
        bestScore = -100000

        #see all available moves from here
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = comp
                score = minimax(board,0,False)
                #undo move
                board[key] = ' '

                #if current best move, update the bests
                bestScore = max(score,bestScore)
        return bestScore

    #minimizing player
    else: 
        bestScore = 100000

        #see all available moves from here
        for key in board.keys():
            if(board[key] == ' '):
                board[key] = player
                score = minimax(board,0,True)
                #undo move
                board[key] = ' '

                #if current best move, update the bests
                bestScore = min(score,bestScore)
        return bestScore

    



def checkWhoWon(mark):
    #horizontal rows
    if(board[1] == board[2] and board[2] == board[3] and board[3] == mark):
        return True
    elif(board[4] == board[5] and board[5] == board[6] and board[6] == mark):
        return True
    elif(board[7] == board[8] and board[8] == board[9] and board[9] == mark):
        return True
    
    #vertical rows
    elif(board[1] == board[4] and board[4] == board[7] and board[7] == mark):
        return True
    elif(board[2] == board[5] and board[5] == board[8] and board[8] == mark):
        return True
    elif(board[3] == board[6] and board[6] == board[9] and board[9] == mark):
        return True
    
    #diagonals
    elif(board[1] == board[5] and board[5] == board[9] and board[9] == mark):
        return True
    elif(board[3] == board[5] and board[5] == board[7] and board[7] == mark):
        return True
    else:
        return False


# MAIN CODE
print()
print()
printBoard(board)
while not(checkWin()):
    
    playerMove()
    compMove()