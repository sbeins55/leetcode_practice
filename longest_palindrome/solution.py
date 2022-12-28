def longest_palindrome(s):
    """
    Given a string s which consists of lowercase or uppercase letters,
    return the length of the longest palindrome that can be built with those letters.

    Examples
        - abccccdd = 7 => dccaccd
        - a = 1        => a

    :param s: a string with uppercase and lowercase letters
    :return: the length of the longest palindrome
    """
    letters = {}
    for c in s:
        if c in letters:
            letters[c] += 1
        else:
            letters[c] = 1

    count = 0
    for key, val in letters.items():
        count += val // 2 * 2

    return min(count + 1, len(s))