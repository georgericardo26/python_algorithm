

# def countMoves(numbers):
#     number_of_moves = 0
#     new_arr = []
#
#     number_of_moves = get_number_of_moves(numbers, new_arr)
#
#     return number_of_moves
#
#
# def get_number_of_moves(numbers, new_arr):
#
#     if
#
#     for n in range(numbers):
#         get_number_of_moves()




# result = countMoves([3, 4, 6, 6, 3])
# print(result)

#
# def countMinimumMoves(arr, n, k):
#     # Check if it is possible or not
#     # That is if all the elements from
#     # index K to N are not equal
#     for i in range(k - 1, n):
#         if (arr[i] != arr[k - 1]):
#             return -1
#
#     # Find minimum number of moves
#     for i in range(k - 1, -1, -1):
#         if (arr[i] != arr[k - 1]):
#             return i + 1
#
#     # Elements are already equal
#     return 0
#
#
# # Driver Code
# if __name__ == "__main__":
#     # arr = [1, 2, 3, 4]
#     arr = [3, 4, 6, 6, 3]
#     K = 4
#
#     n = len(arr)
#
#     print(countMinimumMoves(arr, n, K))


# Python 3 for finding minimum
# operation required

# function for finding array sum
def arraySum(arr, n):
    sm = 0
    i = 0

    while (i < n):
        sm = sm + arr[i]
        i = i + 1
    return sm


# function for finding smallest
# element
def smallest(arr, n):
    small = 1000000000

    for i in range(0, n):

        if (arr[i] < small):
            small = arr[i]
    return small


# function for finding min
# operation
def minOp(arr):
    n = len(arr)
    # find array sum
    sm_arr = sum(arr)
    # sm = arraySum(arr, n)

    # find the smallest element from
    # array
    small = min(arr)

    # calculate min operation required
    minOperation = sm_arr - (n * small)

    # return result
    return minOperation


# Driver function
# arr = [5, 6, 2, 4, 3]
arr = [3, 4, 6, 6, 3]
n = len(arr)
print("Minimum Operation = ", minOp(arr))

# This code is contributed by Nikita Tiwari.


"""
Two approaches:
    - The first one would be travessing the elements and increasing all elements
    except the largest element until all elements became equals.
    
    But this approach is bad because we woud have a time complexity O(nˆ2)
    
    - The second one was doing the inverse path, decreasing the largest elements, so we dont need increse the 
    smallest elements anymore. The mathematic formula is: Sum(Arr) - n * smallestElement.
"""