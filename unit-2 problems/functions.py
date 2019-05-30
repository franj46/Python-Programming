'''
intro = input('What operation would you like to do? add, sub, mult or div?')

if intro = 'add': 
    addprompt = int(input('What is number 1?'))
    addprompt2 = int(input('What is number 2?')) 

    sum = addprompt + addprompt2 
'''

#defining a function 
def add(a, b): 
    return a + b 

def subtract(a, b): 
    return a - b 

def multiply(a, b): 
    return a * b 

def divide(a, b): 
    return a / b 

#function with single argument 
def print_msg(message): 
    print(message)

#print_msg('Python rocks!') 

#functions that return a result 
def square(value): 
    result = value * value 
    return result 

answer = square(10) 
#print(answer) 

#print(square(square(3)))

#function with multiple arguments 
'''
def greetings(name, job, hobby): 
    print(f'Hello {name} your job is {job} and you like {hobby}') 

greetings('Jeremy', 'student', 'music') 
'''
'''
#iterate over a list in reverse order using a function
def reverse_list(my_list): 
    new_list = []
    #the for loop iterates over the list 
    for i in range(len(my_list) - 1, - 1, - 1): 
        #add each element to a new list 
        new_list.append(my_list[i])
    return new_list

fruits = ['apple', 'kiwi', 'banana', 'mango'] 

result = reverse_list(fruits)
print(result)
'''

#check if word is palindrome 
#return True if it is, and False if otherwise 

def reverse_word(my_word): 
    reverse_word = ''
    for i in range(len(my_word) - 1, - 1, - 1): 
        reversed_word += my_word[i] 
    return reverse_word

def is_palindrome(word): 
    new_word = reverse_word(word) 
    if reverse_word == word: 
        return True 
    return False



    






