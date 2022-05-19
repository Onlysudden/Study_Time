class Counter:
    def __init__(self, value=0):
        self.value = value

    def inc(self, delta=1):
        self.value += delta
        if self.value >= 0:
            pass
        else:
            self.value = 0
        return Counter(self.value)

    def dec(self, delta=1):
        self.value -= delta
        if self.value >= 0:
            pass
        else:
            self.value = 0
        return Counter(self.value)


c = Counter()
print(c.inc().inc(5).dec(2).value)

d = Counter().inc(100)
print(d.dec().value)

forty_two = Counter(42)
print(forty_two.value)
