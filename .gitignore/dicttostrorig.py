def dict_conv(s):
    S=" "
    for  i in s:
         a=i
         b=d[i]
         c=i+"="+d[i]+';'
         S=S+c
    return S     


d ={'"key1"': '"val1"', '"key2"': '"val2"', '"key3"': '"val3"'}
print(dict_conv(d)) 
