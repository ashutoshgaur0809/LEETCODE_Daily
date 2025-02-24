a = [4,9,5]
b = [9,4,9,8,4]

l = []
for i in a:
    if i in b:
        l.append(i)
    
print(set(l))
