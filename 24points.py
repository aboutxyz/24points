#coding:utf-8
from __future__ import division
from itertools import permutations,product
operator = ["+","-","*","/"]
# nums = raw_input()
# num = [int(i) for i in nums.split(',')]
# num = ["1","2","3","4"]
num = [3,3,8,8]
#长度位1536
coml = product(permutations(num),operator,operator,operator)
# cal = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x/y}
def cal(a, b, operator):
    return operator == '+' and float(a) + float(b) or operator == '-' and float(a) - float(b) or operator == '*' and  float(a) * float(b) or operator == '/' and float(a)/float(b)
# all_num_list = list(permutations(num))
# all_ops_list = list(product(operator,repeat = 3))
result = []
# for root in coml:
    # try:
        # val = root[0][0]
        # for i in range(1,4):
            # val = cal(val,root[0][i],root[i])
        # if 23.999<val<24.001:
            # result.append(root)
    # except:
        # pass

for root in coml:
    try:
        val = root[0][0]
        val = cal(val,root[0][1],root[1])
        val1 = cal(val,root[0][2],root[2])
        val2 = cal(root[0][2],val,root[2])
        for i in [val1,val2]:
            val = cal(i,root[0][3],root[3])
            if 23.999<val<24.001:
                result.append(root)
        for i in [val1,val2]:
            val = cal(root[0][3],i,root[3])
            if 23.999<val<24.001:
                result.append(root)
    except:
        pass

print set(result)
