import os
import sys
# liste and values for start the games,
xo="O" #value who is playing now X or Y - standard O start
turns = 0 # value of steps , strt 0 later stop on 8 because can only 9 steps in liste
list_cordinates=[[" "," "," "],[" "," "," "],[" "," "," "]] #liste 2D of games, here save chosed filed of X or O
def add_to_list(xy,xo): # add item X or O for filed , check if filed is empty or eary used
    x=int(xy[0])
    y=int(xy[1])
    if list_cordinates[x][y]==" ":
        list_cordinates[x][y] = xo
        print(list_cordinates[x][y])
    else:
        print(f'pozycja  {xy} jest zajęta {list_cordinates[x][y]}')
        main_game(xo, turns, list_cordinates)



def check_result_game(list_cordinates,xo): 
    #check everyone possible if a player win
    if xo==list_cordinates[0][0]==list_cordinates[0][1]==list_cordinates[0][2] or xo==list_cordinates[1][0]==list_cordinates[1][1]==list_cordinates[1][2] or xo==list_cordinates[2][0]==list_cordinates[2][1]==list_cordinates[2][2] or xo==list_cordinates[0][0]==list_cordinates[1][0]==list_cordinates[2][0] or xo==list_cordinates[0][1]==list_cordinates[1][1]==list_cordinates[2][1] or xo==list_cordinates[0][2]==list_cordinates[1][2]==list_cordinates[2][2] or xo==list_cordinates[0][0]==list_cordinates[1][1]==list_cordinates[2][2] or xo==list_cordinates[0][2]==list_cordinates[1][1]==list_cordinates[2][0]:
        print(f"Wygrywa {xo}")
        sys.exit(0)
def print_result_game(): #print result of array items fom list_cordinatins
    #os.system('clear')
    print("---0---1---2--X")
    print("0|",list_cordinates[0][0],"|",list_cordinates[0][1],"|",list_cordinates[0][2],"|")
    print("--------------")
    print("1|",list_cordinates[1][0],"|",list_cordinates[1][1],"|",list_cordinates[1][2],"|")
    print("--------------")
    print("2|",list_cordinates[2][0],"|",list_cordinates[2][1],"|",list_cordinates[2][2],"|")
    print("Y-------------")
def main_game(xo,turns,list_cordinates):# main cod  for games and use def add items , check result and print game
    list_cordinates=list_cordinates
    turns=turns
    print_result_game()
    while turns < 9 :
        print(f'Liczba ruchów: {turns +1}')
        if xo == "O":
            xy = input("Ruch O, podaj koordynanty xy: ")
            if xy[0]== "0" or xy[0]== "1" or xy[0]== "2" :
                if xy[1]== "0" or xy[1]== "1" or xy[1]== "2":
                    print(f'Wprowadzone koordynanty {xy}' )
                    add_to_list(xy,xo)
                    check_result_game(list_cordinates,xo)
                    print_result_game()
                    xo = "X"
                    print(f'Ilosc ruchow: {turns}')
                    turns += 1
                else:
                    print("Nieprawidłowy format Y")
                    main_game(xo,turns,list_cordinates)
            else:
                print("Nieprawidłowy format X")
                main_game(xo,turns,list_cordinates)

        else:
            xy = input("Ruch X, podaj koordynanty xy: ")
            if xy[0] == "0" or xy[0] == "1" or xy[0] == "2":
                if xy[1] == "0" or xy[1] == "1" or xy[1] == "2":
                    print(f'Wprowadzone koordynanty {xy}')
                    add_to_list(xy, xo)
                    check_result_game(list_cordinates, xo)
                    print_result_game()
                    xo = "O"
                    print(f'Ilosc ruchow: {turns}')
                    turns += 1
                else:
                    print("Niepoprawne koordynanty Y")
                    main_game(xo, turns, list_cordinates)
            else:
                print("Niepoprawne koordynanty X")
                main_game(xo, turns, list_cordinates)
    print("remis")
    sys.exit()
main_game(xo,turns,list_cordinates)
