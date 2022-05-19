class HourClock:
    def __init__(self):
        self.position = 0

    @property
    def hours(self):
        return self.position

    @hours.setter
    def hours(self, new_pos):
        self.position = new_pos % 12


clock = HourClock()
print(clock.hours)

clock.hours += 5
clock.hours += 5
print(clock.hours)

clock.hours += 5
print(clock.hours)

clock.hours -= 4
print(clock.hours)

clock.hours = 123
print(clock.hours)
