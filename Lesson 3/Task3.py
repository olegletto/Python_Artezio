maximum = 0
def foo(*a):
    global maximum
    if maximum < max(a):
        maximum = max(a)
    res = 0
    for i in a:
        res += i
    average = res / len(a)
    
    return [average, maximum]
    

print(foo(1,2,3,4)) # -> 2.5, 4
print(foo(-3, -2, 10, 1)) # -> 1.5, 10
print(foo(7,8,8,1)) # -> 6, 10