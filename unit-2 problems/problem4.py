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

'''

intro = input('What operation would you like to do? add, subtract, multiply or divide?')
a = int(input('What is the first number?')) 
b = int(input('What is the second number?'))

if intro == input('add'): 
  
    add(a, b)
    print(add) 

elif intro == input('subtract'): 
    a = int(input('What is the first number?')) 
    b = int(input('What is the second number?'))
    subtract(a, b) 
    print(subtract) 

elif intro == input('multiply'): 
    a = int(input('What is the first number?')) 
    b = int(input('What is the second number?'))
    multiply(a, b)
    print(multiply) 

elif intro == input('divide'):
    a = int(input('What is the first number?')) 
    b = int(input('What is the second number?'))
    divide(a, b)
    print(divide)  

''' 

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

print(square(square(3)))

#function with 




