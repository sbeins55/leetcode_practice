def running_sum(numbers):
    solution = []
    for idx, number in enumerate(numbers):
        if idx == 0:
            solution.append(number)
        else:
            solution.append(solution[idx-1] + number)

    return solution
