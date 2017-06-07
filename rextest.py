#coding:utf-8
import re

expr = '(-56*)'
rex = re.match('[0-9\+\-\*\/\(\)]*', expr)
if rex.group() == expr:
    print "ok"
else:
    print "error"