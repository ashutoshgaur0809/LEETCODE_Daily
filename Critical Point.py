a = [5,3,1,2,5,1,2]

l = []
for i in range(1, len(a) - 1):  # Iterate over indices from 1 to len(a) - 2
    if (a[i-1] < a[i] and a[i+1] < a[i]) or (a[i-1] > a[i] and a[i+1] > a[i]):
        l.append(a[i])

print("Critical Points in an array - ")
print(l)
