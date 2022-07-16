def count(numbs):
    count=0

    for numb in numbs:
        if numb == 4:
            count = count+1
    return count
print(count([1, 4, 6, 7, 4]))
print(count([1, 4, 6, 4, 7, 4]))



