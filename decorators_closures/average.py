def make_averager():
    """
    average of clousure
    :return:
    """
    series = []

    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)

    return averager

def make_averager():
    """
    non local version of average
    :return:
    """
    total = 0
    count = 0

    def averager(new_value):
        nonlocal count, total # comment it would be buggy!
        count += 1
        total += new_value
        return total / count

    return averager


avg =  make_averager()
print(avg(10))
print(avg(11))
print(avg(12))