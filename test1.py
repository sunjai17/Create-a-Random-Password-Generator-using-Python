import string
import random

#Getting the Password length
length=int(input("Enter The Password Length:"))

print('''choose charater set for password from these
      1.Digits
      2.Letters
      3.Special characters
      4.Exit''')

characterList=""

#Getting character set for password
while(True):

    choice=int(input("Pick The Number:"))
    if (choice == 1):

        #Adding letters to possible characters 
        characterList += string.ascii_letters

    elif (choice == 2):

        #Adding digits to possible characters
        characterList += string.digits

    elif (choice == 3):

        #Adding special characters to the opossible characters 
        characterList += string.punctuation
    
    elif (choice == 4):
        break

    else:
        print("Please pick a valid Option!")

Password = []

for i in range(length):
    
    #Picking a random character from our character list
    randomchar = random.choice(characterList)

    # appending a random character to the password
    Password.append(randomchar)

 #printing Password as a string
print("The random Password is " + "".join(Password))
    



        





