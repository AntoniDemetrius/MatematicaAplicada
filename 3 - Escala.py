#Escreva um programa que realize a escala de um objeto em relação a um ponto específico e exiba o resultado na tela.
def escalar_objeto(objeto, ponto_referencia, fator_escala):
    # Inicialize uma lista para armazenar os novos pontos do objeto escalado
    objeto_escalado = []

    # Itere sobre cada ponto no objeto e aplique a escala em relação ao ponto de referência
    for ponto in objeto:
        # Calcule as novas coordenadas do ponto escalado
        novo_x = ponto_referencia[0] + (ponto[0] - ponto_referencia[0]) * fator_escala
        novo_y = ponto_referencia[1] + (ponto[1] - ponto_referencia[1]) * fator_escala

        # Adicione as novas coordenadas à lista do objeto escalado
        objeto_escalado.append((novo_x, novo_y))

    return objeto_escalado

# Função para exibir os pontos de um objeto
def exibir_objeto(objeto):
    for ponto in objeto:
        print(f'({ponto[0]}, {ponto[1]})')

# Solicitar entrada do usuário para o objeto e fator de escala
objeto = [(1, 1), (2, 2), (3, 3)]  # Exemplo de objeto, você pode substituir pelos seus próprios pontos
ponto_referencia = (2, 2)  # Ponto de referência para a escala
fator_escala = float(input("Digite o fator de escala: "))

# Realizar a escala do objeto
objeto_escalado = escalar_objeto(objeto, ponto_referencia, fator_escala)

# Exibir o objeto original e o objeto escalado
print("Objeto Original:")
exibir_objeto(objeto)

print("\nObjeto Escalado:")
exibir_objeto(objeto_escalado)
