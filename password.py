import string
import random


s1 = list(string.ascii_lowercase) #30%
s2 = list(string.ascii_uppercase) #20%
s3 = list(string.digits) #20
s4 = list(string.punctuation)#20


while True:
    try:
        characters_number = int(characters_number)
        if characters_number < 8 :
            print("you need at least 8 characters")
            characters_number = input("please enter the number again : ")
        else:
            break
    except:
        print("please enter numbers only")
        characters_number = input("how many characters for the password : ")
        
        
random.shuffle(s1)    
random.shuffle(s2)    
random.shuffle(s3)    
random.shuffle(s4)    
             
part1 = round(characters_number * (30/100))             
part2 = round(characters_number * (20/100))

password =[]

for i in range(part1):
    password.append(s1[i])            
    password.append(s2[i])
    
                
for i in range(part2):
    password.append(s3[i])            
    password.append(s4[i]) 
    
password = "".join(password[0:])

print(password)             