"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

Max = '0'


def ispandigital(number):
    if '0' in number:
        return False
    if len(number) == 9:
        number = set(number)
        return len(number) == 9
    else:
        return False


def main():
    global Max
    for ite in range(2, 10):
        num = 1
        while True:
            # print(num)
            Gened = ''.join([str(s * num) for s in range(1, ite + 1)])
            if len(Gened) > 9:
                break
            elif len(Gened) < 9:
                num += 1
                continue
            else:
                if ispandigital(Gened):
                    Max = max(Gened, Max)
            num += 1
    print(Max)


main()
