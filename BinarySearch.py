
# Mapping of the alphabet
d = {chr(i+96):i for i in range(1,27)}


list = ["ab", "aa", "ad", "ac", "ba", "bb", "bd", "bc", "ca", "cb", "cd", "cc", "da", "db", "dc", "dd"]


l = []

#Convert the string to hexadecimal for value of a string
for i in list:
    l.append(int(i, 16))

#sorting the list in numerical ascending order
l.sort()


value = int(str(input("What are you looking for? ")), 16)

class BinarySearch():
    def __init__(self, value, list, src_list):
        self.value = value
        self.list = list
        self.list1 = src_list
        
    def middle(self):
        """Finding the middle of the list"""
        middle = float(len(self.list))/2
        if middle % 2 != 0:
            return self.list[int(middle - 0.5)]
        else:
            return (self.list[int(middle-1)])

    def search(self):
        """Halfing the list until we find the designated value"""
        if self.value == self.middle():
            return self.middle()
        elif self.value > self.middle():
            self.list = self.list[int(len(self.list)/2):]
            return self.search()
        elif self.value < self.middle():
            self.list = self.list[:int(len(self.list)/2)]
            return self.search()
        
    def result(self):
        """Return the result"""
        counter = 0
        for i in self.list1:
            if self.search() == int(i, 16):
                return "Item found at index - " + str(counter-1)
            else:
                counter +=1
        
    

print(BinarySearch(value, l, list).result())