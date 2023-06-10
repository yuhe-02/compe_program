N = int(input())

K = N % 5

if K == 0:
    print(N)

elif K == 1:
    print(N-1)

elif K == 2:
    print(N-2)

elif K == 3:
    print(N+2)

elif K == 4:
    print(N+1)