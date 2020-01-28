d = {1: 1, 2: 4, 3: 5, 6: 1, 5: 8, 4: 1, 7: 3}
s = set(d.values())
l = list(s)
l.sort()
l.reverse()
print (l[0:3])

