import View

exp_list: str = ''
result: int = 0

opSelect = {
    "*": lambda x, y: int(x) * int(y),
    "/": lambda x, y: int(x) / int(y) if int(y) != 0 else View.zero_division(),
    "+": lambda x, y: int(x) + int(y),
    "-": lambda x, y: int(x) - int(y)}


def string_expression(ex_list: str):
    ex_list = ex_list.replace(' ', '').strip()
    ex_list = ex_list.replace('+', ' + ')\
                    .replace('-', ' - ')\
                    .replace('*', ' * ')\
                    .replace('/', ' / ')
    string = ex_list.split()
    return string
