#정렬-성적이 낮은 순서로 학생 출력하기
m=int(input())
arr=[]

for i in range(m):
    input_data=input().split()
    arr.append((input_data[0],int(input_data[1])))


array=sorted(arr,key=lambda arr:arr[1])
for student in array:
    print(student[0],end=' ')
