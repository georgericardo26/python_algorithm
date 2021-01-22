"""
Hi, here's your problem today. This problem was recently asked by Apple:

Given a string, we want to remove 2 adjacent characters that are the same, and repeat the process with the new string until we can no longer perform the operation.

Here's an example and some starter code:

def remove_adjacent_dup(s):
  # Fill this in.

print(remove_adjacent_dup("cabba"))
# Start with cabba
# After remove bb: caa
# After remove aa: c
# print c
"""
import re


def remove_adjacent_dup(word, i=None):
    has_repeatble = True

    index = 0

    while has_repeatble:
        letter = word[index]
        combination = ""
        s = re.findall("("+letter+"){2,}", word)
        if s:
            index_l = word.index(s[0])
            for i in range(index_l, len(word)):
                if word[i] == letter:
                    combination += letter
                else:
                    break
            index = 0
            word = word.replace(combination, "")
        else:
            index += 1

        if index >= len(word):
            has_repeatble = False
    return word


if __name__ == '__main__':
    print(remove_adjacent_dup("ccaeebbia"))