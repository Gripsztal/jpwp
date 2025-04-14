import itertools

#wyrażenie generatorowe dla licbz parzystych
even_numbers = (x for x in itertools.count(0) if x % 2 == 0)

#islice przycina generator do pierwszych 10 elementów
limited_evens = itertools.islice(even_numbers, 10)

for num in limited_evens:
    print(num)
