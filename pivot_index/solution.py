def pivot_index(numbers):
    left_sum = []
    for idx, val in enumerate(numbers):
        if idx == 0:
            left_sum.append(val)
        else:
            left_sum.append(val + left_sum[idx - 1])

    right_sum = []
    for idx in range(len(numbers) - 1, -1, -1):
        if idx == len(numbers) - 1:
            right_sum.append(numbers[idx])
        else:
            right_sum.append(numbers[idx] + right_sum[len(numbers) - 1 - idx - 1])

    pivot = -1
    for idx in range(0, len(numbers)):
        if left_sum[idx] == right_sum[len(numbers) - 1 - idx]:
            pivot = idx
            break

    return pivot
