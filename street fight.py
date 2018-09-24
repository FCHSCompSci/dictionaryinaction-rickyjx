

your_fighter = {
    'health': 100,
    'speed' : 10,
    'strenth' : 5,
    'curr_x' : 0,
    'curr_y' : 0, 
    }
boss_fight = {
    'health' : 500,
    'speed' : 3,
    'strenth' : 15,
    }

boss_moves = [ 50, 10, 30, 25]

move = input ("how would you like to move?")

while your_fighter['curr_y'] < 5:
    
        your_fighter['curr_y'] = your_fighter['curr_y'] +1
        print (your_fighter['curr_y'])
          
  
        
        your_fighter['curr_x'] = your_fighter['curr_x'] +1
        print (random.choice(boss_moves))
           
    elif move == "q":
        break
    elif move == "S":
        boss_fight['health'] = boss_fight['health'] - S
        print(boss_figth ['health'])
    
  
