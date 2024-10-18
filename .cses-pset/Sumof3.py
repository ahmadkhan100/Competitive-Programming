n, x = map(int, input().split())
a = list(map(int, input().split()))
arr = [(val, idx + 1) for idx, val in enumerate(a)]
arr.sort()
 
found = False
for i in range(n - 2):
    j = i + 1
    k = n - 1
    while j < k:
        total = arr[i][0] + arr[j][0] + arr[k][0]
        if total == x:
            print(arr[i][1], arr[j][1], arr[k][1])
            found = True
            break
        elif total < x:
            j += 1
        else:
            k -= 1
    if found:
        break
 
if not found:
  print("IMPOSSIBLE")
