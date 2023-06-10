H,W = map(int,input().split())
X = []
Y = []
for i in range(H):
    A = list(input())
    start_X=[]
    start_Y=[]
    for j in range(W):
        if A[j] == "#":
            start_X.append(j+1)
            start_Y.append(i+1)
    if len(start_X) != 0: 
        X.append(start_X)
    if len(start_Y) != 0:     
        Y.append(start_Y)

fX = len(X[0])
target_X = []
solve_Y = 0

for i in range(1,len(X)):
    if fX > len(X[i]):
        target_X = X[i]
        solve_Y = Y[i][0]
        if X[i][0] != X[0][0]:
            wh = "top"
            print(str(solve_Y)+ " "+ str(X[0][0]))
            exit()
        elif X[i][-1] != X[0][-1]:
            wh = "bottom"
            print(str(solve_Y)+ " "+ str(X[0][-1]))
            exit()
        break
    elif fX < len(X[i]):
        target_X = X[0]
        solve_Y = Y[0][0]
        if X[i][0] != X[0][0]:
            wh = "top"
            print(str(solve_Y)+ " "+ str(X[i][0]))
            exit()
        elif X[i][-1] != X[0][-1]:
            wh = "bottom"
            print(str(solve_Y)+ " "+ str(X[i][-1]))
            exit()
        break

arr = [i for i in range(target_X[0],target_X[-1]+1)]

solve_X = set(target_X) ^ set(arr)
k = list(solve_X)

print(str(solve_Y)+" "+str(k[0]))    

