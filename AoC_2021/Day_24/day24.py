from itertools import product

steps = [7, 8, 2, 11, None, 12, 14, None, 15, None, None, None, None, None]
required = [None, None, None, None, 3, None, None, 16, None, 8, 12, 7, 6, 11]

inputdata = product(range(9, 0, -1), repeat=7)


def works(digits):
    z = 0
    res = [0] * 14

    digits_idx = 0

    for i in range(14):
        inc, mod_req = steps[i], required[i]

        if inc == None:
            res[i] = ((z % 26) - mod_req)
            z //= 26
            if not (1 <= res[i] <= 9):
                return False

        else:
            z *= 26
            z += digits[digits_idx] + inc
            res[i] = digits[digits_idx]
            digits_idx += 1

    return res


for digits in inputdata:
    res = works(digits)
    if res:
        print("".join([str(i) for i in res]))
        break