'''
num = 36
my_list = [1, 2, 3, 4, 5, 6, 7] 
new_list = []

for index, number in enumerate(my_list): 
    my_list[index] = number * num 

print(my_list) 
''' 
num = 36
my_list = [1, 2, 3, 4, 5, 6, 7] 

for index in range(len(my_list)): 
    my_list[index] = my_list[index] * num 
    
print(my_list)
