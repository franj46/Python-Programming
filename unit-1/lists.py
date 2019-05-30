'''
#declaring an empty list 
classmates = [] 

#add items to list. Lists have indexes, and they start at 0. List indexes indicate the location of an item in a list 

'classmates[0] = 'Sue'
classmates[1] = 'Shad'

#Here's another way of adding to a list 
classmates.append('Sue')
classmates.append('Shad') 
classmates.append('Mayank')
classmates.append('Gus')
classmates.append('Chin')
classmates.append('Eva')
classmates.append('Jeremy')
classmates.append('Dan')
classmates.append('Aaron')
classmates.append('Julian') 


#Access an item at a specific position 
#print(classmates[0]) #1st element in list 

#print(classmates[4]) #4th element in list  

# get size of the list 
#print(len(classmates)) 
print(classmates)

#remove an item from the end of the list 
classmates.pop() #removes last element in list 

print(classmates) 

#insert at specific position 
classmates.insert(0, 'Julian')

print(classmates) 

#Remove item from a list 
classmates.remove('Gus') 
print(classmates)

#edit an item in a list 
classmates[1] = 'Sue Work' #access an item in a list with listName[index] 

#print(classmates) 


#iterate over a list (for loops) 
for classmate in classmates: 
    if(classmate == 'Gus'):
        print('Great, Gus is in the class!') 


#edit elements while iterating 
for index, classmate in enumerate(classmates): 
    classmates[index] = classmate.upper()

print(classmates)

''' 

#create a of list all the marvel movies from Iron Man to Endgame 
#go through the list and create a second list with all the titles that have "The"
'''
marvelMovies = ['Iron Man', 'Iron Man 2', 'The Incredible Hulk', 'Thor', 'Captain America: The First Avenger', 'The Avengers', 'Iron Man 3', 'Thor: Dark World', 'Cap America: The Winter Soldier', 'Guardians of the Galaxy', 'Avengers: Age of Ultron', 'Ant Man', 'Captain America: Civil War', 'Dr. Strange', 'Guardians of the Galaxy II', 'Spider Man: Homecoming', 'Thor Ragnarok', 'Black Panther', 'Avengers: Infinity War', 'Ant Man and The Wasp', 'Captain Marvel', 'Avengers Endgame'] 

theMovie = []

for index, movie in enumerate(marvelMovies): 
    if 'the ' in movie.lower(): 
        theMovie.append(movie)

print(theMovie)

#get index of a list 

for index in range(len(marvelMovies)): 
        print(index)
''' 
#reverse string example
#strings are immutable
my_string = 'This is a sentence'
reversed_string = '' 
for i in range(len(my_string) - 1, - 1, - 1): 
        reversed_string += my_string[i] 

print(reversed_string)




    



