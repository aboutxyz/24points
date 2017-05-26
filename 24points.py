#coding:utf-8
from itertools import permutations,product
operator = ["+","-","*","/"]

# a = int(raw_input("please input a single number: "))
# b = int(raw_input("please input a single number: "))
# c = int(raw_input("please input a single number: "))
# d = int(raw_input("please input a single number: "))

# numlist = [a,b,c,d]
# for i in permutations(numlist,4):
    # print i

result = []
strtest = ["1","2","3","4"]
strtest.insert(1,"+")
strtest.insert(3,"+")
strtest.insert(5,"+")
for i in product(operator,repeat = 3):
    strtest[1] = i[0]
    strtest[3] = i[1]
    strtest[5] = i[2]
    print strtest
    try:
        if eval("".join(strtest))== 24:
            result.append(strtest)
    except:
        pass
        
print result
    
    


