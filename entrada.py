from getpass import getpass

def func_entrada(tipo, msg, limite = False, lim_sup = -1):
    while True:
        try:
            if tipo == getpass:
                entrada = getpass(prompt=msg)
            else:
                entrada = tipo(input(msg))
        except KeyboardInterrupt:
            print('\nAté logo!\n')
            exit()
        except ValueError:
            print('Entrada inválida!')
            print('Nova entrada: ', end='')
        else:
            if tipo == str:
                aux = entrada.split()
                continuar = True
                for palavra in aux:
                    if not palavra.isalnum():
                        continuar = False
                        break

                if continuar:
                    break
                else:
                    print('Entrada inválida!')
                    print('Nova entrada: ', end='')

            else: 
                if not limite: break
                else:
                    if 1 <= entrada <= lim_sup: break
                    else:
                        print('Valor inválido!')
                        print('Nova entrada: ', end='')

    return entrada
