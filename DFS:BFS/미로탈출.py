#BFS_미로탈출
from collections import deque

n,m=map(int,input().split())
graph=[list(map(int,input())) for i in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=deque()
    #시작 지점 담기
    queue.append((x,y))
    #큐가 빌때까지 반복
    while queue:
        #담아져있는거 pop
        x,y=queue.popleft() 
        #상하좌우 확인 - 한번에 한칸씩 이동 (종류별로 확인)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            #map 유효한 부분만 확인
            if nx < 0 or ny < 0 or nx >=n or ny >=m:
                continue
            #벽인 경우 무시 
            if graph[nx][ny]==0:
                continue
            #갈 수 있는 곳일 경우,
            if graph[nx][ny]==1:
                #최단거리 기록 
                graph[nx][ny]=graph[x][y]+1
                #이동한 다음 queue append
                queue.append((nx,ny))
    return graph[n-1][m-1] #가장 마지막 노드 확인 (여기까지 도착하)
    
    
print(bfs(0,0))
