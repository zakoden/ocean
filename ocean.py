import random
from os import system
from time import sleep 

def clear(): 
    system('cls') 

SIZE = 16
EMPTY_CELL = 0
ROCK_CELL = 1
FISH_CELL = 2
SHRIMP_CELL = 3

ocean = [[0] * (SIZE + 2) for i in range(SIZE + 2)]
temp_ocean = ocean.copy()

def generate_ocean():
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            rand_val = random.randint(1, 20)
            if (rand_val <= 1):
                ocean[i][j] = ROCK_CELL
            elif (rand_val <= 6):
                ocean[i][j] = FISH_CELL
            elif (rand_val <= 11):
                ocean[i][j] = SHRIMP_CELL
            else:
                ocean[i][j] = EMPTY_CELL
            
def print_ocean():
    for i in range(1, SIZE + 1):
        s = ''
        for j in range(1, SIZE + 1):
            if (ocean[i][j] == SHRIMP_CELL):
                s += '+'
            elif (ocean[i][j] == ROCK_CELL):
                s += '#'   
            elif (ocean[i][j] == FISH_CELL):
                s += '*'       
            else:
                s += '.'
        print(s)
        

dx = [-1,-1,-1, 0, 1, 1, 1, 0]
dy = [ 1, 0,-1,-1,-1, 0, 1, 1]

def count_obj_around(x, y, obj):
    cnt = 0
    for v in range(8):
        tx = x + dx[v]
        ty = y + dy[v]
        if (temp_ocean[ty][tx] == obj):
            cnt += 1
    return cnt  
        
def next_ocean_state():
    temp_ocean = ocean.copy()
            
    for i in range(1, SIZE + 1):
        for j in range(1, SIZE + 1):
            if (temp_ocean[i][j] == SHRIMP_CELL):
                around = count_obj_around(j, i, SHRIMP_CELL)
                if ((2 <= around) and (around <= 3)):
                    ocean[i][j] = SHRIMP_CELL  # SHRIMP still alive
                else:
                    ocean[i][j] = EMPTY_CELL   # SHRIMP dies
            elif (temp_ocean[i][j] == ROCK_CELL):
                ocean[i][j] = ROCK_CELL
            elif (temp_ocean[i][j] == FISH_CELL):
                around = count_obj_around(j, i, FISH_CELL)
                if ((2 <= around) and (around <= 3)):
                    ocean[i][j] = FISH_CELL  # fish still alive
                else:
                    ocean[i][j] = EMPTY_CELL # fish dies
            else:
                cnt_fish = count_obj_around(j, i, FISH_CELL)
                if (cnt_fish == 3):
                    ocean[i][j] = FISH_CELL # create fish
                else:
                    cnt_shrimp = count_obj_around(j, i, SHRIMP_CELL)
                    if (cnt_shrimp == 3):
                        ocean[i][j] = SHRIMP_CELL # create shrimp
                    else:
                        ocean[i][j] = EMPTY_CELL 


generate_ocean()
while True:
    clear()
    print_ocean()
    next_ocean_state()
    sleep(2)