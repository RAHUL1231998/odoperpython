dict ={'"key1"': '"val1"', '"key2"': '"val2"', '"key3"': '"val3"'}
S=" " 
for  i in dict:
 a=i
 b=dict[i]
 c=i+"="+dict[i]+';'
 S=S+c
print (S) 
