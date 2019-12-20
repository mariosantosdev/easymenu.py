from EasyMenu import menu_nocolor
option = {
    "Sim": "print('Hello, World!')",
    "Não": "exit()"
}

menu = menu_nocolor.Menu(option, 'Deseja continuar ?', 'Escolha uma opção: ')
eval(menu.display())
