class Counter:
    def __init__(self, value=0):
        self.value = value

    def value(self):
        return self.value

    def inc(self, delta=1):
        self.value += delta

    def dec(self, delta=1):
        self.value -= delta


class LimitedCounter(Counter):
    def __init__(self, value=0, limit=0):
        self.value = value
        self.limit = limit

    def inc(self, delta=1):
        super().inc(delta)
        if self.value > self.limit:
            self.value = self.limit
        if self.value < 0:
            self.value = 0

    def dec(self, delta=1):
        super().dec(delta)
        if self.value > self.limit:
            self.value = self.limit
        if self.value < 0:
            self.value = 0


counter = LimitedCounter(limit=10)
counter.inc()
counter.inc(7)
print(counter.value)

counter.dec(10)
print(counter.value)

counter.inc(7)
counter.inc(7)
print(counter.value)
