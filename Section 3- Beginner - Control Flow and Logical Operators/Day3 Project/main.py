print('''     _ _                                 _ 
    | (_)                               | |
  __| |_  __ _ _ __ ___   ___  _ __   __| |
 / _` | |/ _` | '_ ` _ \ / _ \| '_ \ / _` |
| (_| | | (_| | | | | | | (_) | | | | (_| |
 \__,_|_|\__,_|_| |_| |_|\___/|_| |_|\__,_|''')
print(''' _     _                 _ 
(_)   | |               | |
 _ ___| | __ _ _ __   __| |
| / __| |/ _` | '_ \ / _` |
| \__ \ | (_| | | | | (_| |
|_|___/_|\__,_|_| |_|\__,_|\n''')
print('Welcome the Diamond Island\n')
print("Your mission is to find the biggest diamond in the world")
try:
    input("Press enter to continue")
except SyntaxError:
    pass

print('''      __________________
    .-'  \ _.-''-._ /  '-.
  .-/\   .'.      .'.   /\-.
 _'/  \.'   '.  .'   './  \'_
:======:======::======:======:  
 '. '.  \     ''     /  .' .'
   '. .  \   :  :   /  . .'
     '.'  \  '  '  /  '.'
       ':  \:    :/  :'
         '. \    / .'
           '.\  /.'    
             '\/''')

mountain = input(
    'You see 2 mountains. Which one will you go to? "left" or "right"\n')

if mountain == 'left':
    print(f'You selected {mountain}. -you have already smelled the diamond..')
    enterence = input(
        'It says "dangerous" at the entrance of the cave will you go inside? "yes" or "no"\n')
    if enterence == 'yes':
        print('You saw the cave plan. It consists of 3 floors. Which floor will you choose? 1, 2 or 3')
        floor = input('1, 2 or 3\n')
        if floor != "2":
            print('You fell into a bottomless pit and died in hunger and thirst.\n')
            print('Game Over')
        else:
            print(
                '\n\nCongratulations you did it. You found the apple. Yes apple... just it :( \n')
            print('''             .:'
         __ :'__
      .'`  `-'  ``.
     :             :
     :             :
      :           :
       `.__.-.__.''')
    else:
        print('On your way back you slipped and hit your head\n')
        print('Game Over')
else:
    print('''                
                       
             ##-------->  GAME OVER      
                   
                ''')
    print(
        f'You selected {mountain}. While on the road, you were shot by the locals with an arrow and bled to death... gg')
