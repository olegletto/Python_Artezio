l = ['abc', 'xyz', 'aba', '1221', 'anna']
c = 0
i = 0
while i < len(l):
    s = l[i]
    if s[0] == s[-1]:
        c += 1
    i += 1

print (c)