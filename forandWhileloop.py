#Creating a list
random_stuff=['toilet','coronavirus','one',1]

#Creating a for loop for each element of the list
for i in range (len(random_stuff)):
    print (i,random_stuff[i])


#Printing elements of a list not using index or step or counter
for itemname in random_stuff:
     print (itemname)


print ("Printing while loop")
#Printng itens using while loop
i=0
while (True):
    if (i==4):
        break
    print (random_stuff[i])
    i=i+1



#Printing contents of tuple contents
print ("Printing Tuples using for")
food_tuple=('pasta','ravioli','pizza')


for food in food_tuple:
    print (food)


print ("Printing Tuples while loop")

i=0
while(True):
    if(i==len (food_tuple)):
        break
    print (food_tuple[i])
    i=i+1
