#시각

n,m= map(int,input().split())
count=0

for i in range(n+1):
    if i <10 :
        i='0'+str(i)
    for k in range(60):
        if k <10:
            k='0'+str(k)
        for l in range(60):
            if l <10:
                l='0'+str(l)
            if str(m) in str(i)+str(k)+str(l):
                count+=1
                
print(count)
