class Countdown:
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
    print(i)