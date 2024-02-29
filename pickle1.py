import pickle
d1={
        10:["raphael", "gabriel", "thomas"], 
        11:["julia", "yann"],
        13:["roman", "mohamed"]
}

with open("mydict.pick", "wb") as afile:
    pickle.dump(d1, afile)
    
    