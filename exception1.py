
data=[2,3,4,6,10]


ix=input("Please enter an int in the range [0,4]: ")

try:
    ix=int(ix)
    print(f"At position {ix} is the element {data[ix]}")
    print("End of try block")
except:
    print("There is a problem")
    
print("The end")