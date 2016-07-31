from fractions import Fraction


# help(fractions)
# print(fractions.Fraction(3, 6))


def judge(num, denom):
    a_set = {int(num / 10), num % 10, int(denom / 10), denom % 10}
    if len(a_set) != 3 or 0 in a_set:
        return

    num_list = [int(num / 10), num % 10]
    denom_list = [int(denom / 10), denom % 10]
    for i in set(str(num)) & set(str(denom)):
        num_list.remove(int(i))
        denom_list.remove(int(i))
    if len(num_list) != 1:
        return

    if Fraction(num, denom) == Fraction(num_list[0], denom_list[0]):
        print('{}/{}'.format(num, denom))
        return True


f = Fraction(1, 1)
for denominator in range(10, 100):
    for numerator in range(10, denominator):
        if judge(numerator, denominator):
            f *= Fraction(numerator,denominator)
print(f)
