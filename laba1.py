def laba1():
    a = '1,3,2,4,5,6,7,8'
    if '1,2,3' in a:
        print(True)
    elif '3,2,1' in a:
        print(True)
    elif '2,1,3' in a:
        print(True)
    elif '2,3,1' in a:
        print(True)
    elif '3,1,2' in a:
       print(True)
    elif '1,3,2' in a:
        print(True)
    else:
        print(False)
laba1()