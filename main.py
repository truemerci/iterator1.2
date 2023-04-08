class FibonacciIterator:
    def __init__(self, value):
        self.value = value
        self.i = 1
        self.f = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i > self.value:
            raise StopIteration
        result = self.i
        self.i, self.f = self.i + self.f, self.i
        return result


fibonacci = FibonacciIterator(21)

for number in fibonacci:
    print(number)
