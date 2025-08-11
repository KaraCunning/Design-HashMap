class MyHashMap:

    def __init__(self):
        self.items = []


    def put(self, key: int, value: int) -> None:
        for i, (k,v) in enumerate(self.items):
            if k == key:
                self.items[i] = (key, value)
                return
        
        self.items.append((key,value))
        

    def get(self, key: int) -> int:
        for k, v in self.items:
            if k == key:
                return v
        return -1


    def remove(self, key: int) -> None:
        for i, (k,v) in enumerate(self.items):
            if k == key:
                del self.items[i]
                return
       


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)