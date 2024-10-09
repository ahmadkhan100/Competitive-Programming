# lol if you are reading this has been my shortest piece of code in comp programming, no wonder i implemented it in python, to just make it look shorter.

# Read input
n = int(input())
t_list = list(map(int, input().split()))
 
sum_t = sum(t_list)
max_t = max(t_list)
min_total_time = max(sum_t, 2 * max_t)
print(min_total_time)
