class RandomizedSet:

    def __init__(self):
        self.internal_dict = dict()
        self.counter = 0
        

    def insert(self, val: int) -> bool:
        if val in self.internal_dict:
            return False
        else:
            self.internal_dict[val] = self.counter + 1
            self.counter += 1
            return True
        

    def remove(self, val: int) -> bool:
        temp = self.internal_dict.pop(val, -1)
        if temp == -1:
            return False
        return True
        

    def getRandom(self) -> int:
        dict_list = list(self.internal_dict.values())
        while True:
            try:
                random_int = random.randint(0, self.counter)
                key = list(self.internal_dict.keys())[dict_list.index(random_int)]
                return key
            except ValueError:
                continue
            
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
