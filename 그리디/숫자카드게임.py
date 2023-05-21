#숫자 카드 게임

n,m=map(int,input().split())

num_arr=[]
min_val=[]

for i in range(n):
    num_arr.append(list(map(int,input().split())))
    
for i in range(n):
    min_val.append(min(num_arr[i]))
    
print(max(min_val))
    
