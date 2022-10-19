import Model
import View


def delete_element(strings, i):
    strings.pop(i)
    strings.pop(i)


def operation(string, i, oper):
    if string[i] == oper:
        string[i - 1] = Model.opSelect.get(oper)(int(string[i - 1]), int(string[i + 1]))
        delete_element(string, i)
        return True
    return False


def calculate_expression(string: list):
    while len(string) > 1:
        if '*' in string or '/' in string:
            for i in range(len(string)):
                if operation(string, i, '*'):
                    break
                if operation(string, i, '/'):
                    break
        else:
            if '+' in string or '-' in string:
                for i in range(len(string)):
                    if operation(string, i, '+'):
                        break
                    if operation(string, i, '-'):
                        break
    return string


def res_expression(expression: str):
    expression = Model.string_expression(expression)
    while len(expression) > 1:
        expression = calculate_expression(expression)
    Model.result = expression[0]
    View.print_result()


def input_integer(enter):
    while True:
        try:
            a = int(input(enter))
            return a
        except:
            View.error_value()


def input_operation(enter):
    while True:
        a = input(enter)
        if a in ['+', '-', '*', '/', '=']:
            return a
        else:
            View.error_value()


def oper():
    match (Model.ops):
        case '+':
            Model.result = Model.first + Model.second
        case '-':
            Model.result = Model.first - Model.second
        case '*':
            Model.result = Model.first * Model.second
        case '/':
            while Model.second == 0:
                print('На ноль делить нельзя!')
                Model.init_second()
            Model.result = int(Model.first / Model.second)
