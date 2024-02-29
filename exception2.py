
data=[2,3,4,6,10]


while True:
    ix=input("Please enter an int in the range [0,4]: ")
    try:
        ix=int(ix)
        print(f"At position {ix} is the element {data[ix]}")
        print("End of try block")
        break
    except ValueError as ex:
        print("A ValueError is raised")
        print(ex)
    except IndexError as ex:
        print("An IndexError is raised")
        print(ex)
    
print("The end")