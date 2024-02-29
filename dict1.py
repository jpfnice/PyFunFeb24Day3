"""
dict: a collection

len(), for, in, not in, ...
"""

d1=dict()
#or
d1={}

print(d1, type(d1), len(d1))

d1={
    "maria":27845676, 
    "peter":27867899
}

print(d1, type(d1), len(d1))
print(d1["maria"])
print(d1.get("maria"))
d1["paul"]=27977666
d1["maria"]=27977665
print(d1["maria"])

print(d1, type(d1), len(d1))

d1={
        10:["raphael", "gabriel", "thomas"], 
        11:["julia", "yann"]
}

print(d1, type(d1), len(d1))

print(d1[10])
print(d1.get(0))
d1[9]=["mario"]
print(d1, type(d1), len(d1))
d1[9].append("julia")
print(d1, type(d1), len(d1))

