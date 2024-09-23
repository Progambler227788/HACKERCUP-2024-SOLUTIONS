import sys
sys.stdout = open('output1.txt','w')  
sys.stdin = open('input1.txt','r')
def solveYES_NO(n,k,array):
    sorting = sorted(array,reverse=True)
    if n==1:
       return sorting[0] <=k 
    if n==2: # minimum is last
        return sorting[1] <=k 
     
    
    total = 0

    minimum = sorting[-1]
  
    #1st case
    total = minimum +  ( (minimum * 2) * (n-2) )
    # print(total)
    return total<=k

    #     # print('here')
    #     return True
    # r
    
    # # 2nd case
    # total = 0
   
    # if n%2==0:

     
    #    for i in range(1, len(sorting)):
    #        total += (sorting[i] *2)
    # else:
    #    for i in range(1, len(sorting) - 1):
    #        total += (sorting[i] *2)
    #    total += sorting[-1]
    
    
    # return total<=k
# 4 3 2 1
# 

# 4 3 1 -> 

# 10, 5 ,2 ,1 -> 1+1 ==2, 
# 10,9,9,9 -> 9+9, 9+9, 9,|  10,9,9 -> 9+9, 9
# 10,9,9,9,9


#[28, 20, 17, 16, 15]

#  15






#10 9 8
# 9+9, 8
#9+9, 8
#10,9,8
#10,9,8 
# 9, 8
# 9+9, 8

# 10,9,8,6
# 9,

for t in range(int(input())):
    n, k = map(int, input().split())
    array = []
    for i in range(n):
        array.append( int(input()) )
    if solveYES_NO(n,k,array):
        print(f"Case #{t+1}: YES")
    else:
        print(f"Case #{t+1}: NO")

    
    
            