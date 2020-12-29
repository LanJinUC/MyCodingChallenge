def isValidSubsequence(array, sequence):
    index = 0
    result = []
    i = 0
    while i <= len(array) - 1:
        if array[i] == sequence[index] and index <= len(sequence) - 1:
            result.append(array[i])
            if index == len(sequence) - 1:
                break
            else:
                index += 1
        i += 1

    return len(result) == len(sequence)