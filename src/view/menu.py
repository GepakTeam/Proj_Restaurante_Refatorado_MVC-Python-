def introduction_page():
    message = '''
Sistema Restaurante

1 - Cadastrar
2 - Cadastro de Clientes
3 - Utilitarios
5 - Sair
'''
    print(message)
    command = int(input("Comando: "))
    return command

def menu() -> None:
    while True:
        command = introduction_page()

        if command == 1 :
            print("opcao 1 ...")
            input("")

        elif command == 2 :
            "()"

        elif command == 5 :
            exit()
        else: print('\n Comando não encontrado!! \n\n')