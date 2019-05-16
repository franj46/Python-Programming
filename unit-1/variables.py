#def "Function Name" is syntax for defining function
def main():
    first_name = 'Jeremy'
    last_name = 'Francis'

    full_name = first_name + ' ' + last_name 

    print(full_name) 

    #boolean value
    has_child = True

    #null/none variable - Has no value, unlike 0 or an empty string, which are both values
    cars = None


def conditionals(): 
    #given a range of grades 0-100
    #if grade is between 80 and 100 - print 'A'
    #if grade is between 60 and 79 - print 'B' 
    #if grade is between 50 and 59 - print 'C'
    #0-49 - print 'F' 

    val = 4
    if val > 35: 
        print('High')
    elif val > 15:     #If 2 or more conditionals, need to use elif
        print('Medium') 
    else: 
        print('Low') 

def grade(): 
    mark  = 79 

    if mark >= 80 and mark <=100: 
        print('A') 
    elif mark >=60 and mark <= 79: 
        print('B') 
    elif mark >= 50 and mark <= 59: 
        print('C')
    else: 
        print('F') 
    
if __name__ == '__main__': 
    grade() 

#Exercise used in coding interviews
def fizzbuzz(): 
    '''
    for the numbers 1 to 50 
    print 'fizz' if the number is a multiple of 3 
    print 'buzz' if the number is a multiple of 5 
    print 'fizzbuzz' if the number is a multiple of 15 
    ''' 
    for num in range (1, 51): 
        if num % 15 == 0: 
            print('Fizzbuzz')
        elif num % 5 == 0: 
            print('buzz')
        elif num % 3 == 0: 
            print('fizz')
        else: 
            print(num)


if __name__ == '__main__': 
    fizzbuzz()  
