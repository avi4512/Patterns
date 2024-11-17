'''
        1
      1 2 1
    1 2 3 2 1
  1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
'''
n = 5
for i in range(n):

    for x in range(n-i-1):
        print(" ",end=" ")
    p = 1
    for y in range(i):
        print(p,end=" ")
        p = p + 1
    for z in range(i+1):
        print(p,end=" ")
        p = p - 1
    print()