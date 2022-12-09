def get_fibo():
    x=0
    y=1
    while True:
        yield x
        yield y
        prevy = y
        x+= + y
        y = prevy + x

fibo_gen = get_fibo()
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))
print(next(fibo_gen))