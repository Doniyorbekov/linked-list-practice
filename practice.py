numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def three_num(numbers, target):

    for x1 in numbers:
        seen = set()

        for x2 in numbers:
            x3 = target - x1 -x2

            if x3 in seen:
                return True
            seen.add(x2)
    return False
print(three_num(numbers, 15))