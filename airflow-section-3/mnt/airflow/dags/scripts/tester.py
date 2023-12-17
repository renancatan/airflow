d = [1,2,3,3,4]
data = [str(x) for x in d]
print(data)

sets = list(set(data))
print(sets)
l = []
for x in sets:
    if str(sets) not in x:
        l.append(x)


print(l)