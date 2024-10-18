def three_sum_indices(n, x, arr):
    """
    Returns the indices of three values in the array that sum up to x.
    
    :param n: Array size
    :param x: Target sum
    :param arr: List of integers
    :return: List of three indices (1-indexed) or "IMPOSSIBLE"
    """
    # Create a hashmap for efficient lookups
    num_map = {val: i + 1 for i, val in enumerate(arr)}
    
    # Iterate over the array to find the first two values
    for i in range(n):
        for j in range(i + 1, n):
            # Calculate the remaining value needed to reach the target sum
            remaining = x - arr[i] - arr[j]
            
            # Check if the remaining value exists in the hashmap
            # and is not at the same index as the first two values
            if remaining in num_map and num_map[remaining] not in (i + 1, j + 1):
                return [i + 1, j + 1, num_map[remaining]]
    
    # If no solution is found, return "IMPOSSIBLE"
    return "IMPOSSIBLE"

# Example usage
n, x = map(int, input().split())
arr = list(map(int, input().split()))

result = three_sum_indices(n, x, arr)
if result == "IMPOSSIBLE":
    print(result)
else:
    print(*result)
