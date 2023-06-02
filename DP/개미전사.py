#이코테 DP 개미전사 
n=int(input())
n_list=list(map(int,input().split()))

d=[0]*100 #최대 식량 창고의 갯수가 100이니까
d[0]=n_list[0]
d[1]=max(d[0],n_list[1])
for i in range(2,n):
    d[i]=max(n_list[i]+d[i-2],d[i])

print(d[n-1])
