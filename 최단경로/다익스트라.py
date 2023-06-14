#다익스트라 알고리즘
import heapq
import sys

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
