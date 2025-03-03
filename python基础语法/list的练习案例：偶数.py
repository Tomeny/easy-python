# while循环
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist2 = []
index = 0
while index < len(mylist1):
    if mylist1[index] % 2 == 0:
        mylist2.append(mylist1[index])
    index += 1
print(mylist2)

# for循环
mylist1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mylist2 = []
for x in mylist1:
    if x % 2 == 0:
        mylist2.append(x)
print(mylist2)
