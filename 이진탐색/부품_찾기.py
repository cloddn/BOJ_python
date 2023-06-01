## 재귀함수 이용 (이진탐색)
def binary_search(start, end, data, target):
    mid = (start+end)//2
    if start >end:
        return None
    
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search(start, mid-1, data, target)
    else:
        return binary_search(mid+1, end, data, target)
        
N = 5
have = [8,3,7,9,2]

M=3
req = [5,7,9]

for target in req:
    r = binary_search(0,len(have)-1,have, target)
    if r == None:
        print ('no', end = ' ')
    else:
        print ('yes', end = ' ')


#이진탐색 - 부품 찾기
# 5
# 8 3 7 9 2
# 3
# 5 7 9

array_n=int(input())
array_list=list(map(int,input().split()))

target_n=int(input())
target_list=list(map(int,input().split()))

#정렬이 필요한지 체크할 것
array_list.sort()

def binary_search_tree(array,target,start,end):
    while (start<=end): #<=으로 해야 인덱스 끝까지 체크함.**** 
        mid=(start+end)//2
        if array_list[mid]==target:
            return mid
        elif array_list[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

#탐색을 target_n번 진행 O(nlogn)
for target in target_list:  
    x= binary_search_tree(array_list,target,0,array_n-1)
    if x==None:
        print("no",end=" ")
    else:
        print("yes",end=" ")
