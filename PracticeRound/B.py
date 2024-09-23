import sys
sys.stdout = open('output.txt','w')  
sys.stdin = open('input.txt','r')

def solveIt(n,p):
  # divide by 100 gives us probability in decimal as there was 50% typed in example

    # P' =  (P/100) ^ (n-1/ n)
    # original -> n , one less -> n-1
    new_probability = ( p / 100.0 ) **  ((n - 1) / n)
    
 # * 100 ab islye krna h q k hamy explain m b 70 converted then from 0.7 form
    
    return (new_probability * 100 ) - p

for i in range( int(input())):
        n, p = map(int, input().split())
        print(f"Case #{i+1}: {solveIt(n, p):.16f}")
