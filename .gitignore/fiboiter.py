class fib1():
    def __init__(self):
        self.n1,self.n2 = 0,1
    def __iter__(self):
        return self
    def __next__(self):
        if count == 0:
            return self.n1
        self.n1,self.n2 = self.n2,self.n1+self.n2
        return self.n1

count = 0
n=10
y = fib1()
iter(y)
for i in y:
    if n<count:
        break
    print(i)
    count+=1
    
        
