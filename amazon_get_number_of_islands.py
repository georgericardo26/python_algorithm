"""
Given a 2 dimension array matrix of 0s and 1s, count the number of islands of 1s.
An island is surrounded by a group of adjacent cells that are all 1s. A cell can only be adjacent to each
other horizontally and vertically.
"""


def get_number_of_islands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    number_islands = 0

    visited = [[0 for col in range(cols)] for row in range(rows)]


    for row in range(rows):
        for col in range(cols):
            print("row", row)
            print("col", col)
            number_islands += get_island(matrix, row, col, visited)

    return number_islands


def get_island(matrix, row, col, visited):
    print("row", row)
    print("col", col)

    if not is_valid(matrix, row, col) or matrix[row][col] == "0" or visited[row][col] == "1":
        return 0

    visited[row][col] = "1"

    get_island(matrix, row, col + 1, visited)
    get_island(matrix, row, col - 1, visited)
    get_island(matrix, row + 1, col, visited)
    get_island(matrix, row - 1, col, visited)

    return 1


def is_valid(matrix, row, col):
    rows = len(matrix)
    cols = len(matrix[0])

    return row >= 0 and row < rows and col >= 0 and col < cols

if __name__ == '__main__':
    result = get_number_of_islands(
        [["0"],
         ["1"]]
    )
    print(result)

    # result = get_number_of_islands(
    #     [["1", "0", "1", "1", "1"],
    #      ["1", "0", "1", "0", "1"],
    #      ["1", "1", "1", "0", "1"]]
    # )
    # print(result)

    # result = get_number_of_islands(
    #     [["0", "1", "0", "1", "0"],
    #      ["0", "0", "1", "1", "1"],
    #      ["1", "0", "0", "1", "0"],
    #      ["0", "1", "1", "0", "0"],
    #      ["1", "0", "1", "0", "1"]]
    # )
    # print(result)

#
# def get_number_of_islands(binaryMatrix):
#     rows = len(binaryMatrix)
#     cols = len(binaryMatrix[0])
#     # you can use Set if you like
#     # or change the content of binaryMatrix as it is visited
#
#     ### Create a second matrix with all 0 to mark when this position was visited. ###
#     visited = [[0 for col in range(cols)] for r in range(rows)]
#     #### ------ #######
#
#     number_of_island = 0
#     for row in range(rows):
#         for col in range(cols):
#             number_of_island += get_island(binaryMatrix, row, col, visited)
#     return number_of_island

#
# # get a continuous island
# def get_island(binaryMatrix, row, col, visited):
#     if not is_valid(binaryMatrix, row, col) or visited[row][col] == "1" or binaryMatrix[row][col] == "0":
#         return 0
#
#     # mark as visited
#     visited[row][col] = "1"
#
#     get_island(binaryMatrix, row, col + 1, visited)
#     get_island(binaryMatrix, row, col - 1, visited)
#     get_island(binaryMatrix, row + 1, col, visited)
#     get_island(binaryMatrix, row - 1, col, visited)
#     return 1
#
# #
# def is_valid(binaryMatrix, row, col):
#     rows = len(binaryMatrix)
#     cols = len(binaryMatrix[0])
#     return row >= 0 and row < rows and col >= 0 and col < cols
#
#
# if __name__ == '__main__':
#     # result = get_number_of_islands(
#     #     [[0, 1, 0, 1, 0],
#     #      [0, 0, 1, 1, 1],
#     #      [1, 0, 0, 1, 0],
#     #      [0, 1, 1, 0, 0],
#     #      [1, 0, 1, 0, 1]]
#     # )
#     # print(result)
#
#     result = get_number_of_islands(
#             [["1", "0", "1", "1", "1"],
#              ["1", "0", "1", "0", "1"],
#              ["1", "1", "1", "0", "1"]]
#     )
#     print(result)