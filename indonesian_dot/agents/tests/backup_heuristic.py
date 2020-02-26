"""lst = list(n)
length = n.length
count = 0
while 1 in lst:
    start = lst.index(1)
    sub_stack = [start]

    while sub_stack:
        start = sub_stack.pop()
        lst[start] = 0

        row, column = divmod(start, length)
        if row - 1 >= 0 and lst[start - length] != 0:
            sub_stack.append(row - 1)
        if row + 1 < length and lst[start + length] != 0:
            sub_stack.append(start + length)
        if column + 1 < length and lst[start + 1] != 0:
            sub_stack.append(start + 1)
        if column - 1 >= 0 and lst[start - 1] != 0:
            sub_stack.append(start - 1)

    count += 1

return count
"""
