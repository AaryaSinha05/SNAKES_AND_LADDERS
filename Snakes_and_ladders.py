#snakes and ladders -
import random

#this function block checks if the player has landed at the top of a snake
def snakes_check(position):
    new_position_dict = {44 : 22, 46 : 5, 48 : 9, 52 : 11, 55 : 7, 59 : 17, 64 : 36, 69 : 39, 73 : 1, 83 : 19, 92 : 51, 95 : 24, 98 : 28}
    if position in new_position_dict:
        print("OPPS! There is a snake.")
        print()
        return new_position_dict[position]
    else:
        return position

#this function blocks checks if the player has landed at the end of the ladder
def ladders_check(position):
    new_position_dict = {8 : 26, 21 : 82, 43 : 77, 50 : 91, 54 : 93, 62 : 96, 66 : 87, 80 : 100}
    if position in new_position_dict:
        print("COOL! There is a ladder.")
        print()
        return new_position_dict[position]
    else:
        return position

#This function block returns a random number between 1 - 6 
def dice_roll():
    return (random.randint(1,6))

#This function block prints the scores and this is only for computer vs player mode.
def show_current_position(player_name,dpoints):
    print("-------------------- CURRENT POSITIONS --------------------")
    print(player_name + " : " + str(dpoints[1]))
    print("COMPUTER : ", dpoints[2])
    print()
    print()

#FUNCTION block for computer vs player mode
def computer_vs_player():

    end = 100

    player_name = input("enter your name : ")
    print()
    print("Hello, ",player_name)
    print()

    dpoints={}
    for i in range(2):
        if (i+1) not in dpoints:
            dpoints[i+1] = 0
    turn = 0
    while True:
        if turn%2 == 0:
            print("Its your turn, "+player_name)
            rinput = input("enter any character for your move : ")
            move = dice_roll()
            print("the dice shows the number ", move)
            print()
            dpoints[1] += move
            dpoints[1] = snakes_check(dpoints[1])
            dpoints[1] = ladders_check(dpoints[1])
            if dpoints[1] >= 100:
                dpoints[1] = 100
            show_current_position(player_name,dpoints)
            if dpoints[1] == end:
                print("CONGRATS! YOU HAVE WON THE GAME... :)")
                break
        else:
            move = dice_roll()
            print("It's the computer's turn and the dice shows the number ",move)
            print()
            dpoints[2] += move
            dpoints[2] = snakes_check(dpoints[2])
            dpoints[2] = ladders_check(dpoints[2])
            if dpoints[2] >= 100:
                dpoints[2] = 100
            show_current_position(player_name,dpoints)
            if dpoints[2] == end:
                print("Better luck next time! :') ")
                break
        
        turn += 1

def show_cposition(lnames, dpoints):
    print("-------------------- CURRENT POSITIONS --------------------")
    for i in lnames:
        print(i + " : " + str(dpoints[i]))
    print()
    print()

#FUNCTION block for player vs player mode 
def player_vs_player(no_of_players):
    dpoints = {}
    lnames = []
    winners = []
    for i in range(no_of_players):
        print("enter the name of player "+ str(i+1)+" : ",end = "")
        name = input()
        dpoints[name] = 0  
        lnames.append(name)
        print()
    
    count = 0
    turn = lnames[count]
    while (1):
        print("It is your turn, "+turn)
        rinput = input("enter any character for your move : ")
        move = dice_roll()
        print("the dice shows the number ", move)
        print()
        dpoints[turn] += move
        dpoints[turn] = snakes_check(dpoints[turn])
        dpoints[turn] = ladders_check(dpoints[turn])
        if dpoints[turn] >= 100:
            dpoints[turn] = 100
        show_cposition(lnames, dpoints)

        if dpoints[turn] == 100:
            print("YES! " + turn + " has won the game :)) ")
            print()
            winners.append(turn)
            lnames.remove(turn)
            no_of_players -= 1
            del dpoints[turn]

            if len(lnames) == 1:
                break

        if (count<no_of_players-1):
            count += 1
        else:
            count = 0
        
        turn = lnames[count]
    
    print()
    print("THE RANK OF THE PLAYERS : ")
    j = 1
    for i in winners:
        print(str(j) + ". " + i)
        j += 1
    print(str(j)+ ". "+ lnames[0])
    print()
    print()


new = ""
print("Hello world!!")
print("Let's play snakes and ladders")
print()

while True :
    print("Let's start the game "+new+"...")
    print()
    print("Enter 1 for computer vs player and enter 2 for player vs player.")
    print()

    ask = int(input("Enter your choice : "))
    while(1):
        if ask not in [1,2] : 
            print("WARNING! ENTER A PROPER CHOICE.")
            ask = int(input("Enter your choice : "))
        else:
            break
    
    if ask == 2:
        no_of_players = int(input("Enter the number of players (1-8) : "))
        player_vs_player(no_of_players)

    else:
        computer_vs_player()
    

    ask1 = input("want to play again ?(y/n) : ")
    if ask1 == 'n' or ask1 == 'N':
        break
    else:
        new = "again "
        continue
