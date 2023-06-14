#미래 도시

#1. 초기설정
INF=int(1e9)
n,m=map(int,input().split())

#1. 처음 inf로 설정
graph=[[INF]*(n+1) for _ in range(n+1)]

#2. 자기 자신의 경로는 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

#3. 문제에 제시된 경로에 1 ** 집어넣기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    ####서로 반대되는 방향도 초기화해주기
    graph[b][a]=1

    
x,k=map(int,input().split()) #4. DP-> 경로 찾기
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
            
#5. 실제 주어진 경로에 대한 최소 경로 출력하기
distance=graph[1][k]+graph[k][x]

if distance>=INF:
    print(-1)
else:
    print(distance)
