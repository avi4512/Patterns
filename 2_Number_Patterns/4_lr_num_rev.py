n = 5
p = 5
for i in range(n):
    for j in range(i+1):
        print(p,end=" ")
    p = p - 1
    print()

'''
5 
4 4 
3 3 3 
2 2 2 2 
1 1 1 1 1 
'''