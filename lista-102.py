#########
# Exercicios - Listas
# Faca sem usar loops
#########

weekdays = ['mon','tues','wed','thurs','fri']
days_list = ['mon','tues','wed','thurs','fri','sat','sun']
lista = ['a', 1, 3.14159265359]

# Como selecionar 'wed' pelo indice?
wed = weekdays[2]
print(wed)
# Como verificar o tipo de 'mon'?
print(type(weekdays[0]))
# Como separar 'wed' até 'fri'?
days = weekdays[2:-1]
print(days)
# Quais as maneiras de selecionar 'fri' por indice?
print(weekdays[4])
print(weekdays[-1])
# Qual eh o tamanho dos dias e days_list?
print(len(weekdays))
print(len(days_list))
# Como inverter a ordem dos dias?
print(weekdays[4::-1])
# Como inserir a palavra 'zero' entre 'a' e 1 de list?
lista.insert(1,'zero')
print(lista)
# Como limpar list?
lista.clear()
print(lista)
# Como deletar list?
del lista
# Como atribuir o ultimo elemento de list na variavel ultimo_elemento e remove-lo de list?
ultimo_elemento = weekdays.pop()
print(weekdays)
print(ultimo_elemento)
