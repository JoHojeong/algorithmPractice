N = int(input())
num = list()

for i in range(N):
    num.append(int(input()))
num.sort()

for k in num:
    print(k)