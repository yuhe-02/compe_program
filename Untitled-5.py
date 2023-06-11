H,W = map(int,input().split())
A = []
x = []
y = []

for i in range(H):
    B = list(input())
    A.append(B)
    c = B.count("#")
    x.append(c)

for i in range(W):
    d = 0
    for j in range(H):
        if A[j][i] == "#":
            d += 1
    
    y.append(d)

#print(x)
#print(y)

xi = x.index(max(x)-1)+1
yi = y.index(max(y)-1)+1

print(str(yi)+" "+str(xi))
    
    