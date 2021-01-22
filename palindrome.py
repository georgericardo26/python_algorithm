"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?



Example 1:

Input: x = 121
Output: true
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Example 4:

Input: x = -101
Output: false


Constraints:

-231 <= x <= 231 - 1
"""
def is_palindrome(x):
    given_n = x
    reversed_n = 0

    while (x != 0):
        r = int(x % 10)
        reversed_n = reversed_n * 10 + r
        x = int(x / 10)
    return reversed_n == given_n
#
# def is_palindrome(n):
#     given_num = n
#     reversed_n = 0
#     while n != 0:
#         r = int(n % 10)
#         print("r: ", r)
#         reversed_n = reversed_n * 10 + r
#         print("reversed: ", reversed_n)
#
#         n = (n / 10)
#         print("n: ", n)
#
#     return reversed_n


if __name__ == '__main__':
    result = is_palindrome(10)
    print(result)