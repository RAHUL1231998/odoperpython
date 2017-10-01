try:
    with open('test.txt','r') as f:
        file_things = f.read()
except:
    print('PLEASE ENTER VALID FILE NAME!!!!!!')
else:
    print(file_things,end='')
    
