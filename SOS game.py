# Display board on screen.
def display_board():
    global board
    #board 4X4
    columns = 4
    rows = 4
    board = [[' ' for i in range (columns)] for j in range(rows)]
    #print  board 4X4
    for i in range(4):
        print(board[i])

#Get inputs from users.
def user_input():
    global column, row, play_input 
    #while true to check if the place that the user will put in the letters is full or not
    while True:
        while True:
            #while true to check the input if it is out of index or not
            while True:
                #try to check if the user inputs letters insted of numbers
                try:
                   row = int(input("Enter the row number: "))
                   break
                except:
                   print("Enter only numbers! ")
                   continue
            if row > 4 or row <1 :
                   print("Enter row between 1-4!")
                   continue
            else:
               break 
           
        while True :
            #while true to check the input if it is out of index or not
            while True:
            #try to check if the user inputs letters insted of numbers
                try:
                    column = int(input("Enter the column number: "))  
                    break
                except:
                   print("Enter only numbers!")
                   continue
            if column > 4 or column<1:
                print("Enter column between 1-4")
                continue
            else:
               break   
        if board[row-1][column-1] == 'S' or board[row-1][column-1] == 'O' :
            print("The place is full ,  Choose another place")
            continue
        else:
            break
    while True:
        #while true to check if user input S or O or not
        play_input = (input("Enter S or O: "))
        play_input = play_input.upper()
        if play_input!= 'S' and play_input !='O':
            print("Please enter only ' S ' or 'O ' " )
            continue
        else:
            break

#Update the board
def update(row,column,play_input):
    row -= 1
    column -= 1
    #put the letter in the sutible place
    if board [row][column] == ' ':
        board[row][column] = play_input
        for i in range(4):
            print(board[i])
            
#Check the score increase and all possible errors
def check_score(column , row , turn):
    column -= 1
    row -= 1
    global score1, score2
    if turn ==0:
        score1 =0
        score2= 0
    #if the input are O 
    if play_input == 'O':
    #try-except to pass the error out of index
        try:
             if ((board[row][column - 1] =='S') and (board[row][column + 1] =='S')) :
                 #if num of index is negative or not to pass this error
                 if column-1 >=0 :
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                 else:
                    pass
        except:
            pass
        try:
            if (board[row - 1][column] =='S') and (board[row + 1][column] =='S'):
                if  row-1>=0:
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
        try:
            if (board[row + 1][column - 1] =='S') and (board[row - 1][column+ 1] =='S'):
                if column-1 >=0 and row-1>=0:
                   if turn%2 == 0:
                       score1 += 1
                   else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
        try:
            if (board[row + 1][column + 1] =='S') and (board[row - 1][column- 1] =='S'):
                if column-1 >=0 and row-1>=0:
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
    if play_input == 'S' :
        try:
           if board[row][column+1]=='O' and board[row][column+2] == 'S':
                if turn%2 == 0:
                   score1 += 1
                else:
                   score2 += 1 
        except:
            pass
        try :
            if board[row][column-1]=='O' and board[row][column-2] == 'S' :
                if column-1 >=0 and column-2>=0:
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
        try :
            if board[row+1][column]=='O' and board[row+2][column] == 'S' :
                if turn%2 == 0:
                   score1 += 1
                else:
                   score2 += 1 
        except:
            pass
        try : 
            if board[row-1][column]=='O' and board[row-2][column] == 'S' :
                if  row-1>=0 and row-2>=0:
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
        try:
            if board[row+1][column+1]=='O' and board[row+2][column+2] == 'S' :
                if turn%2 == 0:
                   score1 += 1
                else:
                    score2 += 1 
        except:
            pass
        try:
            if board[row-1][column-1]=='O' and board[row-2][column-2] == 'S' :
                if column-1 >=0 and row-1>=0 and column-2>=0 and row-2>=0 :
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
        try :
            if board[row+1][column-1]=='O' and board[row+2][column-2] == 'S' :
                if column-1 >=0 and column-2>=0:
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
        try:
            if board[row-1][column+1]=='O' and board[row-2][column+2] == 'S':
                if row-1 >=0 and row-2>=0:
                    if turn%2 == 0:
                       score1 += 1
                    else:
                       score2 += 1 
                else:
                    pass
        except:
            pass
    print("Player1 score: ", score1, "Player2 score: ", score2)
#print turns of players
def turn():
    if counter < 16:
        if i%2 == 0:
            print("Player1 Turn")
        else:
            print("Player2 Turn")
#put scores in variable to use it in some funcations
#k = score1 , z = score2
display_board()
global k , Z , counter
counter = 0
z=0
k =0
#for loop to return the code in special cases
for i in range(50):
    turn()
    #counter to know when the game is end
    counter= counter + 1
    user_input()
    update(row,column,play_input)
    if i > 0 :
       k = score1
       z = score2L
    check_score(column , row , i)
    #if counter = 16 , the game will end
    if counter == 16:
        #if condition to know who is win
        if score1 > score2 :
            print("Player1 win!")
        elif score1 < score2:
            print("Player2 win!")
        elif score1 == score2 :
            print ("Draw!")
        break    
    #while loop to allow the winner to play again
    while score1 == k+1 or score2 == z+1:
        #save the old score
        k = score1
        z = score2
        turn()
        counter= counter + 1
        user_input()
        update(row,column,play_input)
        check_score(column , row , i)
        #to end loop to pass error if the last player in this while loop was winnig
        if counter ==15:
            break
    
    


    






        