#전보
import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)#무한을 의미하는 값

#노드의 갯수, 간선의 갯수, 시작 노드
n,m,start=map(int,input().split())
graph=[[]for i in range(n+1)]
distance =[INF]*(n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))
    
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q: #큐가 비어있다면
        dist,now = heapq,heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            cost=dist+ i[1]
            #현재 노드를 거쳐서 , 다른 노드로 이동하는 거리가 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
                
dijkstra(start)

count=0

max_distance=0
for d in distance:
    if d!=INF:
        count+=1
        max_distance=max(max_distance,d)
        
print(count-1,max_distance)
