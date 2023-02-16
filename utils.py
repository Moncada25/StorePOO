def validate_number(message):

    while True:

        try:
            option = int(input(message))
            return option
        except ValueError:
            print('\nIngrese una opción válida'.upper()+'\n')
            continue
