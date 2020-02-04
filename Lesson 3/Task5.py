def foo(*a):
    x = max(a)
    for i in a:
        if abs(x) > abs(i):
            x = i
    return x

print(foo(1, 2, -0.5, 0.75, 22, -0.05))