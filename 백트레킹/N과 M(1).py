n,m = map(int, input().split()) 

s=[]

def dfs():

    
    if len(s)==m:
        print(" ".join(map(str,s))) #s에 필요한 갯수 m개 다 넣으면 -> join(map(str,s))-> 1 3 출력되도록
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs() #맨처음 1 2 나올때까지
            s.pop()         
            
dfs()
