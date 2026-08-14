'''class Countdown:
    def __init__(self,start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        else:
            self.current -= 1
            return self.current

for i in Countdown (6):
    print(i)'''

class MyRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __iter__(self):
        return self

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start -1

for i in MyRange(1, 8):
    print(i)