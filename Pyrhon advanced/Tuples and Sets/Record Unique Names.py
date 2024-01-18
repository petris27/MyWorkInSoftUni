number_of_names = int(input()) # input the number of people
names = set() # set
for n in range(number_of_names): # loop of writting the names of all the given number of people
    names.add(input()) # giving the set values
for character in names: # for loop to output the given names once
    print(character) # printing