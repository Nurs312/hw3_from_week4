def min_absent_pos(lst):
    maximum = max(lst)
    if maximum > 0:
        for i in range(maximum + 1):
            if i not in lst and i > 0:
                print(i)
            elif i in lst and i > 0:
                absent = maximum + 1
                return absent
    elif maximum == 0 or maximum < 0:
        return 1


x = [-1, -2, 0]
print(min_absent_pos(x))
