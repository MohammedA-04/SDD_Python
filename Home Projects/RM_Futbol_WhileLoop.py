# Futbol While Loop - Captains Randomly Select Players...

# import random, enables you to return random values
import random
Available_Players = ['Anastasia', 'Eli', 'Jamal',
'Jada', 'Theo', 'Michelle', 'Adam', 'Rhea', 'Charlie',
'Jasmine', 'Marley', 'Kenji', 'Sydney', 'Yara']

Jaleesas_team = ['Jaleesa']
Rahims_Team = ['Rahim']
# random.choice() function in your program
while len(Jaleesas_team) < 8:
    Player_Selected = random.choice(Available_Players)
    Jaleesas_team.append(Player_Selected)
    Available_Players.remove(Player_Selected)

Rahims_Team.extend(Available_Players)

print("Jalees`s Team")
print(*Jaleesas_team, sep = " , ")
print()
print("Rahim`s Team")
print(*Rahims_Team, sep = " , ")



