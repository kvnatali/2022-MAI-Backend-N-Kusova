
msg = 'Hello'
print(msg)

class LRUCache:

    def __init__(self, capacity: int=3) -> None:
        self.capacity = capacity
        self.elements = {}
        print('Cache capacity setted as: '+ str(self.capacity))
    
    def get(self, key:str) -> str:
        if key not in self.elements:
            return 'not found'
        return self.elements[key]

    def set(self, key: str, value: str) -> None:
        if len(self.elements) >= self.capacity:
            oldestValue3 = next(iter(self.elements))
            print('Oldest value to remove is: ' + oldestValue3)
            del(self.elements[oldestValue3])

        self.elements[key] = value 
            

    def rem(self, key: str) -> None:
        if key not in self.elements:
            print('There is no such key')
            return
        del(self.elements[key])


