numbers = [10, 20, 30]

iterator = iter(numbers)


numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))



class Count:

    def __init__(self, max_value):
        self.current = 1
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):

        if self.current <= self.max_value:
            value = self.current
            self.current += 1
            return value

        raise StopIteration


counter = Count(5)

for number in counter:
    print(number)