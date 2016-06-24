__author__ = 'Ben'


"""
Polynomial manipulations.
Polynomials are represented as lists of coefficients, 0 order first.
"""

def evaluate(x, poly):
    """
    Evaluate the polynomial at the value x.
    poly is a list of coefficients from lowest to highest.

    :param x:     Argument at which to evaluate
    :param poly:  The polynomial coefficients, lowest order to highest
    :return:      The result of evaluating the polynomial at x
    """

    if len(poly) == 0:
        return 0
    else:
        return x*evaluate(x,poly[1:]) + poly[0]


def bisection(a, b, poly, tolerance):
    """
    Assume that poly(a) <= 0 and poly(b) >= 0.
    Modify a and b so that abs(b-a) < tolerance and poly(b) >= 0 and poly(a) <= 0.
    Return (a+b)/2
    :param a: poly(a) <= 0
    :param b: poly(b) >= 0
    :param poly: polynomial coefficients, low order first
    :param tolerance: greater than 0
    :return:  an approximate root of the polynomial
    """
    if evaluate(a, poly) > 0:
        raise Exception("poly(a) must be <= 0")
    if evaluate(b,poly) < 0:
        raise Exception("poly(b) must be >= 0")
    mid = (a+b) / 2
    if abs(b-a) <= tolerance:
        return mid
    else:
        val = evaluate(mid,poly)
        if val <= 0:
            return bisection(mid, b, poly, tolerance)
        else:
            return bisection(a, mid, poly, tolerance)