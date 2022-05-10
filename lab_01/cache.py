
msg = 'Hello'
print(msg)

class LRUCache:

    def __init__(self, capacity: int=3) -> None:
        self.num = 0
        self.capacity = capacity
        self.elements = {}
        self.list = {}
        print('Cache capacity setted as: '+ str(self.capacity))
    
    def get(self, key:str) -> str:
        if key not in self.elements:
            return 'not found'
        return self.elements[key]

    def set(self, key: str, value: str) -> None:
        if len(self.elements) >= self.capacity:
            oldestValue = min(self.list, key=self.list.get)
            print('Oldest value to remove is ' + oldestValue)
            del(self.elements[oldestValue])
            del(self.list[key])

        self.elements[key] = value 
        self.list[key] = self.num
        self.num = self.num + 1
            

    def rem(self, key: str) -> None:
        if key not in self.elements:
            print('There is no such key')
            return
        del(self.elements[key])
        del(self.list[key])


