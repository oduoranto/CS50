  
print("list :  sequence of mutable(can be changed) values")

#Define a list of months
months = ['jan', 'Feb','Mar', 'April', ' May', 'June', 
          'July','Aug', 'Sept', 'Oct', 'Nov', 'Dec']

number = int(input("Number(0-11) : "))

print(f"{months[number]} is your birth month")

months.append('Anto')
print(months)