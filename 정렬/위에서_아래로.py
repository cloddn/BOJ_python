#정렬-위에서 아래로
m=int(input())
arr=[]

for i in range(m):
    arr.append(int(input()))


print(sorted(arr,reverse=True))
