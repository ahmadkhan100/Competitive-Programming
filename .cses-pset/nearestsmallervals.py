n, *rest = map(int, open(0).read().split())
x = rest[:n]
stack = []
res = []

for i in range(n):
    while stack and x[stack[-1]] >= x[i]:
        stack.pop()
    if not stack:
        res.append(0)
    else:
        res.append(stack[-1] + 1)  # +1 for 1-based indexing
    stack.append(i)

print(' '.join(map(str, res)))
