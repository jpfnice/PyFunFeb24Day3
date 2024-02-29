
with open("data.txt") as afile:
    print(afile.tell())
    text=afile.readline()
    print(text)
    text=afile.readline()
    print(text)
    text=afile.readline(100)
    print(text)
    print(afile.tell())
    afile.seek(0)
    print(afile.tell())
    text=afile.readline()
    print(text)
    
