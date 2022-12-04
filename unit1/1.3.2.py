def is_prime(number):
    return 0 not in [number%x for x in range(2,number)]

print(is_prime(42))
print(is_prime(43))