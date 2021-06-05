###
# Exercicio
###

# 1) Imprima os metodos disponiveis para uma lista e para uma tupla

print(f'{dir(list)} \n\n{dir(tuple)} \n')

# 2) Faca um metodo para retornar apenas as diferencas entre as duas de metodos

lista_list = dir(list)
lista_tuple = dir(tuple)
    
lista_diferenca_list = [s for s in lista_list if s not in lista_tuple]
lista_diferenca_tuple = [s for s in lista_tuple if s not in lista_list]
print(f'diferencas de metodos da lista com a tupla: \n{lista_diferenca_list} \n')
print(f'diferencas de metodos da tupla com a lista: \n{lista_diferenca_tuple}')
  
# 3) Adicione as coordenadas (latitude, longitude) para os dicts professor1, professor2 e professor3. Copie os dicts do arquivo 106.py. As coordenadas precisam ser inseparaveis e imutaveis.
professor1 = {'id': 42, 'name': 'Alexandre Abreu', 'age': 30, 'state_origin': 'Minas Gerais', 'courses': ['Inteligência Artificial', 'Mineração de Dados', 'Programação para Internet I', 'Programação para Internet II']}
professor1 ['latitude_longitude'] = [['14º,13\',58\"'],['39º,51\',32\"']]
print(professor1['latitude_longitude'])

professor2 = {'id': 37, 'name': 'Denilson Barbosa', 'age': 40, 'state_origin': 'Paraná', 'courses': ['Inteligência Artificial', 'Banco de Dados I', 'Banco de Dados II', 'Programação para Internet I']}
professor2 ['latitude_longitude'] = [['22º ,30\', 58\"'],['48º,05\',37\"']]
print(professor2['latitude_longitude'])

professor3 = dict(id=28, name='Jorge Armino', idade=37, state_origin='Rio Grande do Sul', courses=['Filosofia', 'Informática e Sociedade'])
professor3 ['latitude_longitude'] = [['32º,02\',06\"'],['52º,05\',55\"']]
print(professor3['latitude_longitude'])
