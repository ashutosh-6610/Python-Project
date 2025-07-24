import random
import string
encript=string.punctuation+string.digits+string.ascii_letters+" "
encripts=list(encript)

key=encripts.copy()
random.shuffle(key)

strings=input("enter a string\n")
encripted=""
for i in strings:
    index=encript.find(i)
    encripted=encripted+key[index]
print(f"encripted version of the above string is {encripted}")

user_input=(input("press 1 if you want to see the actual string\n"))
try:
    input_=int(user_input)
    if input_==1:
        a=""
        for i in encripted:
            index=key.index(i)
            a=a+encript[index]
        print(f"The actual string you have entered is {a}")    
 
except ValueError:
        print("invalid choice\n")   


