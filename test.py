#coding:utf-8
from __future__ import division
from itertools import permutations,product
operator = ["+","-","*","/"]
# nums = raw_input()
# num = [int(i) for i in nums.split(',')]
# num = ["1","2","3","4"]
num = [3,3,8,8]
def cal(a, b, operator):
    return operator == '+' and float(a) + float(b) or operator == '-' and float(a) - float(b) or operator == '*' and  float(a) * float(b) or operator == '/' and float(a)/float(b)
#≥§∂»Œª1536
coml = product(permutations(num),operator,operator,operator)
all_num_list = list(permutations(num))
all_ops_list = list(product(operator,repeat = 3))
#  ((a1 op1 a2)op2 a3)op3 a4   (a3 op2(a1 op1 a2))op3 a4  a4 op3 ((a1 op1 a2) op2 a3)   a4 op3( a3 op2(a1 op1 a2))   (a1 op1 a2)op2 (a3op3 a4)
fmtlist = ["((%d%s%d)%s%d)%s%d", "(%d%s(%d%s%d))%s%d", "%d%s((%d%s%d)%s%d)", "%d%s(%d%s(%d%s%d))", "(%d%s%d)%s(%d%s%d)"]
result = []
def check(fmt, testroot):
    a, b, c, d = testroot[0]
    op1, op2, op3 = testroot[1], testroot[2], testroot[3]
    expr = fmt %(a, op1, b, op2, c, op3, d)
    try:
        cal()
for i in coml:
    check(fmtlist[1], i)
# for root in coml:
    # try:
        # val = root[0][0]
        # for fmt in fmtlist:
        
        # for i in range(1,4):
            # val = cal(val,root[0][i],root[i])
        # if 23.999<val<24.001:
            # result.append(root)
    # except:
        # pass