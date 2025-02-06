def power(value, exponent):
    """Raise a value to an exponent"""
    result = value
    for _ in range(exponent-1):
        result *= value
    return result

def square_root(x):
   """Raise Value Error"""
   if x < 0:
      raise ValueError("Cannot compute square root of negative number yet!")
   return x ** 0.5