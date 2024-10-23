def count_divisible_subarrays(n, arr):
    mod_count = {0: 1}  # There is one empty subarray with a sum divisible by n
    prefix_sum = 0
    result = 0

    for num in arr:
        prefix_sum += num
        # Calculate the modulo, ensuring it's positive
        mod = prefix_sum % n
        if mod < 0:
            mod += n
        
        # If the same modulo has been seen before, it means we found some subarrays
        if mod in mod_count:
            result += mod_count[mod]
            mod_count[mod] += 1
        else:
            mod_count[mod] = 1

    return result
