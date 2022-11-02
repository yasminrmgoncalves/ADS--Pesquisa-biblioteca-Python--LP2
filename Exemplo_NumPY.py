#Importando a biblioteca numpy
import numpy as np
my_array=[1,2,3,4,5]
a=np.array(my_array)

#COMANDOS BÁSICOS NUMPY

#Imprime a forma do array
print(a.shape)
print("\n")
#Redimenciona a array
a=np.arange(6).reshape((3,2))
print(a)
print("\n")

#Imprime a versão do numpy
print(np.__version__)
print("\n")

#Cria uma Array NumPy vazia
x = np.empty([3,2], dtype = int) 
print(x)
print("\n")

#Cria um array de zeros
my_new_array = np.zeros((5)) 
print(my_new_array)
print("\n")

#Cria um array com valores aleatorios
my_random_array = np.random.random((5)) 
print(my_random_array)
print("\n")

#Array com número aleatorio entre 0 e 10
a2 = np.floor(10*np.random.random((3,4))) 
print(a2)
print("\n")

#Fazendo calculos matemáticos
a = np.array([[1.0, 2.0], [3.0, 4.0]])
b = np.array([[5.0, 6.0], [7.0, 8.0]])
sum = a + b # Soma
difference = a - b # Subtração
product = a * b # Multiplicação
quotient = a / b # Divisão
print('Sum = \n', + sum)
print('\n')
print('Difference = \n', + difference)
print('\n')
print('Product = \n', + product)
print('\n')
print('Quotient = \n', + quotient)
print("\n")

#Multiplicação de arrays
matrix_product = a.dot(b) 
 
print('Matrix Product = \n', + matrix_product)
