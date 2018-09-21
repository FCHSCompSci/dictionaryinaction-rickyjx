

your_fighter = {
    'health': 100,
    'speed' : 10,
    'strenth' : 5,
    'curr_x' : 0,
     'curr_' : 0, 
    }
boss_fight = {
    'health' : 500,
    'speed' : 3,
    'strenth' : 15,
    }
print ("p[ress 8 tp start")
boss_moves = [ 50, 10, 30, 25]
while your_fighter['health'] < 0:
    
    move = input ("Which way would you like to move? [S]lash [q] to quite")
    
    if move == 8:
        your_fighter['curr_y'] = your_fighter['curr_y'] +1
        print (random.choice(boss_moves))
    elif move == 6:
        your_fighter['curr_y'] = your_fighter['curr_y'] +1
        print (random.choice(boss_moves))
           
    elif move == "q":
        break
    elif move == "S":
        boss_fight['health'] = boss_fight['health'] - Q
        print(boss_figth ['health'])
    
