import itertools

class ChainIterator:
    def __init__(self, *collections):
        #łączenie wszystkich list w jeden iterator
        self.chain_iter = itertools.chain(*collections)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.chain_iter)


list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

for item in ChainIterator(list1, list2, list3):
    print(item)
