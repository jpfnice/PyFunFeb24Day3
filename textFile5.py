# mode: r, w, a, r+, w+, a+, rb, wb, ab
with open("newfile.txt", "a") as afile:
    print("First line", file=afile, end=",")
    print("Second line", file=afile)
    print("Third line", file=afile)

    
    
    
