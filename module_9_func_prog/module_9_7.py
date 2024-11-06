
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        for i in range(2, result):
            if result % i == 0:
                print('Составное')
                break
            else:
                print('Простое')
                break
        return result
    return wrapper


@is_prime
def sum_three(*args):
    sum_ = 0
    for i in args:
        sum_ += i
    return sum_

result = sum_three(2, 3, 7)
print(result)