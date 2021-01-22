def addTwoDigits(n):
    num_str = str(n)
    convert_to_list = [int(n) for n in num_str]
    return sum(convert_to_list)


if __name__ == '__main__':
    print(addTwoDigits(295))