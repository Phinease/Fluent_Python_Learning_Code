def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total/len(series)

    return averager


a = make_averager()
a(10)
a(11)
a(12)
print(a.__closure__)
print(a.__closure__[0].cell_contents)
print(a.__closure__[0].__doc__)
