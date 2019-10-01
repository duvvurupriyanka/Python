#board print
   
pattern = {1:" ", 2: "|", 3:"_", "pos1": 1, "pos2": 2, "pos3": 3, "pos4": 4, "pos5": 5, "pos6": 6,
           "pos7": 7, "pos8": 8, "pos9": 9}
row_list ={1:[1,1,1,2,1,1,1,2,1,1,1], 2:[1,"pos1",1,2,1,"pos2",1,2,1,"pos3",1], 3:[3,3,3,1,3,3,3,1,3,3,3],
           4:[1,"pos4",1,2,1,"pos5",1,2,1,"pos6",1], 5:[1,"pos7",1,2,1,"pos8",1,2,1,"pos9",1]}
board = {'b':[1,2,1,3,1,4,1,3,1,5,1]}

def tic_tac_toe():
    tic_tac_toe = False
    if pattern['pos1'] == pattern['pos4'] and pattern['pos4'] == pattern['pos7']:
        print(f'{player} win the game!')
    elif pattern['pos1'] == pattern['pos5'] and pattern['pos5'] == pattern['pos9']:
        print(f'{player} win the game!')
    elif pattern['pos1'] == pattern['pos2'] and pattern['pos2'] == pattern['pos3']:
        print(f'{player} win the game!')
    elif pattern['pos2'] == pattern['pos5'] and pattern['pos5'] == pattern['pos8']:
        print(f'{player} win the game!')
    elif pattern['pos3'] == pattern['pos6'] and pattern['pos6'] == pattern['pos9']:
        print(f'{player} win the game!')
    elif pattern['pos3'] == pattern['pos5'] and pattern['pos5'] == pattern['pos7']:
        print(f'{player} win the game!')
    elif pattern['pos4'] == pattern['pos5'] and pattern['pos5'] == pattern['pos6']:
        print(f'{player} win the game!') 
    elif pattern['pos7'] == pattern['pos8'] and pattern['pos8'] == pattern['pos9']:
        print(f'{player} win the game!')
    else:
        tic_tac_toe = True
    return tic_tac_toe
        
def pattern_change(num,player):    
    for key,value in pattern.items():
        if (value == num) and player == 'player1':
            pattern[key] = player1_symbol
            board_print()
            break
        elif (value == num) and player == 'player2':
            pattern[key] = player2_symbol
            board_print()
            break
        else:
            continue
            
def board_print():
    for b in board['b']:
        for r in row_list[b]:
            print(pattern[r], end ='')
        print('\n', end = '')

        
        
player_list = []
valid = True
#taking the symbol
while valid:
    player1_symbol = str(input("Select the symbol x or o :"))
    if (player1_symbol.lower() == 'x'):
        print("player 1 with x")
        player2_symbol = 'o'
        print("player 2 with o")
        valid = False
    elif (player1_symbol.lower() == 'o'):
        print("player 1 with o")
        player2_symbol = 'x'
        print("player 2 with x")
        valid = False
    else:
        print('please select the correct option')
        
#display the initial board       
board_print()

#validating the number of inputs
while len(player_list) != 9 and tic_tac_toe():
#deciding the player
    if len(player_list) % 2 == 0:
        player = "player1"
    else:
        player = "player2"
#taking the input
    while True:
        try:
            select_in = int(input("{} Enter your choice:".format(player)))
        except:
            print("wrong input. Please enter between 1 and 9")
            continue
        else:
            #input validation    
            if 1 <= select_in <= 9 and select_in not in player_list:
                player_list.append(select_in)
                pattern_change(select_in, player)
                break
            else:
                print("wrong poisition. please check your position")
                continue