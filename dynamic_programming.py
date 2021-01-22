def fib(n):
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib(n-1) + fib(n-2)

    return result


def get_fibonacci(n):
    memo = [0 for _ in range(n + 1)]
    result = fib_memo(n, memo)
    return result


def fib_memo(n, memo):
    a = memo
    if memo[n] != 0:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
        memo[n] = result
    return result


def get_fibonacci_with_bottom_up(n):
    bottom_up = [0 for _ in range(n + 1)]
    result = fib_bottom_up(n, bottom_up)
    return result


def fib_bottom_up(n, bottom_up):
    if n == 1 or n == 2:
        bottom_up[n] = 1
        return bottom_up[n]

    bottom_up[1] = 1
    bottom_up[2] = 1

    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i - 1] + bottom_up[i - 2]
        n = i

    return bottom_up[n]


# test = get_fibonacci_with_bottom_up(1000)
#
# print(test)

# memo = [0] * (6)


"""
1. 16
2. fib(16-1)     +       fib(16-2)
    fib(15)
    
    
    Bad pratice = O(2n)
        
"""

############# Code Test ###############
"""
A partir de um array, encontre o subconjunto deste array
arr = [2, 4, 6, 10] que somados resultam em 16
"""

def count_sets(arr, total):
    return rec(arr, total, len(arr) - 1)

def rec(arr, total, i):
    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        return rec(arr, total, i - 1)
    else:
        return rec(arr, total - arr[i], i - 1) + rec(arr, total, i - 1)


def count_sets_memo(arr, total):
    memo = {}
    return rec_memo(arr, total, len(arr) - 1, memo)


def rec_memo(arr, total, i, memo):
    key = f"{str(total)}:{str(i)}"
    if key in memo:
        return memo["key"]

    if total == 0:
        return 1
    elif total < 0:
        return 0
    elif i < 0:
        return 0
    elif total < arr[i]:
        to_return = rec(arr, total, i - 1)
    else:
        to_return = rec(arr, total - arr[i], i - 1) + rec(arr, total, i - 1)
    memo[key] = to_return
    return to_return


result = count_sets_memo([2, 4, 6, 10], 16)
print(result)
# def find_sets_numbers_add_up_n(final_number):
#     sets = []
#     set = []
#     for n in range(final_number):
#         temp_n = sum(set + [n])
#         if temp_n == final_number:
#             set.extend(n)
#             sets.append(set)
