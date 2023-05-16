n,m = map(int, input().split()) 

s=[]

#시작 시점이 중요하므로 dfs(s) : 1부터 n까지 쓰는 것이 아니고 , 시작 지점부터 n까지 쓰기때문에
def dfs(start):


    if len(s)==m:
        print(" ".join(map(str,s)))
        return
    
    for i in range(1,n+1):
            s.append(i)
            dfs(i)
            s.pop()
            
dfs(1)
