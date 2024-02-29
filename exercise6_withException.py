"""
    Define a function isPrime which purpose is to determine if
    the number it receives as argument is a prime number or not.
    
    Step1:
        test the argument received to ensure it is an int > 1
    Step2:
        with the help of a loop try to divide the argument received 
        (lets call it "number") by 2,3,4,5, up to number-1
        For instance, if number is 17 you can test: 2,3,4,5,...,15,16
        Ex: if number % 2 == 0 then 2 is a divisor of number
        As soon as you find a divisor of "number" you can return False
    Step3:
        At the end of the loop, you will have tested all possible
        divisor of number, you can return True: "number" is a 
        prime number
"""

def isPrime(number):
    if isinstance(number, int):        
        if number > 1:
            divisor=2
            while divisor < number:
                if number % divisor == 0:
                    return False
                divisor = divisor + 1
            return True
        else:
            return False
    else:
        ex=ValueError(f"{number} is not an int")
        raise ex
    
        
        # or
        # raise ValueError(f"{number} is not an int")
        
        #return False    # In this case a better option is to raise
                        # an exception (this will be covered later)
   

tests=["abc",-1,2,4,5,6,7,11,3.4, 26,27,1233]

for e in tests:
    try:
        if isPrime(e):
            print(e, "is a prime number")
        else: 
            print(e,"is NOT a prime number")
    except:
        print(f"Problem with the value {e}")
