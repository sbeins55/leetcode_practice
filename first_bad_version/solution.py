def first_bad_version(n, is_bad_version):
    start = 0
    end = n
    median = (start + end) // 2
    while end - start > 1:
        if is_bad_version(median):
            end = median
        else:
            start = median + 1
        median = (start + end) // 2

    result = -1
    if is_bad_version(start):
        result = start
    elif is_bad_version(end):
        result = end

    return result
