from math import gcd


# def gcm_calc(num, arr):
#
#     # a = 18
#     # b = 12
#
#     divisor = arr
#
#     while divisor > 0:
#         # if a % divisor == 0 and b % divisor == 0:
#         #     print('The GCD is', divisor)
#         #     break
#         for n in arr():
#             find_gcm()
#         divisor -= 1
#
#
# def find_gcd(x, y):
#     while (y):
#         x, y = y, x % y
#     print(x)
#     return x


# def gcd(a, b):
#     if b == 0:
#         return a
#     else:
#         # print(a % b)
#         return gcd(b, a % b)


def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a

    # if b == 0:
    #     return a
    #
    # else:
    #     return gcd(b, a % b)


if __name__ == '__main__':
    A = [2, 4, 6, 8, 10]
    # A = [12, 24, 27, 30, 36]

    divisor = A[0]
    numbers = A[1:]

    for n in numbers:
        divisor = gcd(divisor, n)

    print(divisor)

    # res = A[0]
    # print(A[1:])
    # for c in A[1::]:
    #     res = gcd(res, c)
    #     print(res)
    # print("final", res)
    # gcm_calc(5, [2, 4, 6, 8, 10])
    # print(gcd(18, 12))
    # # print(result)
    #
    # def find_gcd(x, y):
    #     while (y):
    #         x, y = y, x % y
    #
    #     return x

    # l = [20, 15, 26]
    #
    # num1 = l[0]
    # num2 = l[1]
    # gcd = find_gcd(num1, num2)
    #
    # for i in range(2, len(l)):
    #     gcd = find_gcd(gcd, l[i])
    #
    # print(gcd)

#  Euclid's Algorithm for finding GCD.
