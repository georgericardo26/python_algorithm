import copy

houses = 8


def update_cells(cells):
    new_cells = copy.deepcopy(cells)
    for index, n in enumerate(cells):
        prev = cells[index - 1] if index > 0 else 0
        next = cells[index + 1] if index < (len(cells) - 1) else 0

        if prev == next:
            new_cells[index] = 0
        else:
            new_cells[index] = 1

    return new_cells


def state_cells(cells, days):

    for _ in range(0, days):
        cells = update_cells(cells)

    return cells


if __name__ == '__main__':
    result = state_cells([1, 0, 0, 0, 0, 1, 0, 0], 2)

    print("O resultado é: ", result)
