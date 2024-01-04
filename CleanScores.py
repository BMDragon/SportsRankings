import numpy as np

scoreFile = './scores/nbascores.txt'
saveFile = './scores/nbaScoresClean.txt'

f = open(scoreFile,'r')
lines = f.readlines()
f.close()

teams = set()
for line in lines:
    winner = line[12:30].strip()
    loser = line[41:60].strip()
    teams.add(winner)
    teams.add(loser)

teams = sorted(teams)
print(teams)
sf = open(saveFile, 'w')
sf.write("NumTeams: " + str(len(teams)) + "\n")
for t in teams:
    sf.write(t + "\n")

for line in lines:
    sf.write(line[12:68] + "\n")

sf.close()