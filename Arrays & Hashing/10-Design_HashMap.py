 class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        for array in self.hashMap:
            if array[0] == key:
                array[1] = value        
                return
        self.hashMap.append([key, value])
        
    def get(self, key: int) -> int:
        if not self.hashMap:
            return -1
        for array in self.hashMap:
            if array[0] == key:
                return array[1]
        return -1

    def remove(self, key: int) -> None:
        if not self.hashMap:
            return
        for array in self.hashMap:
            if array[0] == key:
                self.hashMap.remove(array)
                return

