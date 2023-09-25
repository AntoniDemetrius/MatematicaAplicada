class Objeto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def transladar(self, dx, dy):
        self.x += dx
        self.y += dy

    def __str__(self):
        return f'Objeto na posição ({self.x}, {self.y})'

# Função para entrada de valores inteiros
def input_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

# Criar um objeto com coordenadas iniciais
x_inicial = input_int("Digite a coordenada x inicial: ")
y_inicial = input_int("Digite a coordenada y inicial: ")
objeto = Objeto(x_inicial, y_inicial)

# Realizar a translação
dx = input_int("Digite o deslocamento em x: ")
dy = input_int("Digite o deslocamento em y: ")
objeto.transladar(dx, dy)

# Exibir o resultado
print(objeto)