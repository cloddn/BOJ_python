import sys

#input()을 쓰면 시간초과가 나오길래 sys.stdin.readline()으로 수정

#오름 차순 정렬하기 - 힙정렬? binary 정렬?
n=int(sys.stdin.readline())
number_list=[]
for i in range(n):
    number_list.append(int(sys.stdin.readline()))
#Return값 None : 원본 값이 수정됨
number_list.sort()
for i in number_list:
    print(i)
