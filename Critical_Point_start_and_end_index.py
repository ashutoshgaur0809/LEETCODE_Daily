# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
  

a = [5,3,1,2,5,1,2]

l = []
for i in range(1, len(a) - 1):  # Iterate over indices from 1 to len(a) - 2
    if (a[i-1] < a[i] and a[i+1] < a[i]) or (a[i-1] > a[i] and a[i+1] > a[i]):
        l.append(a[i])

print("Critical Points in an array - ")
print(l)


si = 0 
ei = 0

for i in range(1,len(a)-1):
    if l[0] == a[i]:
        si = i
        break

for i in range(len(a)-1,0,-1):
    if l[-1] == a[i]:
        ei = i
        break

print("start index of critical -> ",si)
print("end index of critical -> ",ei)
