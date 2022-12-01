# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4,
# but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during
# the twentieth century (1 Jan 1901 to 31 Dec 2000)?

class Day:
    def __init__(self, year: int, month: int, day: int, day_type: int):
        self.day_types = ["Monday", "Tuesday", "Wednesday", "Thursday",
                          "Friday", " Saturday", "Sunday"]
        self.year = year
        self.month = month
        self.day = day
        self.day_type = day_type
        self.date = f"{self.year}-{self.month}-{self.day}"
        if self.year % 4 == 0:
            if self.year % 100:
                if self.year % 400:
                    self.leap = True
                else:
                    self.leap = False
            else:
                self.leap = True
        else:
            self.leap = False

    def check_leap(self):
        if self.year % 4 == 0:
            if self.year % 100:
                if self.year % 400:
                    self.leap = True
                else:
                    self.leap = False
            else:
                self.leap = True
        else:
            self.leap = False

    def print_date(self):
        print(self.day_types[self.day_type-1], self.day, self.month, self.year)

    def next_day(self):
        self.day_type += 1
        if self.day_type > 7:
            self.day_type = 1

        self.day += 1
        if self.month in [1, 3, 5, 7, 8, 10, 12]:
            if self.day > 31:
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.month = 1
                    self.year += 1
                    self.check_leap()
        elif self.month in [4, 6, 9, 11]:
            if self.day > 30:
                self.day = 1
                self.month += 1
                if self.month > 12:
                    self.month = 1
                    self.year += 1
                    self.check_leap()
        else:
            if not self.leap:
                if self.day > 28:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
                        self.check_leap()
            else:
                if self.day > 29:
                    self.day = 1
                    self.month += 1
                    if self.month > 12:
                        self.month = 1
                        self.year += 1
                        self.check_leap()
        self.date = f"{self.year}-{self.month}-{self.day}"


current_date = Day(1900, 1, 1, 7)
counter = 0
while current_date.date != "2000-12-31":
    current_date.next_day()
    if current_date.day_type == 7 \
            and current_date.year != 1900 \
            and current_date.day == 1:
        counter += 1
print(counter)
