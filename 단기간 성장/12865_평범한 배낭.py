import sys

#int형으로 입력받기
n,k=map(int,sys.stdin.readline().split())

thing=[[0,0]] #개당 정보 추가하는 용도
#2차원 배열 초기화 - 메모이제이션
d=[ [0] *(k+1) for _ in range(n+1)]

#결국 최대 가치를 구하는 문제 # 체크해야될 부분: 무게와 가치 -> 최대의 가치를 구해 max(i-1,new)
for i in range(n):
    thing.append(list(map(int,sys.stdin.readline().split())))

#해당 되는 부분들 다 체크
for i in range(1,n+1):
    for j in range(1,k+1):
        w = thing[i][0]
        v= thing[i][1]

        #가방에 넣을 수 없다면 -> 예전 값 그대로 (못 넣었으니까)
        if j < w :
            d[i][j]=d[i-1][j]
        else:
            d[i][j]=max(d[i-1][j],d[i-1][j-w]+v)
        

print(d[n][k])
    


# 물건을 배낭에 담을 때,
# ① 현재 배낭의 허용 무게보다 넣을 물건의 무게가 더 크다면 넣지 않는다.
# ② 그렇지 않다면, 다음 중 더 나은 가치를 선택하여 넣는다
#     2-1) 현재 넣을 물건의 무게만큼 배낭에서 뺀다. 그리고 현재 물건을 넣는다.
#     2-2) 현재 물건을 넣지않고 이전 배낭 그대로 가지고 간다.
 
# 위 과정을 식으로 나타내면 다음과 같다.
# 현재 담을 물건의 인덱스를 i, 현재 가방 허용 용량이 j, 현재 담을 물건의 무게를 weight, 가치 value라고 할 때,
# ① j < weight : d[i][j] = d[i-1][j]
# ② d[i][j] = max( d[i-1][ j-weight ]+value ), d[i-1][j] )