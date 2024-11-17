'''
        1
      2 2 2
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
'''

n = 5
p = 1
for i in range(n):
    for x in range(n-i-1):
        print(" ",end=" ")
    for y in range(i):
        print(p,end=" ")
    for z in range(i+1):
        print(p,end=" ")
    p = p + 1
    print()
p = 4
for i in range(n):
    for x in range(i+1):
        print(" ",end=" ")
    for y in range(n-i-2):
        print(p,end=" ")
    for z in range(n-i-1):
        print(p,end=" ")
    p = p - 1
    print()
