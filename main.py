import os
import sys
xo="O"
ilosc_ruchow = 0
list_cordinates=[[" "," "," "],[" "," "," "],[" "," "," "]]
def add_to_list(xy,xo):

    x=int(xy[0])
    y=int(xy[1])
    if list_cordinates[x][y]==" ":
        list_cordinates[x][y] = xo
        print(list_cordinates[x][y])
    else:
        print(f'position  {xy} is  used early {list_cordinates[x][y]}')
        main_game(xo, ilosc_ruchow, list_cordinates)



def check_result_game(list_cordinates,xo):
    if xo==list_cordinates[0][0]==list_cordinates[0][1]==list_cordinates[0][2] or xo==list_cordinates[1][0]==list_cordinates[1][1]==list_cordinates[1][2] or xo==list_cordinates[2][0]==list_cordinates[2][1]==list_cordinates[2][2] or xo==list_cordinates[0][0]==list_cordinates[1][0]==list_cordinates[2][0] or xo==list_cordinates[0][1]==list_cordinates[1][1]==list_cordinates[2][1] or xo==list_cordinates[0][2]==list_cordinates[1][2]==list_cordinates[2][2] or xo==list_cordinates[0][0]==list_cordinates[1][1]==list_cordinates[2][2] or xo==list_cordinates[0][2]==list_cordinates[1][1]==list_cordinates[2][0]:
        print(f"win {xo}")
        sys.exit(0)
def print_result_game():
    #os.system('clear')
    print("---0---1---2--X")
    print("0|",list_cordinates[0][0],"|",list_cordinates[0][1],"|",list_cordinates[0][2],"|")
    print("--------------")
    print("1|",list_cordinates[1][0],"|",list_cordinates[1][1],"|",list_cordinates[1][2],"|")
    print("--------------")
    print("2|",list_cordinates[2][0],"|",list_cordinates[2][1],"|",list_cordinates[2][2],"|")
    print("Y-------------")
def main_game(xo,ilosc_ruchow,list_cordinates):
    list_cordinates=list_cordinates
    ilosc_ruchow=ilosc_ruchow
    print_result_game()
    while ilosc_ruchow < 9 :
        print(f'Który ruch jest wykonywany: {ilosc_ruchow +1}')
        if xo == "O":
            xy = input("Enter O your xy pole: ")
            if xy[0]== "0" or xy[0]== "1" or xy[0]== "2" :
                if xy[1]== "0" or xy[1]== "1" or xy[1]== "2":
                    print(f'Input poles {xy}' )
                    add_to_list(xy,xo)
                    check_result_game(list_cordinates,xo)
                    print_result_game()
                    xo = "X"
                    print(f'Ilosc ruchow: {ilosc_ruchow}')
                    ilosc_ruchow += 1
                else:
                    print("Wrong input Y")
                    main_game(xo,ilosc_ruchow,list_cordinates)
            else:
                print("Wrong input X")
                main_game(xo,ilosc_ruchow,list_cordinates)

        else:
            xy = input("Enter X your xy pole: ")
            if xy[0] == "0" or xy[0] == "1" or xy[0] == "2":
                if xy[1] == "0" or xy[1] == "1" or xy[1] == "2":
                    print(f'Input poles {xy}')
                    add_to_list(xy, xo)
                    check_result_game(list_cordinates, xo)
                    print_result_game()
                    xo = "O"
                    print(f'Ilosc ruchow: {ilosc_ruchow}')
                    ilosc_ruchow += 1
                else:
                    print("Wrong input Y")
                    main_game(xo, ilosc_ruchow, list_cordinates)
            else:
                print("Wrong input X")
                main_game(xo, ilosc_ruchow, list_cordinates)
    print("jeszcze nikt nie wygrał")
    sys.exit()
main_game(xo,ilosc_ruchow,list_cordinates)
