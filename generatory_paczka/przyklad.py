data = list(range(100_000_000))  #100 mln elementów w RAM
total = 0
for x in data:
    if x % 2 == 0:
        total += x
print(total)

class BigRangeIterator:
    def __init__(self, max_val):
        self.current = 0
        self.max_val = max_val

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max_val:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


data = BigRangeIterator(100_000_000)  # żadnej listy, nie zużywa RAM
total = 0
for x in data:
    if x % 2 == 0:
        total += x
print(total)


