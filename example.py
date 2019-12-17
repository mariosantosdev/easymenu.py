from EasyMenu import *

option = {
    "Sim" : "print('Hello, World!')",
    "Não" : "exit()"
}

menu = menu_nocolor.Menu(options=option, question='Deseja continuar ?', qchoice='Escolha uma opção: ')
eval(menu.display())
