def isPan(s):
    return s == s[::-1]


sum = 0
for i in range(1, 1000001):
    if isPan(str(i)) and isPan(str(bin(i))[2:]):
        sum += i
print(sum())
