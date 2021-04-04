formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter))
print(formatter.format(
    "humpty dumpty sat on a wall",
    " and they had a great fall",
))
