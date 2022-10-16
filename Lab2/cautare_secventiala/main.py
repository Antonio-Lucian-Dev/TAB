def sequential_search(arr, x):
    for i in range(1):
        if arr[i] == x:
            return i
    return -1

print(sequential_search([1, 2, 3, 4, 5], 3))