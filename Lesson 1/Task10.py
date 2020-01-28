l1 = list('список')
l2 = list('записок')

diff = set(l1) ^ set(l2)

l3 = list(diff)
print (l3)