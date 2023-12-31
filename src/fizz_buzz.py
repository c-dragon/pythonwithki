def fizz_buzz(n: int) -> str:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be non-negative")
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)
