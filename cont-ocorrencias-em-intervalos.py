# Solicite ao usuário que pressione 1 para iniciar
start = int(input("Pressione 1 para iniciar: "))

# Solicite o número de classes
n_classes = int(input("Informe o número de classes: "))

# Solicite os dados como uma string separada por ponto e vírgula e converta em uma lista de floats
dados_string = input("Coloque os dados aqui:\n")
dados = [float(num.strip()) for num in dados_string.split(';')]

# Solicite o valor de delta
delta = float(input('Informe o delta: '))

# Solicite o limite inferior
Linf = float(input("Informe o valor do limite inferior: "))
Lsup = Linf + delta

cont = 0

while start == 1:
    if n_classes > 0:
        sentido_fechado = int(input("""Escolha o tipo de intervalo:
[ 1 ] - Intervalo fechado à esquerda.
[ 2 ] - Intervalo fechado à direita.
[ 3 ] - Intervalo fechado em ambos os lados.
Escolha uma opção: """))
        

        # Inicialize a contagem para este intervalo
        cont_intervalo = 0

        for valor in dados:
            if sentido_fechado == 1 and Linf <= valor < Lsup:
                cont_intervalo = cont_intervalo + 1
            elif sentido_fechado == 2 and Linf < valor <= Lsup:
                cont_intervalo = cont_intervalo + 1
            elif sentido_fechado == 3 and Linf <= valor <= Lsup:
                cont_intervalo = cont_intervalo + 1

        print(f"\n{Linf:.2f} ---- {Lsup:.2f} ==> {cont_intervalo}")
        print(f"Há {cont_intervalo} ocorrências no intervalo entre {Linf:.2f} e {Lsup:.2f}\n")

        cont = cont + cont_intervalo
        n_classes = n_classes - 1

        if n_classes == 0:
            print('Fim do programa.')
            start = 0
        else:
            start = int(input('Deseja continuar (1 para sim, 0 para não): '))

    Linf = Lsup
    Lsup = Linf + delta

print(f'Total de dados avaliados: {cont}')
print(dados)
