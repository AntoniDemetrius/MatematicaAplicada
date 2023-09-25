#Escreva um programa que faça a rotação de um objeto em torno de um ponto específico e exiba o resultado na tela.
import math

# Função para realizar a rotação de um ponto (x, y) em torno de um ponto (cx, cy) por um ângulo em graus.
def rotate_point(x, y, cx, cy, angle_degrees):
    # Converter ângulo de graus para radianos
    angle_radians = math.radians(angle_degrees)
    
    # Calcular as novas coordenadas após a rotação
    new_x = math.cos(angle_radians) * (x - cx) - math.sin(angle_radians) * (y - cy) + cx
    new_y = math.sin(angle_radians) * (x - cx) + math.cos(angle_radians) * (y - cy) + cy
    
    return new_x, new_y

# Coordenadas do ponto de rotação
cx = 2.0
cy = 3.0

# Coordenadas do objeto a ser rotacionado
x = 1.0
y = 2.0

# Ângulo de rotação em graus
angle_degrees = 45.0

# Realiza a rotação do objeto
new_x, new_y = rotate_point(x, y, cx, cy, angle_degrees)

# Exibe as coordenadas antes e depois da rotação
print(f'Coordenadas originais: ({x}, {y})')
print(f'Coordenadas após a rotação: ({new_x}, {new_y})')
