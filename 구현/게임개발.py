# 구현 - 3. 게임 개발

n,m=list(map(int, input().split()))
x,y,direction=list(map(int, input().split()))

#방향에 따라 이동할 수 있는 종류에 대해 적기
dx=[1,0,-1,0]
dy=[0,1,0,-1]

#방문 유무를 구분하기 위해 d추가
d=[[0]*m for i in range(n)]
#맨처음 위치 방문 O
d[x][y]=1

#2차원 맵 초기화
array=[ list(map(int,input().split())) for i in range(n)]

def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

#방문셈을 위한 변수 - 맨처음 방문 노드
#turn time (왼쪽 회전 4번)
count=1
turn_time=0

while (True):
    #1) 왼쪽 방향부터 확인
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]
    
    #2) 앞에 전진 한칸 전진 ( 바다가 X, 방문X일 경우)
    if (d[nx][ny]==0) and (array[nx][ny] == 0):
        d[nx][ny]==1
        #현재 위치 업데이트
        x=nx
        y=ny
        count+=1
        turn_time=0 
        #그 다음 번의 반복문 체크 :
        #continue : 하위 코딩을 건너뛰고 다음 순번의 loop를 수행한다. 
        continue
    else:
        turn_left()
        turn_time+=1
        
    # 4방향 전부 확인해봤을때
    if turn_time==4:
        nx=x-dx[direction]
        ny=y-dy[direction]
        if  array[nx][ny] == 0:
            x=nx
            y=ny
            
        else:
            break
        turn_time=0
        
        
print(count)
