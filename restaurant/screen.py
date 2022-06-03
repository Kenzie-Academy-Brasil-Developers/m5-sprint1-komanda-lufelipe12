from .management import add_item_to_tab, calculate_tab, get_item

import os

table_tab = []

os.system("clear")

def initial_screen():
    continue_looping = True

    while continue_looping:
        print('Escolha entre uma das opções:')
        print('1. Adicionar item a comanda')
        print('2. Fechar a comanda')

        option = input('Digite o que deseja fazer: ')

        if option == '1':
            add_item_screen()
        elif option == '2':
            continue_looping = False
            check_out_screen()
        else: 
            os.system("clear")
            print('Digite uma opção válida 1 ou 2\n')


def add_item_screen():
    is_added = False

    while not is_added:
        item_id = input('Digite o id do item: ')
        amount = input('Digite a quantidade do item: ')

        added = add_item_to_tab(table_tab, int(item_id), int(amount))

        if added:
            os.system("clear")

            for item in table_tab:
                print(f'{item["amount"]} {item["name"]} adicionado(s) a comanda!\n')

            is_added = True

        else:
            os.system("clear")
            print(f'{item_id} não é um id de item válido\n')


def check_out_screen():
    os.system('clear')
    total_price = 0
    quit = False

    for item in table_tab:
        total_price += item['price']*item['amount']

    while not quit:
        os.system('clear')
        for index, item in enumerate(table_tab):
            print(f'Item {index + 1}: {item["amount"]} {item["name"]} - R$ {item["price"] * item["amount"]}')
        
        print('-' * 50)
        print(f'R$ {total_price}')


        exit = input('Digite F para sair do sistema\n')

        if exit.upper() == 'F':
            quit = True
