def laba3(list1,a,b):
    list2 = []
    for i in list1:
        if i >= a and i <= b:
            list2.append(i)
    print(list2)
list1 = [i for i in range (101)]
a=-5
b=110
laba3(list1,a,b)