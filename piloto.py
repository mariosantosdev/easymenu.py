from EasyMenu import menu, menu_nocolor

style = input('Quer o menu com cores? [S]im ou [N]ão\n>> ').upper().strip()[0]

option = {
    "Sim": "print('Hello, World!')",
    "Não": "exit()"
}

parametros = [option, 'Deseja continuar ?', 'Escolha uma opção: ']

if style == 'S':
    menu = menu.Menu(*parametros)
    eval(menu.display())

elif style == 'N':
    question = "Deseja continuar?"
    menu = menu_nocolor.Menu(*parametros)
    eval(menu.display())
else:
    print('Opção inválida')
