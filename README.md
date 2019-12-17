# EasyMenu.py

Uma biblioteca feita para facilitar o desenvolvimento de menu interativo no Python 3.6.x

## Como Instalar

Usando o gerenciador de pacotes [pip](https://pypi.org/) para instalar o *EasyMenu*.

```bash
pip install EasyMenu
```

## Como Usar

```python
from easy_menu import easymenu

options = ['Sim', 'Não'] # Data Type <list>
attr = ["print('Continuando...')", "exit()"] # Data Type <list>
question = 'Deseja continuar ?' # Data Type <str>
response = 'Escolha uma opção: ' # Data Type <str>

menu = easymenu.Menu(options, attr, question, response)
menu.menu()
```

## Menu Final
> Menu Com Cor
![](https://i.imgur.com/sQFMTv9.png)

> Menu Sem Cor
![](https://i.imgur.com/vRV2lnJ.png)

## Contribuição
Solicitações de contribuições são bem-vindas. Sempre mantendo a beleza do código e a facilidade de usar.\
Para grandes mudanças, abra um problema primeiro para discutir o que você gostaria de mudar.

## License
[MIT](https://github.com/nvrsantos/easymenu.py/blob/master/LICENSE)
