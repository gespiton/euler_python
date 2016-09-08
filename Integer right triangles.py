"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
 For which value of p ≤ 1000, is the number of solutions maximised? """
# help(list)
import math
# help(set)


def jud(list_triangle):
    return list_triangle[0]**2 + list_triangle[1]**2 == list_triangle[2]**2


def solver(peri):
    set_of_set = set()
    set_of_result = set()
    for one in range(1, peri):
        for two in range(1, peri):
            three = peri - one - two
            if three <= 0:
                continue
            #print(one, two, three)
            buf = [one, two, three]
            buf.sort()
            buf = tuple(buf)
            if buf in set_of_set:
                continue
            set_of_set.add(buf)
            if jud(buf):
                set_of_result.add(buf)
    return len(set_of_result)


def main():
    Max = 0
    current = 0
    for i in range(3, 1001):
        num = solver(i)
        if num > Max:
            Max = num
            current = i

    print(current, Max)
main()
