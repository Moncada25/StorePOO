def validate_number(message):
    while True:

        try:
            option = int(input(message))
            return option
        except ValueError:
            print('\nIngrese una opción válida'.upper() + '\n')
            continue


def show_list(list_to_show, name):
    print(f'Hay {len(list_to_show)} {name}')
    for item in list_to_show:
        item.view()