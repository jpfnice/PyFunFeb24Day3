
class listPlus(list): # listPlus inherit from list

    def removeAll(self, element):
        while element in self:
            self.remove(element)
            
    def __add__(list1, list2):
        newList=[]
        if len(list1) > len(list2):
            for index in range(len(list2)): 
                newList.append(list1[index]+list2[index])
            for index in range(len(list2), len(list1)): 
                newList.append(list1[index])
        else:
            for index in range(len(list1)):
                newList.append(list1[index]+list2[index])
            for index in range(len(list1), len(list2)):
                newList.append(list2[index])
        return newList        

l1=listPlus()
l1.append(34)
l1.insert(0,100)
l1.append(34)
l1.insert(0,10)
l1.insert(0,300)
l1.insert(0,100)
print(l1)
l1.removeAll(100)
print(l1)

l2=listPlus([300, 10, 3, 4, 34, 5])
print(l2)

l3=l1+l2 # l3=l1.__add__(l2)
print(l3)

