#Gets the User's name
name = input("Enter name :")
print(name)

#Enters Users Favorite Number
number = input("Enter Favorite Number :")
print (number)

number = int(number)

prime = "prime"
for i in range(2,(number//2)+1): #super inefficent
    if number % i == 0: 
        prime = "not prime"
        break 
print("Your favorite number is " + prime)
