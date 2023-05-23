#정렬-두 배열의 원소 교체
m,n=map(int,input().split())
a_array=list(map(int,input().split()))
b_array=list(map(int,input().split()))

a_array.sort()
b_array.sort(reverse=True)

for i in range(n):
    a_array[i],b_array[i]=b_array[i],a_array[i]

print(sum(a_array))
