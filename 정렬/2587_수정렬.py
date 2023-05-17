nums_list=[]
sum_nums=0

for i in range(5):
    nums_list.append(int(input()))
    
for i in nums_list:
    sum_nums+=i
nums_list.sort()  
print(int(sum_nums/len(nums_list)))
print(nums_list[len(nums_list)//2])
