import Model

def zero_division():
    print('Делить на ноль нельзя!')
    exit()

def print_result():
    return print(f'{Model.expression_list} = {Model.result}')


def error_value():
    return print('Ошибка ввода данных')

def print_total():
    return print(f'Результат: {Model.result}')