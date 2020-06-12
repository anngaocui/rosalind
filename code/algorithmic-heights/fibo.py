def fibonacci(number):
    if number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        n = 1
        this_f = 1
        pre_f = 0
        while n < number:
            pre_number = this_f
            this_f += pre_f
            pre_f = pre_number
            n += 1
        return this_f

if __name__ == '__main__':
    print fibonacci(22)