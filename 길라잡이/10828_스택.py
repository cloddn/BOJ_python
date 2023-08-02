import sys
input=sys.stdin.readline
k=int(input())

stackList=[]
for i in range(k):
    s=input().split()
    if s[0]=='push':
        stackList.append(s[1])
    elif s[0]=='top':
        if len(stackList)==0:
            print(-1)
        else:
            print(stackList[-1])
    elif s[0]=='size':
        print(len(stackList))
    elif s[0]=='empty':
        if len(stackList)==0:
            print(1)
        else:
            print(0)
    else:
        if len(stackList)>0:
            print(stackList.pop())  
        else:
            print(-1)
        
