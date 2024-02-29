
def isPrime(number):
    """
    The purpose of the function isPrime is to determine if the number it receives as argument is a prime number or not.

    Parameters
    ----------
    number : int
        The number to be tested by isPrime

    Returns
    -------
    bool
        Returns True if number is a prime number

    """
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
        return False    # In this case a better option is to raise
                        # an exception (this will be covered later)
                        
class Stack:
    """ A docstring to describre the class itself """
    def __init__(self, size): # The "constructor"
        """ A docstring to describe the class constructor """
        if isinstance(size, int) and size > 0:
            self.maxSize=size
            self.content=[]
        else:
            print("Wrong size received")
            
    def push(self, element):
        """ A docstring to describe the push method """
        if len(self.content) < self.maxSize:
            self.content.append(element)
        else:
            print(f"Stack Full: {element} cannot be pushed")
            
    def __repr__(self): # -> used by str() to convert a Stack into a str
        """ A docstring to describe the __repr__ method """
        return f"({len(self.content)}/{self.maxSize}) {self.content}"
    
    def pop(self):
        """ A docstring to describe the pop method """
        if len(self.content) != 0:
            return self.content.pop()
        else:
            print("Stack Empty: it cannot pop an element")
    def peek(self):
        """ A docstring to describe the peek method """
        if len(self.content) != 0:
            return self.content[-1]
        else:
            print("Stack Empty: it cannot peek an element")
    def __len__(self): # -> used by the function len()
        """ A docstring to describe the __len__ method """
        return len(self.content)
    def __eq__(self, other): #-> used by ==
        """ A docstring to describe the __eq__ method """
        return self.maxSize == other.maxSize and self.content == other.content 
    def __contains__(self, element):
        return element in self.content

if __name__ == "__main__":
    # To test the Stack class:
    s1=Stack(10) # A stack with a maximum size of 10 created
    s1.push(20)
    s1.push(True)
    s1.push(4.5)
    print(s1) # (3/10) [20, True, 4.5]
    top=s1.pop()
    print(top) # 4.5
    print(s1) # (2/10) [20, True]
    top=s1.peek()
    print(top) # True
    print(s1) # (2/10) [20, True]
    
    s2=Stack(20)
    s2.push(20)
    s2.push(True)
    print(s1, len(s1))
    print(s2, len(s2))
    print(s1 == s2)
    
    len(s1) # s1.__len__() Stack -> LIFO Queue -> FIFO List -> no specific order
    
    s3=Stack(10)
    s3.push(20)
    s3.push(True)
    print(s1, len(s1))
    print(s3, len(s3))
    print(s1 == s3)
    
    if 20 in s1: # __contains__
        print(f"20 is in {s1}")
