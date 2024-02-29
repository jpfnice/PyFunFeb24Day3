import pickle

with open("mydict.pick", "rb") as afile:
    d1=pickle.load(afile)
    
print(d1, len(d1), type(d1))