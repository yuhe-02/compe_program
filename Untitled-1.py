import sys
input = sys.stdin.readline

N,K = map(int,input().split())
A = list(map(int,input().split()))

def check(x):
    sum = 0
    for i in range(N):
        sum += x // A[i]
    if sum >= K:
        return True
    else:    
        return False
 
def main():
    # 二分探索
    L = 1
    R = 1000000000
    while L < R:
        M = (L + R) // 2
        ans = check(M)
        if ans == False:
            L = M + 1
        if ans == True:
            R = M
    print(L)
  
if __name__ == '__main__':
    main() 
    
