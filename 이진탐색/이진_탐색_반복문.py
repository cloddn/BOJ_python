def binary_search(array,start,end,target):
    while start <= end:
        mid = (start+end)//2
        if array(mid)==target:
            return mid
        elif array(mid)<target:
            start=mid+1

        else :
            end=mid-1
    return None #찾는 값 없을 경우 None


   ########공통########  
    

# n(원소의 개수)와 target(찾고자 하는 문자열)을 입력받기
n, target = list(map(int, input().split()))
# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    #index니까 +1
    print(result+1)
