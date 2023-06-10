dis = [["A",0],["B",3],["C",4],["D",8],["E",9],["F",14],["G",23]]

p,q = input().split()
x = 0
y = 0

for i in range(7):
    if dis[i][0] == p:
        x = dis[i][1]
    if dis[i][0] == q:
        y = dis[i][1]

print(abs(x-y))
