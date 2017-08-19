def conv(x):
                a = dict(s.split('=')for s in x.split(';'))
                return a;

d = str(input("enter input string :"))
f = conv(d)
print(f)
