'''
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1
'''
n = 5
for i in range(n):
    p = 1
    for x in range(n-i):
        print("",end=" ")
    for j in range(i+1):
        print(p,end=" ")
        p = p + 1
    print()