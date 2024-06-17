number = int(input("Number: "))

if number > 0 :
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is nagative")    
else:
    print(f"{number} is zero")   

#list :  sequence of mutable(can be changed) values
names = ['John', 'Sean', 'Emmaa','Anto' ]

print(names)

for items in names:
    print(items)

for n in range(len(names)):
    
    print(n)    

#Tuples : used if you have values that are not going to  change (sequence of immutable values)   

coordinate =(200,200)
print(coordinate)

#Sets; collection of unique values
#Dict : collection of key-value pairs