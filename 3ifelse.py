# 1330번
a, b  = list(map(int, input().split(' ')))
if(a > b):
    print('>')
elif(a < b):
    print('<')
else:
    print('==')

# 9498번
score = int(input())
if (90<=score<=100):
    print("A")
elif (80<=score<90):
    print("B")
elif (70<=score<80):
    print("C")
elif (60<=score<70):
    print("D")
else:
    print("F")

# 2753번
year = int(input())
if ((year %4 == 0) and (year %100 != 0 or year %400 == 0)):
    print(1)
else:
    print(0)

# 14681번 첫째풀이
x=int(input())
y=int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)

# 14681번 둘째풀이
x=int(input())
y=int(input())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)
        