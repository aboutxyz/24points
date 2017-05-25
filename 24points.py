#coding:utf-8
from itertools import permutations
operator = ["+","-","*","/"]

# a = int(raw_input("please input a single number: "))
# b = int(raw_input("please input a single number: "))
# c = int(raw_input("please input a single number: "))
# d = int(raw_input("please input a single number: "))

# numlist = [a,b,c,d]
# for i in permutations(numlist,4):
    # print i

test = [1,2,3,4]
strtest = ["1","2","3","4"]
strtest.insert(1,"+")
strtest.insert(3,"-")
strtest.insert(5,"+")
print eval("".join(strtest))
    
    


