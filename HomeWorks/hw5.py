def find_pairs(arr, target):
    n = len(arr)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                pairs.append((arr[i], arr[j]))
    return pairs


arr = [1, 2, 3, 4, 5]
target = 6
print(find_pairs(arr, target))  # [(1, 5), (2, 4)]