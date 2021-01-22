
def string_construction(a, b):
    combinate = ""
    words = 0
    size_word = len(a)

    for s in b:
        combinate += s
        if sorted(combinate) == sorted(a):
            words += 1
            combinate = ""
        else:
            if len(combinate) == size_word:
                combinate = ""

    return words


if __name__ == '__main__':
#     # print(string_construction("abc", "abccba"))
#     # print(string_construction("ab", "abcbcb"))
#     # print(string_construction("ab", "abccba"))
    print(string_construction("hnccv", "ncvohcjhdfnhonxddcocjncchnvohchnjohcvnhjdhihsn"))

# Python3 program to print the number of
# times str2 can be formed from str1 using
# the characters of str1 only once
# import sys
#
#
# # Function to find the number of str2
# # that can be formed using characters of str1
# def findNumberOfTimes(str1, str2):
#     freq = [0] * 26
#     l1 = len(str1)
#
#     # iterate and mark the frequencies
#     # of all characters in str1
#     for i in range(l1):
#         freq[ord(str1[i]) - ord("a")] += 1
#     l2 = len(str2)
#     count = sys.maxsize
#
#     # find the minimum frequency of
#     # every character in str1
#     for i in range(l2):
#         count = min(count, freq[ord(str2[i]) -
#                                 ord('a')])
#     return count
#
#
# # Driver Code
# if __name__ == '__main__':
#     str1 = "ab"
#     str2 = "abccba"
#     print(findNumberOfTimes(str1, str2))
#
# # This code is contributed by PrinciRaj1992


