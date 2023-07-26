import sys

#int형으로 입력받기
n=int(sys.stdin.readline())
#숫자를 string 형태로 변환후 예제 출력과 같이 내림차순으로 출력
n=sorted(str(n),reverse=True)

#리스트를 하나의 문자열로 join후 int형으로 형변환
print(int(''.join(n)))
