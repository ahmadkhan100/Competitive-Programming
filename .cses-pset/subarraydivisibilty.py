def count_subarrays_divisible_by_n(arr, n):
    remainder_count = {0: 1}  # To handle subarrays starting from the beginning
    current_sum = 0
    count = 0
    
    # Iterate over the array and keep track of prefix sums and remainders
    for num in arr:
        current_sum += num
        remainder = current_sum % n
        
        # Handle negative remainders to make sure they are in the range [0, n-1]
        if remainder < 0:
            remainder += n
        
        # If this remainder has been seen before, add the count of occurrences to result
        if remainder in remainder_count:
            count += remainder_count[remainder]
        
        # Update the count of this remainder in the hashmap
        remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
    
    return count
