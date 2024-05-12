import random
import string
length=int(input("Enter password length:"))
print('''choose character set for password from these:
1. digits
2. letters
3. special characters
4. exit''')
characterList=" "
while(True):
    choice=int(input("pick a number"))
    if(choice==1):
        characterList+=string.ascii_letters
    elif(choice==2):
        characterList+=string.digits
    elif(choice==3):
        characterList+=string.punctuation
    elif(choice==4):
        break
    else:
        print("please pick a valid option!")
password=[]
for i in range(length):
    randomchar=random.choice(characterList)
    password.append(randomchar)
print("the random password is"+"".join(password))

