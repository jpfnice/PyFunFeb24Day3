"""
Note: this text is a docstring which purpose could be to describe this
module

Exercise 10:
    
Definition of a new kind of collection: a Stack

Attributes:
    maxSize: an int, the maximum size of the stack
    content: a list to hold the elements
    
Methods:
    __init__(self, size)
    push(self, element)
    __repr__(self)
    pop(self)
    peek(self)
    
    __len__(self) -> used by the function len()
    __eq__(self, other) -> used by ==
"""

class Stack:
    """ A docstring to describre the class itself """
    def __init__(self, size): # The "constructor"
        """ A docstring to describe the class constructor """
        if isinstance(size, int) and size > 0:
            self.maxSize=size
            self.content=[]
        else:
            #print("Wrong size received")
            raise ValueError(f"Wrong Stack size used: {size}")
            
    def push(self, element):
        """
        The push method add a element at the end of the Stack is the Stack is
        not full
        
        Parameters
        ----------
        element : any type
            The element to be pushed in the Stack

        Raises
        ------
        Exception
            This exception will be raised if the Stack is full

        Returns
        -------
        None.

        """
        if len(self.content) < self.maxSize:
            self.content.append(element)
        else:
            #print(f"Stack Full: {element} cannot be pushed")
            raise Exception(f"Stack Full: {element} cannot be pushed")
            
    def __repr__(self): # -> used by str() to convert a Stack into a str
        """ A docstring to describe the __repr__ method """
        return f"({len(self.content)}/{self.maxSize}) {self.content}"
    
    def pop(self):
        """ A docstring to describe the pop method """
        if len(self.content) != 0:
            return self.content.pop()
        else:
            #print("Stack Empty: pop() cannot pop an element")
            raise Exception("Stack Empty: pop() cannot pop an element")
    def peek(self):
        """ A docstring to describe the peek method """
        if len(self.content) != 0:
            return self.content[-1]
        else:
            #print("Stack Empty: it cannot peek an element")
            raise Exception("Stack Empty: peek() cannot peek an element")
    def __len__(self): # -> used by the function len()
        """ A docstring to describe the __len__ method """
        return len(self.content)
    def __eq__(self, other): #-> used by ==
        """ A docstring to describe the __eq__ method """
        return self.maxSize == other.maxSize and self.content == other.content 
    def __contains__(self, element):
        return element in self.content
    
# To test the Stack class:

try:
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
except ValueError as e:
    print("Invalid Stack size")
    print(e)
except Exception as e:
    print("A problem is detected")
    print(e)