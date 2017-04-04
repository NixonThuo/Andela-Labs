def fizz_buzz(number):
    while number > 0 and isinstance(number, int):
        if number % 3 == 0 and number % 5 != 0:
            return "Fizz"
        elif number % 5 == 0 and number % 3 != 0:
            return "Buzz"
        elif number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        else:
            return number
    else:
        return "Invalid Argument"
