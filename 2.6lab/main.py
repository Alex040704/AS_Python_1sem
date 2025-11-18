import math

def add_fractions(frac1, frac2):
    p1, q1 = frac1
    p2, q2 = frac2
    numerator = p1 * q2 + p2 * q1
    denominator = q1 * q2
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

def subtract_fractions(frac1, frac2):
    p1, q1 = frac1
    p2, q2 = frac2
    numerator = p1 * q2 - p2 * q1
    denominator = q1 * q2
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

def multiply_fractions(frac1, frac2):
    p1, q1 = frac1
    p2, q2 = frac2
    numerator = p1 * p2
    denominator = q1 * q2
    gcd = math.gcd(numerator, denominator)
    return (numerator // gcd, denominator // gcd)

if __name__ == "__main__":
    frac_a = (1, 2)
    frac_b = (1, 3)
    
    print(f"{frac_a} + {frac_b} = {add_fractions(frac_a, frac_b)}")
    print(f"{frac_a} - {frac_b} = {subtract_fractions(frac_a, frac_b)}")
    print(f"{frac_a} * {frac_b} = {multiply_fractions(frac_a, frac_b)}")
