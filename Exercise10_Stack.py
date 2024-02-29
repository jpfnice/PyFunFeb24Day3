
class Stack:
    pass

"""
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

