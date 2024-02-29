import random

secret=random.randint(1,100)
 
# secret is the name of the variable
# that holds the number to guess

print(secret) # Just for testing purpose ...

"""

while bool expression:
    statement 1
    statement 2
    ...
else:
    statement 1
    statement 2
    
"""
currentNumberOfAttempts=0

while currentNumberOfAttempts < 6:

    while True:
        currentValue=input(f"Enter an int in the range [1,100]: ({currentNumberOfAttempts+1}/6) :")
        try:
            currentValue=int(currentValue)
            break
        except:
            print(f"Wrong value given: {currentValue}")
    
    if currentValue == secret:
        print ("Bingo ! You've found the secret number")
        break
    elif currentValue > secret:
        print("Too large !")
    elif currentValue < secret:
        print("Too small !") 
    currentNumberOfAttempts += 1 # -= *= /=
else:    
    print("The secret number was:", secret)
