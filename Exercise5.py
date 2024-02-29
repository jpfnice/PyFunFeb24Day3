"""
Exercise 5:
    
Given a list like this one:
    
words=["He", "does", "confess", "he", "feels", 
       "himself","distracted", "but", 
       "from", "what", "cause", "he", "will", 
       "by","no", "means", "speak"]

Create a dict like the following:
  {
  2 :['He', 'he', 'he', 'by', 'no'],
  3 :['but'],
  4 :['does', 'from', 'what', 'will'],
  5 :['feels', 'cause', 'means', 'speak'],
  7 :['confess', 'himself'],
 10 :['distracted']
  }

"""

words=["He", "does", "confess", "he", "feels", 
       "himself","distracted", "but", 
       "from", "what", "cause", "he", "will", 
       "by","no", "means", "speak"]

sizeDict=dict()

for word in words:
    wordSize=len(word)
    # Is the wordSize (2,3,4, ...) already present in the dict sizeDict or is
    # it the first time this size is encountered ?
    if wordSize in sizeDict: 
        sizeDict[wordSize].append(word) # Append a new word to the existing list 
        # of words with this size
    else:
        sizeDict[wordSize]=[word] # Create a new pair -> size:[word]
        
print("First option: keys are not sorted:\n")  
      
for sz,wds in sizeDict.items():
    print(f"{sz} --> {wds}")
    
print("\nSecond option: keys are sorted:\n")
for sz in sorted(sizeDict.keys()):
    print(f"{sz} --> {sorted(sizeDict[sz])}")
    
print("\nThird option: keys are sorted and formatted:\n")
for sz in sorted(sizeDict.keys()):
    print(f"{sz:3d} --> {sizeDict[sz]}")