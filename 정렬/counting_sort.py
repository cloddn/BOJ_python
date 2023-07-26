#수의 범위가 작다면, 카운팅 정렬시 빠르게 정렬할 수 있음
def counting_sort(list,s_list):
    cnt=[0] * max(list)+1 #최댓값 +1 초기화
    
    #각 항목의 개수 저장
    for i in list:
        cnt[i]+=1
    
    #오름차순  # 카운팅 배열 누적합만들기
    for idx in range(1,len(cnt)):
        cnt[idx]+=cnt[idx-1]
    #내림차순 
    #for idx in range(len(cnt)-2, -1,-1):
    #    cnt[idx]+=cnt[idx+1]

    #적절한 곳에 배치 
    for j in range(len(list)-1,-1,-1):
        s_list[cnt[list[j]-1]]=list[j]
        cnt[list[j]]-=1 #