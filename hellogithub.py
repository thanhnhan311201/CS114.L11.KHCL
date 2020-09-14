inp = int(input())
st = str(inp)
lst = list(st)
K = len(lst)
sum = 0
for item in range(0, K):
    lst[item] = int(lst[item])
    sum += lst[item] ** K
if (sum == inp):
    print('True')
else:
    print('False')