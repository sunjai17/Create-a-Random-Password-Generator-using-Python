# Strong Password Generator Only by entering the size of password

import string
import random

#store all the characters in the list
s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)


#Ask users about the Number of characters 
user_input=input("How many Characters do you want in your Password?")


#check the input is the number ?
#check wheather is it greater than 8

while(True):
    try:
        character_number = int(user_input)

        if character_number < 8:
            print("Your number should be atleast 8")

            user_input = input("Please Enter your number again!:")

        else:
            break

    except:
        print("Please enter the numbers only")
        user_input = input("How many characters do you want in your password?")


# shuffle all te list 
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

#calculate 30% and 20% of the no:of charcater 
part1 = round(character_number * (30/100))
part2 = round(character_number * (20/100))

# generation of the password (60% letters and 40% digits & punctuations)
result = []


for x in range(part1):
 
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2):
 
    result.append(s3[x])
    result.append(s4[x])
 
 
# shuffle result
random.shuffle(result)
 
 
# join result
password = "".join(result)
print("Strong Password: ", password)