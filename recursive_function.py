
def print_number(i, numbers, fill):

    print("posicao: ", i)

    if not is_valid(i, numbers) or fill[i] == 1:
        print("caiu aqui")
        return 0

    fill[i] = 1

    print_number(i+1, numbers, fill)
    print("passou o primeiro")
    print_number(i-1, numbers, fill)
    print("passou o segundo")
    print_number(i+2, numbers, fill)
    print("passou o terceiro")

    print("foi ate o final")
    return 1


def is_valid(i, numbers):
    n = len(numbers)
    print(i >= 0 and i < n)
    return i >= 0 and i < n

# def stop_in_zero(n):
#     print("esta em: ", n)
#     if n == 6:
#         return 0
#     stop_in_zero(n + 1)
#     return 1


if __name__ == '__main__':
    # result = 0
    # for i in range(6):
    #     result += stop_in_zero(i)
    #
    # print("final result", result)

    numbers = [1, 3, 5, 7]
    n = len(numbers)
    fill = [0 for _ in numbers]
    result = 0
    for i in range(n):
        result += print_number(i, numbers, fill)

    print(result)


# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(6)