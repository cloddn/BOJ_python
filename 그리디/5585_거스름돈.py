n=1000-int(input())
result=0

coin_array=[500,100,50,10,5,1]

for coin in coin_array:
    result+=n//coin
    n%=coin
    
print(result)
