n=input()
result=0
steps=[(-2,-1),(-2,1),(2,1),(-2,1),(-1,2),(-1,-2),(1,-2),(1,2)]
col=int(n[1])
row=int(ord(n[0]))- int(ord('a'))+1

for step in steps:
    next_row=row+step[0]
    next_col=col+step[1]
    
    if next_row <= 8 and next_row >= 1 and next_col <= 8 and next_col >= 1:
        result+=1
    
print(result)
