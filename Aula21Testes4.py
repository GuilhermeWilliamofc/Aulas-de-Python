def somar(a=0, b=0, c=0):
    """somar _summary_

    Args:
        a (int, optional): first value. Defaults to 0.
        b (int, optional): second value. Defaults to 0.
        c (int, optional): third value. Defaults to 0.

    Returns:
        _type_: _description_
    """
    s = a + b + c
    return s

r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')