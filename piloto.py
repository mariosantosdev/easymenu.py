from EasyMenu import menu, menu_nocolor

style = input('Quer o menu com cores? [S]im ou [N]ão\n>> ').upper().strip()[0]

option = {
    "Sim": "print('Hello, World!')",
    "Não": "exit()"
}

if style == 'S':
    menu = menu.Menu(option, 'Deseja continuar ?', 'Escolha uma opção: ')
    eval(menu.display())

elif style == 'N':
    question = "Deseja continuar?"
    menu = menu_nocolor.Menu(option, question, 'Escolha uma opção: ')
    eval(menu.display())
else:
    print('Opção inválida')
