n=int(input())
card=list(map(int,input().split()))

m=int(input())
check=list(map(int,input().split()))

card.sort()

def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2
        
        if array[mid]==target:
            return mid #index
        elif array[mid] >target:
            end= mid -1 #index
        else:
            start= mid +1 #index
            
    return None
    
for i in range(m):
    if binary_search(card,check[i],0, n-1) is not None:
        print(1,end=' ')
    else:
        print(0,end=' ')
            

#for i in range(s_n):
#    if s_m[i] in m: #순차 탐색은 시간초과가 나오기 때문
#        answer.append("1")
#        
#    else:
#        answer.append("0")
        
#print(' '.join(answer))
    
