# create list and use different functions
 
my_list = [3,9,7,12,8,2,5]
print(len(my_list))
print(my_list)


# add 10 as 8th element to the list
my_list.append(10)
print(len(my_list))
print(my_list)


# insert 1 as the 3rd element in the list
# index value starts from 0
my_list.insert(2,1)
print(len(my_list))
print(my_list)


# create enmpty list and add elements using for loop and append function
my_new_list = []
for i in range(5):
    my_new_list.append(i+1)
print(my_new_list)    


# create new list and add elments using for loop and insert function
my_new_reverse_list = []
for i in range(5):
    my_new_reverse_list.insert(0,i+1)
print(my_new_reverse_list)


# sum up all the elements in the list
total = 0
for i in my_list:
    total += i
print("Sum of all elements in my_list : ",total)


# reverse the given list from right to left
length = len(my_list)
print("Original list : ",my_list)
for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]
print("Reverse list : ",my_list)
