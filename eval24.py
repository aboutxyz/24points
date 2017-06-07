#coding:utf-8
from __future__ import division
from itertools import permutations,product
import re
operator = ["+","-","*","/"]
# nums = raw_input()
# num = [int(i) for i in nums.split(',')]
# num = ["1","2","3","4"]
numlist = [1,1,5,5]
def cal(a, b, operator):
    return operator == '+' and float(a) + float(b) or operator == '-' and float(a) - float(b) or operator == '*' and  float(a) * float(b) or operator == '/' and float(a)/float(b)
#长度位1536
coml = product(permutations(numlist),operator,operator,operator)
all_num_list = list(permutations(numlist))
all_ops_list = list(product(operator,repeat = 3))
#五种括号形式
fmtlist = ["((%d%s%d)%s%d)%s%d", "(%d%s(%d%s%d))%s%d", "%d%s((%d%s%d)%s%d)", "%d%s(%d%s(%d%s%d))", "(%d%s%d)%s(%d%s%d)"]
result = []
def check(fmt, nums, ops):
    a, b, c, d = nums
    op1, op2, op3 = ops
    expr = fmt %(a, op1, b, op2, c, op3, d)
    rex = re.match('[0-9\+\-\*\/\(\)]*', expr)
    if rex.group() == expr:
        try:
            res = eval(expr)
        except ZeroDivisionError:
            return
        if 23.999<res<24.001:
            result.append(expr)
            print expr
    else:
        return

for j in set(all_num_list):        
    for op in all_ops_list:
        for fmt in fmtlist:
            check(fmt,j, op)
        
        
