n = 5
for i in range(n):
    for x in range(n-i-1):
        print(" ",end=" ")
    for y in range(i):
        print("*",end=" ")
    for z in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for x in range(i+1):
        print(" ",end=" ")
    for y in range(n-i-2):
        print("*",end=" ")
    for z in range(n-i-1):
        print("*",end=" ")
    print()
