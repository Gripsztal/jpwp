class CombinedIterator:
    def __init__(self, *collections):
        self.collections = collections
        self.current_collection = 0
        self.iterator = iter(self.collections[self.current_collection])

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                current_value = next(self.iterator)
                if current_value % 2 == 0:
                    return current_value
            except StopIteration:
                self.current_collection += 1
                if self.current_collection < len(self.collections):
                    self.iterator = iter(self.collections[self.current_collection])
                else:
                    raise StopIteration


collection1 = [1, 2, 3, 4, 5]
collection2 = [3, 4, 5, 6, 7]
collection3 = [8, 9, 10]

combined_iterator = CombinedIterator(collection1, collection2, collection3)

for number in combined_iterator:
    print(number)
    
    
    
    
