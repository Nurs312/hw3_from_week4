def moove(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


x = [1, 2, 3, 4]
print(x)
moove(x, 2)
print(x)

