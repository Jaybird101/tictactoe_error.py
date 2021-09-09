"""tictactoe game for 2 players"""
choices = [] # creates the choices list to append into
for x in range(1, 10): # adjust range from 9 to 10 to include enough for 9 spaces
    choices.append(str(x)) # turns x into a string before appending as it needs to be a string

playerOneTurn = True # removed one equals sign as it is not needed
winner = False


def printBoard():
    print('\n -----')
    print('|' + choices[0] + '|' + choices[1] + '|' + choices[2] + '|')
    print(' -----')
    print('|' + choices[3] + '|' + choices[4] + '|' + choices[5] + '|')
    print(' -----')
    print('|' + choices[6] + '|' + choices[7] + '|' + choices[8] + '|')
    print(' -----\n')


while not winner: # added not so the game plays as long as there is no winner
    printBoard() # lower cased the p to match the existing function

    if playerOneTurn :
        print("Player 1:")
    else :
        print("Player 2:")

    try:
        choice = int(input(">> "))
    except:
        print("please enter a valid field")
        continue

    if choices[choice - 1] == 'X' or choices[choice-1] == 'O': # added a = before the 'X' as it was needed ; added a -1 to make sure the index is in the range
        print("illegal move, please try again")
        continue

    if playerOneTurn:
        choices[choice - 1] = 'X'
    else :
        choices[choice - 1] = 'O' # make both X and 0 strings

    playerOneTurn = not playerOneTurn

    for x in range(0, 3):
        y = x * 3 # fixed indentation
        if (choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]):
            winner = True
            printBoard()
        if (choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]):
            winner = True
            printBoard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or
       (choices[2] == choices[4] and choices[4] == choices[6])) :
        winner = True # fixed capitalization to make True a boolean
        printBoard()

print ("Player " + str(int(playerOneTurn + 1)) + " wins!\n")