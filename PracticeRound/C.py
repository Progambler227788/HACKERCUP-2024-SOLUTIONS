import random
import math
import sys
sys.stdout = open('output.txt','w')  
sys.stdin = open('fall_in_line_input.txt','r')
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solve(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    max_count = 0
    iterations = 100
    
    while iterations > 0:
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        
        # Ensure i and j are different
        while i == j:
            j = random.randint(0, n - 1)
        
        ct = 0
        x1, y1 = points[i]
        x2, y2 = points[j]
        
        for k in range(n):
            xk, yk = points[k]
            if (y2 - y1) * (xk - x1) == (yk - y1) * (x2 - x1):
                ct += 1
                
        max_count = max(max_count, ct)
        iterations -= 1
    
    print(f"Case #{t}: {n - max_count}")

def main():
    T = int(input())  # Number of test cases
    for t in range(1, T + 1):
        solve(t)

if __name__ == "__main__":
    main()
