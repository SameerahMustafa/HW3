#Sameerah Mustafa
#1584330
#HW3 CIS 2348

nums = input()
user_list = nums.split()

nList = []

for i in user_list:
    if int(i) >= 0:
        nList.append(int(i))

nList.sort()

for x in nList:
    print(x, end=' ')