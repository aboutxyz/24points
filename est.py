def do_one_cal(a,b,sa,sb,op_num):
    if(op_num==0):
        return a+b, '('+sa+'+'+sb+')'
    elif op_num==2:
        return a-b,  '('+sa+'-'+sb+')'
    elif op_num==1:
        return a*b,  '('+sa+'*'+sb+')'
    elif op_num==3:
        if(b==0):
            return 0,None
    return 1.0*a/b, '('+sa+'/'+sb+')'
    
print do_one_cal(3,1,'4','5',3)