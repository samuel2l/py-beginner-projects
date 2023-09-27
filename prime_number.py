def prime_checker(number):
    if 1 < number < 3:
        print("It's a prime number.")

    elif number <= 1:
        print("It's not a prime number.")

    elif number % 2 == 0 or number % 3 == 0:
        if number == 2 or number == 3:
            pass
        print("It's not a prime number.")
    else:
        print("It's a prime number.")


n = int(input("Check this number: "))
prime_checker(number=n)
