import random
from tracemalloc import stop
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
array = [rock, paper, scissors]
print(random.randint(0, 2))

selected = input(
    'What do you choose? Type 0 for Rock, 1 for Papier or 2 for Scissors\n')

print(f'You selected: {selected} \n')

if int(selected) > len(array)-1:
    print('please select 0 , 1 or 2')
else:
    selected = int(selected)
    print(array[selected])
    comp_selected = random.randint(0, 2)
    print(f'Computer choose: {comp_selected} \n')
    print(array[comp_selected])
    if selected == comp_selected:
        print('Draw')
    if selected == 0 and comp_selected == 1:
        print('You Lose')
    if selected == 0 and comp_selected == 2:
        print('You Win')
    if selected == 1 and comp_selected == 0:
        print('You Win')
    if selected == 0 and comp_selected == 1:
        print('You Lose')
    if selected == 0 and comp_selected == 1:
        print('You Lose')
    if selected == 2 and comp_selected == 1:
        print('You Win')
