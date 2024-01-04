import numpy as np
import operator

scoreFile = './scores/nbaScoresClean.txt'

f = open(scoreFile,'r')
lines = f.readlines()
f.close()

numTeams = int(lines[0][10:])
C = np.zeros((numTeams, numTeams))
b = np.zeros((numTeams,1))
teams = {}

for i in range(numTeams):
    teams[lines[i+1][:-1]] = i

for x in range(numTeams+1, len(lines)):
    winner = lines[x][:20].strip()
    loser = lines[x][29:46].strip()

    C[teams[winner]][teams[winner]] += 1
    C[teams[loser]][teams[loser]] += 1

    C[teams[winner]][teams[loser]] -= 1
    C[teams[loser]][teams[winner]] -= 1

    b[teams[winner]] += 1
    b[teams[loser]] -= 1

for i in range(len(teams)):
    C[i][i] += 2
    b[i] = 1 + b[i]/2

C = np.matrix(C)
b = np.matrix(b)
CInverse = np.linalg.inv(C)

colley = np.matmul(CInverse, b)

ranks = {}
for team in teams:
    ranks[team] = colley[teams[team]]

sortedColley = sorted(ranks.items(), key = operator.itemgetter(1))
sortedColley.reverse()

template = "{0:20}|{1:10}"
print(template.format("Team","Colley Score"))

for team in sortedColley:
    print(template.format(team[0], float(team[1])))