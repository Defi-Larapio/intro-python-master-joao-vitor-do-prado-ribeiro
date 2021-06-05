###
# Exercicios
###

## Usando a lista: ['a','b','c']
# 1) Faca um loop dentro de uma funcao que irah retornar: ['A','B','C']

lista = ['a','b','c']

for i in range(len(lista)):
	lista[i] = lista[i].upper()
	
print(lista)

## Usando a lista: [0, 1, 7, 4, 5]
# 2) Faca um loop dentro de uma funcao para retornar a soma de todos os elementos da listas. A funcao deve receber a lista como parametro.

lista = [0, 1, 7, 4, 5]

def function1(lista):
	soma  = 0
	for i in range(len(lista)):
		soma += lista[i]
	return soma

print(function1(lista))

# 3) Crie uma funcao que receba uma lista e retorne outra lista composta pelos os numeros impares da lista recebida

def function2(list):
	return_list = []
	for i in range(len(list)):
		if list[i]%2 == 1:
			return_list.append(list[i])
	return return_list

print(function2(lista))

## usando a string: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
# 4) Conte quantas palavras de tamanho >= 5 existe nessa string. Faca uma vez sem usar list comprehension e depois usando list comprehension.

string = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
separate_string = string.split()
def function3(string):
	count = 0
	for i in range(len(separate_string)):
		if len(separate_string[i]) >= 5:
			count += 1
	return count

print(f'tem {function3(string)} palavras')

count_string = len([s for s in separate_string if len(s) >= 5])

print(f'(list comprehension) tem {count_string} palavras')


			
# 5) Usando list comprehension, crie uma lista com os multiplos de 3 de 0 ate 100

lista = range(100)

multiple = [i for i in lista if i%3==0]
print(multiple)

# 6) Faca uma funcao para encontrar os numeros primos no intervalo [2, 10), mas nao utilize a clausula else do for
        
lista = [2,3,4,5,6,7,8,9,10]

def function6(lista):
        count = 0
        for i in range(2,10):
                for j in range(2,10):
                        if i%j == 0:
                                count+=1
                        if i==j:
                                break
                if count==1:
                        print(f'{i} eh numero primo')
                count = 0;
                
function6(lista)

                
	
