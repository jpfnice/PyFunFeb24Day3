
with open("data.txt") as afile:
    while True:
        text=afile.read(5)
        if text == "":
            break
        print(text)
    
