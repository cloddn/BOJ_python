import sys


#시간 초과뜸- python / pypy3로 돌릴 것 / 최소 연쇄 행렬 곱셈

def solve():
    k=int(sys.stdin.readline())
    fileList=[0] + list(map(int,sys.stdin.readline().split()))
    #fileList.append(int(sys.stdin.readline()))
    sumList=[ [0] * (k+1) for _ in range(k+1)]

    for i in range(k+1):
        for j in range(k+1):
            if j==i+1: #연속되어있는 파일 더하기
                sumList[i][j]=fileList[i]+fileList[j]

    #sumList밑에서부터 위로 올라오면서 dp를 채워나간다 ***  

    for i in range(k-1,0, -1):
        for j in range(1,k+1):
            if sumList[i][j]==0 and j >i:
                sumList[i][j]=min([sumList[i][k]+sumList[k+1][j] for k in range(i,j)]) + sum(fileList[i:j+1]) #sum() 구성 조합 비용 다 더해주기 / min(가능한 조합수 중에 최솟값 찾기)
    print(sumList[1][k])

t=int(sys.stdin.readline())
for _ in range(t):
    solve()
