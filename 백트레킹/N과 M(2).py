n,m = map(int, input().split()) 
s=[]
#시작 시점이 중요하므로 dfs(s) : 1부터 n까지 쓰는 것이 아니고 , 시작 지점부터 n까지 쓰기때문에
def dfs(start):
    if len(s)==m:
        print(" ".join(map(str,s)))
        return
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i)
            dfs(i+1) #다음 차례 dfs 넣어주기
            s.pop()
        
dfs(1)
