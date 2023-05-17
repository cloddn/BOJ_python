n,m = map(int, input().split())

p_list =list(input().split())
int_list=[]

for i in range(n):
    int_list.append(int(p_list[i]))

int_list.sort(reverse=True)

print(int_list[m-1])
