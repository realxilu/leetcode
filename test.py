def myAtoi(s):
    digits = list(s.strip())

    if len(digits) == 0:
        return 0

    sign = -1 if digits[0] == '-' else 1

    if digits[0] in ('-', '+'):
        del digits[0]

    ret, i = 0, 0
    while i < len(digits) and digits[i].isdigit():
        ret = ret * 10 + int(digits[i])
        i += 1

    return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))

myAtoi('2.31')
