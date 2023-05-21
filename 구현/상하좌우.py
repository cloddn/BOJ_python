#구현-상하좌우

n=int(input())
x,y=1,1 #초기 위치 지정
plans=list(input().split())

dx=[0,0,-1,1]
dy=[-1,1,0,0]
moves_type=['L','R','U','D']

for plan in plans:
    for i in range(len(moves_type)):
        if plan == moves_type[i]:
            nx=x+dx[i]
            ny=y+dy[i]
        
    if nx <1 or ny <1 or nx > n or ny > n :
        continue
        
    x=nx
    y=ny
    
print(x,y)
