def reinicia():
    x = input("Digite 'r' para recomeçar ou qualquer tecla para sair: ")

    if x == 'r':
        bemvindo()
    else:
        print("\n Até logo.")

def bemvindo():

    print('''*CALCULADORA*''')
    num_1 = int((input("Digite o primeiro número: ")))
    num_2 = int((input("Digite o segundo número: ")))
    calcula(num_1,num_2)

def calcula(num_1,num_2):

    print('''Escolha o sinal que representa a operacao que deseja realizar:
                 + para somar
                 - para subtrair
                 * para multiplicar
                 / para dividir''')

    operacao = input("Digite o sinal: ")

    if operacao == '+':
        soma(num_1, num_2)

    elif operacao == '-':
        subtrai(num_1, num_2)

    elif operacao == '*':
        multiplica(num_1, num_2)

    elif operacao == '/':
        divide(num_1, num_2)

    else:
        print("Entrada inválida")

def soma(num_1,num_2):
    resultado = (num_1 + num_2)
    print("somatorio: ", resultado)
    reinicia()

def subtrai(num_1,num_2):
    resultado = (num_1 - num_2)
    print("subtracao: ", resultado)
    reinicia()

def multiplica(num_1,num_2):
    resultado = (num_1 * num_2)
    print("multiplicacao: ", resultado)
    reinicia()

def divide(num_1,num_2):
    resultado = (num_1 / num_2)
    print("divisao: ", resultado)
    reinicia()

bemvindo()