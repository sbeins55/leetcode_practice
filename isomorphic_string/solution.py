def is_isomorphic(s: str, t: str) -> bool:
    s_to_t = {}
    t_to_s = {}

    isomorphic = True
    for i in range(0, len(s)):
        if s[i] in s_to_t:
            if s_to_t[s[i]] != t[i]:
                isomorphic = False
                break
        else:
            s_to_t[s[i]] = t[i]

        if t[i] in t_to_s:
            if t_to_s[t[i]] != s[i]:
                isomorphic = False
                break
        else:
            t_to_s[t[i]] = s[i]

    return isomorphic
