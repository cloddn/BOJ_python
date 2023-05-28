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
