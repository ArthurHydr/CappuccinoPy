QUANTIDADE_COPO = float(input("Digite quantos copos utilizará: "))
TAMANHO_COPO = float(input("Digite o tamanho em ml do seu copo: "))

def medirColheres():
    primeiraRegra = 14 * QUANTIDADE_COPO
    quantidadeColher = primeiraRegra / 7
    print(f'{quantidadeColher} colheres de sopa!')

def medirAguaELeite():
    quantAgua = TAMANHO_COPO / 7
    quantLeite = TAMANHO_COPO - quantAgua
    print(f'{quantAgua:.2f} ml de água!')
    print(f'{quantLeite:.2f} ml de leite!')


def resultado():
    medirColheres()
    medirAguaELeite()

resultado()

input("Aperte qualquer tecla para fechar...")