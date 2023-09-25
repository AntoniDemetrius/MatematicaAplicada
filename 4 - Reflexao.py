#Escreva um programa que realize a reflexão de um objeto em relação a um eixo específico e exiba o resultado na tela.
def refletir_objeto(objeto, eixo):
    # Inicialize uma lista para armazenar os novos pontos do objeto refletido
    objeto_refletido = []

    # Itere sobre cada ponto no objeto e aplique a reflexão em relação ao eixo especificado
    for ponto in objeto:
        x, y = ponto

        if eixo == 'x':
            # Reflexão em relação ao eixo x
            novo_x = x
            novo_y = -y
        elif eixo == 'y':
            # Reflexão em relação ao eixo y
            novo_x = -x
            novo_y = y
        else:
            print("Eixo inválido. Use 'x' ou 'y' como eixo de reflexão.")
            return None

        # Adicione as novas coordenadas à lista do objeto refletido
        objeto_refletido.append((novo_x, novo_y))

    return objeto_refletido

# Função para exibir os pontos de um objeto
def exibir_objeto(objeto):
    for ponto in objeto:
        print(f'({ponto[0]}, {ponto[1]})')

# Solicitar entrada do usuário para o objeto e eixo de reflexão
objeto = [(1, 1), (2, 2), (3, 3)]  # Exemplo de objeto, você pode substituir pelos seus próprios pontos
eixo = input("Digite o eixo de reflexão ('x' ou 'y'): ")

# Realizar a reflexão do objeto
objeto_refletido = refletir_objeto(objeto, eixo)

if objeto_refletido:
    # Exibir o objeto original e o objeto refletido
    print("Objeto Original:")
    exibir_objeto(objeto)

    print("\nObjeto Refletido:")
    exibir_objeto(objeto_refletido)
