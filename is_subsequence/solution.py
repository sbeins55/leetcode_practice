def is_subsequence(s, t):
    """
    Given two strings s and t, check that s is a subsequence of t

    :param s: a string that can be a subsequence of t
    :param t: a string that can contain a subsequence of s
    :return: a boolean indicating if s is a subsequence in t
    """
    if len(s) < 1:
        return True

    s_idx = 0
    for i in range(len(t)):
        if s[s_idx] == t[i]:
            s_idx += 1

        if s_idx == len(s):
            break

    return s_idx == len(s)
