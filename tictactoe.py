import random
from colorama import Fore
import time
def game_board():
      for i in range (3) :
            for j in range (3):
                  print(Fore.WHITE+game[i][j] , end=' ')
            print()   

def check():
      for i in range (3):
            if game[i][0]=='x' and game[i][1]=='x' and game[i][2]=='x': 
                  print('player1 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit()
            elif game[0][i]=='x' and game[1][i]=='x' and game[2][i]=='x': 
                  print('player1 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit()
            elif game[i][2]=='x' and game[i][1]=='x' and game[i][0]=='x': 
                  print('player1 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit() 
      
            elif game[0][0]=='x' and game[1][1]=='x' and game[2][2]=='x': 
                  print('player1 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit()  
       
      for i in range (3):
            if game[i][0]=='o' and game[i][1]=='o' and game[i][2]=='o': 
                  print('player2 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit()     
            elif game[0][i]=='o' and game[1][i]=='o' and game[2][i]=='o': 
                  print('player2 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit()
            elif game[i][2]=='o' and game[i][1]=='o' and game[i][0]=='o': 
                  print('player2 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit()             
      
            elif game[0][0]=='o' and game[1][1]=='o' and game[2][2]=='o': 
                  print('player2 wins')
                  print("Run Time: " + str( time.time() - start ))
                  exit()

      if game[0][0]!='_' and game[0][1]!='_'and game[0][2]!='_' and game[1][0]!='_' and game[1][1]!='_'and game[1][2]!='_' and game[2][0]!='_' and game[2][1]!='_'and game[2][2]!='_' :
                  print('draw') 
                  print("Run Time: " + str( time.time() - start ))
                  exit()    

      
game=[['_','_','_'],
      ['_','_','_'],
      ['_','_','_']]

p=int(input('two player or one player?'))
game_board()
start = time.time()
if p==1:
      while True:
            print(Fore.BLUE+'player1') 
            while True:   
                  row=random.randint(0,2)
                  col=random.randint(0,2)
                  if 0<= row <= 2 and 0<= col <= 2 :  
                        if game [row][col]=='_':
                              game [row][col]=Fore.BLUE+'x'
                              break
            game_board()
            check()  

            print(Fore.RED+'player2') 
            while True:     
                  row=int(input('which row?'))
                  col= int(input('which colmn?'))
                  if 0<= row <= 2 and 0<= col <= 2 : 
                        if game [row][col]=='_': 
                              game [row][col]=Fore.RED+'o'
                              break
                        else:
                              print('cell is not empty')
                  else:
                        print('try again')
            game_board()  
            check()
    
if p==2:
      while True:
            print(Fore.BLUE+'player1') 
            while True:   
                  row=int(input('which row?'))
                  col= int(input('which colmn?'))
                  if 0<= row <= 2 and 0<= col <= 2 :  
                        if game [row][col]=='_':
                              game [row][col]=Fore.BLUE+'x'
                              break
                        else:
                              print('cell is not empty')

                  else:
                        print('try again')
            game_board()
            check()  

            print(Fore.RED+'player2') 
            while True:     
                  row=int(input('which row?'))
                  col= int(input('which colmn?'))
                  if 0<= row <= 2 and 0<= col <= 2 : 
                        if game [row][col]=='_': 
                              game [row][col]=Fore.RED+'o'
                              break
                        else:
                              print('cell is not empty')
                  else:
                        print('try again')
            game_board()  
            check()    
else:
      print('erorr! just inter 1 or 2') 

         

           
