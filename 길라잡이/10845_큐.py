import sys
input=sys.stdin.readline

n=int(input())
queue_list=[]
for i in range(n):
    s=input().split()
    if s[0]=='push':
        queue_list.append(int(s[1]))
    elif s[0]=='pop':
        if len(queue_list)>0:
            print(queue_list.pop(0))
        else:
            print(-1)
    elif s[0]=='size':
        print(len(queue_list))
    elif s[0]=='empty':
        if len(queue_list)>0:
            print(0)
        else:
            print(1)
    elif s[0]=='front':
        if len(queue_list)>0:
            print(queue_list[0])
        else:
            print(-1)
    else:
        if len(queue_list)>0:
            print(queue_list[-1])
        else:
            print(-1)
