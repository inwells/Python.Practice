def prime_checker(number):
    digit_total = 0
    for digit in number:
        digit_total += int(digit)
    integer = int(number)
    if (integer % 2) == 0 and not (integer / 2) == 1:
        print(f"{integer} is not prime. It is divisible by 2.")
    elif (integer % 5) == 0 and not (integer / 5) == 1:
        print(f"{integer} is not prime. It is divisible by 5.")
    elif (digit_total % 3) == 0:
        print(f"{integer} is not prime. The sum of the digits are divisible by 3.")
    else: 
         print(f"{integer} is prime.")


n = (input("Check this number:"))
prime_checker(number=n)