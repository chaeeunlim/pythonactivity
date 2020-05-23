#1065
N_str = input()
number_of_hansu = 0
def f(a):
    if a < 100:
        return True
    elif 99< a < 1000:
        if (int(str(a)[1])-int(str(a)[0]) == int(str(a)[2])-int(str(a)[1])):
            return True

for b in range(1, int(N_str)+1):
    if f(b) == True:
        number_of_hansu += 1
print(number_of_hansu)

#2884
hour,minute = map(int, input().split())

if minute > 44:
    print(hour, minute-45)
elif minute <= 44 and hour >= 1:
    print(hour-1, minute+15)
else:
    print(23, minute+15)