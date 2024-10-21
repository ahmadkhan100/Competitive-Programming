def count_subarrays_with_sum(arr, n, target_sum):
    count = 0
    current_sum = 0
    left = 0
    
    # Using sliding window approach
    for right in range(n):
        current_sum += arr[right]
        
        # Adjust the window by moving the left pointer to maintain the target sum
        while current_sum > target_sum and left <= right:
            current_sum -= arr[left]
            left += 1
        
        # If the current sum matches the target, increment the count
        if current_sum == target_sum:
            count += 1
    
    return count
