import Controller
import Model
import View

def Choise():
    print('Вы хотите ввести выражение?')
    choise = int(input('1.Да \n'
                       '2.Нет\n'
                       'Ваш выбор: '))
    while choise == 1:
        Model.expression_list = input('Введите выражение: ')
        Controller.res_expression(Model.expression_list)
        break
    else:
        Model.init_first()
        while True:
            if Model.init_ops():
                break
            Model.init_second()
            Controller.oper()
            View.print_total()
            Model.first = Model.result

Choise()