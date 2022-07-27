""" Remove duplicate elements from a given list
	Create a empty new_list and append the elements not repeated in original list """

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
new_list = []

for number in my_list:  
	if number not in new_list:  
		new_list.append(number)  
my_list = new_list[:]  
print("The list with unique elements only:")
print(my_list)
