# python tic tac toe by shironeko
import random
import re
import time
from os import system, name

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

player_list = ['O','X']
starting_player = random.choice(player_list)

if starting_player == 'O' :
  next_player = 'X'
else :
  next_player = 'O'

dot_list = ['0','1','2','3','4','5','6','7','8',]
dot_choosen_list = []
still_playing = True

def tictactoe(player_now) :

  while still_playing == True :

    print('| '+dot_list[0]+' | '+dot_list[1]+' | '+dot_list[2] + ' |')
    print("-------------")
    print('| '+dot_list[3]+' | '+dot_list[4]+' | '+dot_list[5] + ' |')
    print("-------------")
    print('| '+dot_list[6]+' | '+dot_list[7]+' | '+dot_list[8] + ' |' +'\n')

    number_choosen = input(player_now + ' choose ur number (between 0 - 8) : ')
    
    if int(number_choosen) <=8 and int(number_choosen) >= 0 and int(number_choosen) not in (dot_choosen_list) :
      
      dot_list[int(number_choosen)] = player_now
      dot_choosen_list.append(int(number_choosen))
      clear()
      
      if player_now == starting_player :
        tictactoe(next_player)
      else :
        tictactoe(starting_player)

    elif int(number_choosen) <=8 and int(number_choosen) >= 0 and int(number_choosen) in (dot_choosen_list) :

      print('\nthat spot already choosen. Try again!')
      time.sleep(1)
      clear()

    else :
      print('ur input is invalid')
      exit()

    

tictactoe(starting_player)
