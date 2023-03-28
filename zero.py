n = int(input())
arr = []
total = 0
for i in range(0,n):
    x = input()
    head = 0
    if int(x) == 0:
        head = head - 1
        arr.pop(head)
    else:
        arr += x
        head += 1
for ele in range(0,len(arr)):
    total += int(arr[ele])
print(total)