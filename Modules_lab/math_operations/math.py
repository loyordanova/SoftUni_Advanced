mapper = {
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b,
    '-': lambda a, b: a - b,
    '+': lambda a, b: a + b,
    '^': lambda a, b: a ** b,
}


def calculate(*args):
    num1, sign, num2 = args[0], args[1], args[2]
    result = mapper[sign](float(num1), int(num2))
    return f'{result:.2f}'

