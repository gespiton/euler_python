"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math

# help(list.copy)
file = open('text', 'wt')


def isprime(n):
    M = math.floor(math.sqrt(n)) + 1
    for i in range(2, M):
        if n % i == 0:
            return False
    return True


# def generator(num_new, num_list):
#     if len(num_list) == 0:
#         print(''.join(num_new))
#         if isprime(int(''.join(num_new))):
#             return False
#         else:
#             return True
#     for i in range(0, len(num_list)):
#         num_list_buf = num_list.copy()
#         num_new_buf = num_new.copy()
#         num_new_buf.append(num_list_buf.pop(i))
#         # print(type(num_new_buf))
#         if generator(num_new_buf, num_list_buf):
#             return True
#         else:
#             return False
#
#
# def judge(num):
#     num_len = len(str(num))
#     for i in range(0, num_len):
#         num_new = list()
#         num_list = list(str(num))
#         num_new.append(num_list.pop(i))
#         if generator(num_new, num_list):
#             return False
#     return True
#
# print(isprime(917))
# print(judge(197))
# fucking stupid, I misunderstand the question
al_sum = 0
for i in range(1, 1000000):
    num_len = len(str(i))
    current = i
    # print(current, file=file)
    for ite_count in range(num_len):
        if not isprime(current):
            break
        num_list = list(str(current))
        num_list.append(num_list.pop(0))
        if num_list[0] == '0':
            break
        current = int(''.join(num_list))
        # print(current, file=file)
        if ite_count == num_len - 1:
            ite_count += 1
    if ite_count == num_len:
        al_sum += 1
        print(i, file=file)
print(al_sum - 1)
