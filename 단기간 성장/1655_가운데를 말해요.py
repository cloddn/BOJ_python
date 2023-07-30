import sys
import heapq

n=int(sys.stdin.readline())
leftHeap=[]
rightHeap=[]
result=[]

for i in range(n):
    num=int(sys.stdin.readline())


    if len(leftHeap)==len(rightHeap):
        heapq.heappush(leftHeap,-num)
        print(leftHeap)
    else:
        heapq.heappush(rightHeap, num)
        print(rightHeap)
     
    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])