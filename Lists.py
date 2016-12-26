#the lists in python should be include inside the [] , thats how python understands that ,it is working on the lists
players = [12,56,78,99,102]
#print the third player, the index starts from 0 , so
print(players[2])
#assign new values to fouth player
players[3] = 88
#print players
print(players)
#the below expression just prints the value, but not append to them
print(players + [11,33,44])
#print the values
print(players)
#append new values
players.append(1234)
#print the values
print(players)
#get the players from first to thirs position
print(players[:3])
#print the players from third to fourth
print(players[2:4])
#assign new values to the list fot 1st and second positions
players[:2] = [3,4]
print(players)
#emplyt the first two values
players[:2] = []
print(players)
#empty the whole list
players[:]= []
print(players)

