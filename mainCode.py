theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'low-L':' ','low-M':' ','low-R':' '}
def printBoard():
    print(theBoard['top-L'] + ' | ' + theBoard['top-M'] + ' | ' + theBoard['top-R'])
    print("--+---+--")
    print(theBoard['mid-L'] + ' | ' + theBoard['mid-M'] + ' | ' + theBoard['mid-R'])
    print("--+---+--")
    print(theBoard['low-L'] + ' | ' + theBoard['low-M'] + ' | ' + theBoard['low-R'])

printBoard()
winner = ' '
block = 0
def enterIntoBoard(player,blockNumber):
    if player=='X':
        if blockNumber == 1:
            theBoard['top-L'] = 'X'
        elif blockNumber == 2:
            theBoard['top-M'] = 'X'
        elif blockNumber == 3:
            theBoard['top-R'] = 'X'
        elif blockNumber == 4:
            theBoard['mid-L'] = 'X'
        elif blockNumber == 5:
            theBoard['mid-M'] = 'X'
        elif blockNumber == 6:
            theBoard['mid-R'] = 'X'
        elif blockNumber == 7:
            theBoard['low-L'] = 'X'
        elif blockNumber == 8:
            theBoard['low-M'] = 'X'
        else:
            theBoard['low-R'] = 'X'
    else:
        if blockNumber == 1:
            theBoard['top-L'] = 'O'
        elif blockNumber == 2:
            theBoard['top-M'] = 'O'
        elif blockNumber == 3:
            theBoard['top-R'] = 'O'
        elif blockNumber == 4:
            theBoard['mid-L'] = 'O'
        elif blockNumber == 5:
            theBoard['mid-M'] = 'O'
        elif blockNumber == 6:
            theBoard['mid-R'] = 'O'
        elif blockNumber == 7:
            theBoard['low-L'] = 'O'
        elif blockNumber == 8:
            theBoard['low-M'] = 'O'
        else:
            theBoard['low-R'] = 'O'

def checkWinner():
    if theBoard['top-L'] =='X' and theBoard['top-M'] == 'X' and theBoard['top-R'] == 'X':
        winner = 'Player X'
    elif theBoard['mid-L'] =='X' and theBoard['mid-M'] == 'X' and theBoard['mid-R'] == 'X':
        winner = 'Player X'
    elif theBoard['low-L'] =='X' and theBoard['low-M'] == 'X' and theBoard['low-R'] == 'X':
        winner = 'Player X'
    elif theBoard['top-L'] =='O' and theBoard['top-M'] == 'O' and theBoard['top-O'] == 'X':
        winner = 'Player O'
    elif theBoard['mid-L'] =='O' and theBoard['mid-M'] == 'O' and theBoard['mid-R'] == 'O':
        winner = 'Player O'
    elif theBoard['low-L'] =='O' and theBoard['low-M'] == 'O' and theBoard['low-R'] == 'O':
        winner = 'Player O'
    elif theBoard['low-L'] =='X' and theBoard['mid-M'] == 'X' and theBoard['top-R'] == 'X':
        winner = 'Player X'
    elif theBoard['low-R'] =='X' and theBoard['mid-M'] == 'X' and theBoard['top-L'] == 'X':
        winner = 'Player X'
    elif theBoard['low-L'] =='O' and theBoard['mid-M'] == 'O' and theBoard['top-R'] == 'O':
        winner = 'Player O'
    elif theBoard['low-R'] =='O' and theBoard['mid-M'] == 'O' and theBoard['top-L'] == 'O':
        winner = 'Player O'
    elif theBoard['low-L'] =='X' and theBoard['mid-L'] == 'X' and theBoard['top-L'] == 'X':
        winner = 'Player X'
    elif theBoard['low-R'] =='X' and theBoard['mid-R'] == 'X' and theBoard['top-R'] == 'X':
        winner = 'Player X'
    elif theBoard['low-M'] =='X' and theBoard['mid-M'] == 'X' and theBoard['top-M'] =='X':
        winner = 'Player X'
    elif theBoard['low-L'] =='O' and theBoard['mid-L'] == 'O' and theBoard['top-L'] == 'O':
        winner = 'Player O'
    elif theBoard['low-R'] =='O' and theBoard['mid-R'] == 'O' and theBoard['top-R'] == 'O':
        winner = 'Player O'
    elif theBoard['low-M'] =='O' and theBoard['mid-M'] == 'O' and theBoard['top-M'] == 'O':
        winner = 'Player O'
    else:
        winner = 'No one'
    return winner
    

for i in range(0,9):
    if i%2 == 1:
        print('Player X enter a legal block number: ')
        block = int(input())
        enterIntoBoard('X',block)
        winner = checkWinner
        printBoard()
    else:
        print('Player O enter a legal block number: ')
        block = int(input())
        enterIntoBoard('O',block)
        winner = checkWinner
        printBoard()
    if(winner == 'Player X' or winner =='Player O'):
        print('The winner is ' + winner)
        break
    
    
