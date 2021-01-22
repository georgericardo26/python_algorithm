

def length_of_longest_substring(s):
    blocks = ""
    longest_word = ""
    # last_longest_word = ""

    for i in range(len(s)):
        if s[i] in blocks:
            if len(blocks) > len(longest_word):
                longest_word = blocks

            # get position of the last repeated letter
            pos = blocks.find(s[i])

            # update the block with the sequence of non-repeated letters
            blocks = blocks[pos+1:] + s[i]
            continue

        blocks += s[i]
        # last_longest_word = blocks

    if len(blocks) > len(longest_word):
        return blocks
    return longest_word


if __name__ == '__main__':
    # result = length_of_longest_substring("abcabcbb")
    # result = length_of_longest_substring("pwwkew")
    # result = length_of_longest_substring("bbbbb")
    # result = length_of_longest_substring(" ")
    # result = length_of_longest_substring("dvdf")
    # result = length_of_longest_substring("ynyo")
    result = length_of_longest_substring("anviaj")
    print("The longest word is >>", result, "<< and the size is >>", len(result), "<<")