'''
        1
      1 2 3
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
'''

n = 5
for i in range(n):
    p = 1
    for x in range(n-i-1):
        print(" ",end=" ")
    for y in range(i):
        print(p,end=" ")
        p = p + 1
    for z in range(i+1):
        print(p,end=" ")
        p = p + 1
    print()