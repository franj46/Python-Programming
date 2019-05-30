'''
This is practice for While loops 

ask user to guess your secret number 

loop as long as users input is not equal to secret number 

Print a message if it is equal, then end loop 

while loops need an exit condition 

Do these mods at home: If guess is 2 less or greater, print 'almost there!'. If guess is greater or less than secret by 2, print 'too far!'


'''

secret = 7 
guess = int(input('Guess my secret number boi '))
while guess != secret: 
    print('Not correct') 
    guess = int(input('Guess my secret number: '))
    print('Nice work!')
