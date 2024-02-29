data=(23, 67, 78, 100, 200, 300)
print(data[0], data[-1])

# first, sec, third, fourth = data # unpacking
first, *other, last=data
print(first, other, last)

d1={'a':12, 'c':67, 'f':78}

for k,v in d1.items():
    print(k, v)

def mysum(*arguments):
    total=0
    for e in arguments:
        total += e
    return total

print(mysum(56,78,89,12,20))

print(mysum(*data))

