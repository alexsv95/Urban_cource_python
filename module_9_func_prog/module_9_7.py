
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        num_prime = True
        for i in range(2, result):
            if result % i == 0:
                check_prime = False
                break
        if num_prime:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_

result = sum_three(2, 3, 6)
print(result)