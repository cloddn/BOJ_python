#이코테 화폐
n,goal=map(int,input().split())
n_array=[]
for i in range(n):
    n_array.append(int(input()))
    
d=[10001]*(goal+1)

d[0]=0
for i in range(n): #화폐 종류 하나씩 체크,
    for j in range(n_array[i],goal+1):#전체적으로 최솟값 갱신위해
        if d[j-n_array[i]]!=10001:
            d[j]=min(d[j],d[j-n_array[i]]+1)
            
        
if d[goal]==10001:
    print(-1)
else:
    print(d[goal])
