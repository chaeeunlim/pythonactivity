#2739
a = int(input())
for i in range(1, 10):
    print(a, "*", i, "=", a*i)

#10950
T = int(input())
for i in range(1, 10):
    a = input().split()
    b = input().split()
    print(int(a)+int(b))

#8393
n = int(input())
sum = 0
for i in range(n+1):
    sum = sum + i
print(sum)

#15552
import sys
T = int(sys.stdin.readline())
for i in range(T):
    a, b = sys.stdin.readline().split()
    print(int(a)+int(b))

#2741
N = int(input())
for i in range(N):
    print(i+1)

#2742 기찍Nㅋㅋㅋㅋㅋㅋㅋ
N = int(input())
for i in range(N, 0, -1):
    print(i)

#11021
import sys
T = int(sys.stdin.readline())
for i in range(T):
    a, b = sys.stdin.readline().split()
    print('Case #'+int(i+1)+':'+(a+b))

#11022
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    n = a + b
    print("Case #%s: %s + %s = %s"%(i + 1, a, b, n))

#2438
N = int(input())
for i in range(1, N+1):
    print(" " * N-i + "*" * i)

#10871
N, X = int(input())
A = int(input())
for i in range(N):
    if X > A[i]:
        print(A[i], end='')


#while, 10952(런타임에러)
while(True):
    A, B = list(map(int, input().split()))
    print(A+B)

#1110
N = int(input())
C = N
new_N = 0
T = 0
count = 0
while True:
    T = N//10 + N%10
    new_N = (N%10)*10 + T%10
    count += 1
    N = new_N
    if new_N == C:
        break
print(count)

#15596 함수 한 문제는 저번 주에 풀었음
def solve(n):
    sum = 0
    for i in n:
        sum += i
    return sum

#4673(으아 이건 모르겄다)
natura1_number_set = set(range(1, 10001))
generated_number_set = set()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    generated_number_set.add(i)

self_number_set = natura1_number_set - generated_number_set

for i in sorted(self_number_set):
    print(i)