import sys

n=int(sys.stdin.readline())
_arr=[0]*10001 #10000보다 작은수로 주어짐
for i in range(n):
    num=int(sys.stdin.readline())
    _arr[num]+=1


for i in range(len(_arr)):
    #_arr에 숫자가 들어왔다면
    if _arr[i]!=0:
        #arm[num]에 있는 개수 만큼 출력
        for j in range(_arr[i]):
            print(i)
