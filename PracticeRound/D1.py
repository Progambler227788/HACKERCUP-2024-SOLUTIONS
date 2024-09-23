import sys
sys.stdout = open('output.txt','w')  
sys.stdin = open('input.txt','r')
def solveIt(n,goal,energies):
    reverse = False
    for energy in range(1,len(energies)):
        if energies[energy-1] < energies[energy]:
           reverse = True
    if reverse:
       energies = sorted(energies,reverse=True)

    equalIndex = n
    equalDiff = float('inf')
    for key,position in enumerate(energies):
        temp = abs(position - goal)
        if temp == equalDiff:
           if key < equalIndex:
              equalIndex = key
           equalDiff = temp
        elif temp < equalDiff:
            equalIndex = key
            equalDiff = temp
    return equalIndex,equalDiff

for t in range(int(input())):
    n, goal= map(int, input().split())
    energies = []
    for i in range(n):
        energies.append( int(input()) )
    a,b =solveIt(n,goal,energies)
    print(f"Case #{t+1}: {a+1} {b}")