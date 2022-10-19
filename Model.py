import View
import Controller

expression_list: str = ''
result: int = 0
first = 0
second = 0
ops = ''

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

def init_first():
    global first
    first = Controller.input_integer('Введите число: ')

def init_second():
    global second
    second = Controller.input_integer('Введите число: ')

def init_ops():
    global ops
    ops = Controller.input_operation('Введите операцию: ')
    if ops == '=':
        View.print_total()
        return True


