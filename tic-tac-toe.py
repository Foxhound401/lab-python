theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'bot-L': ' ', 'bot-M': ' ', 'bot-R': ' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])

def checkWin(board, turn):
    if board['top-L'] == turn and board['top-M'] == turn and board['top-R'] == turn:
        print('win top row')
        return True
    elif board['mid-L'] == turn and board['mid-M'] == turn and board['mid-R'] == turn:
        print('win middle row')
        return True
    elif board['bot-L'] == turn and board['bot-M'] == turn and board['bot-R'] == turn:
        print('win bottom row')
        return True
    elif board['top-L'] == turn and board['mid-L'] == turn and board['bot-L'] == turn:
        print('win left col')
        return True
    elif board['top-M'] == turn and board['mid-M'] == turn and board['bot-M'] == turn:
        print('win middle col')
        return True
    elif board['top-R'] == turn and board['mid-R'] == turn and board['bot-R'] == turn:
        print('win right col')
        return True
    elif board['top-L'] == turn and board['mid-M'] == turn and board['bot-R'] == turn:
        print('win slash left to right')
        return True
    elif board['top-R'] == turn and board['mid-M'] == turn and board['bot-L'] == turn:
        print('win slash right to left')
        return True
    else: 
        return False

turn = 'X'
win = False
for i in range(9):
    # if win == True:
    #     print('Congratulation the winner is ' + turn)
    #     break

    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if checkWin(theBoard, turn):
        print("Congratunation " + turn + " win the match")
        break

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
