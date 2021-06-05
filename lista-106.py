# 1) Implemente o metodo define_default_city de acordo com a docstring definida
# no inicio da funcao. Utilize a clausula else no loop implementado.

# 2) Remova do arquivo capitais-BR.csv todas capitais dos estados do sudeste
# e teste se sua funcao estah robusta o suficiente. Ela deve executar sem erro
# mesmo que alguns dados estejam faltando.

with open("capitais-BR.csv", "r") as f:
    linhas = f.readlines()
with open("capitais-BR.csv", "w") as f:
    for linha in linhas:
        if linha.strip("\n") != "Minas Gerais;Belo Horizonte":
            f.write(linha)
with open("capitais-BR.csv", "w") as f:
    for linha in linhas:
        if linha.strip("\n") != "São Paulo;São Paulo":
            f.write(linha)
with open("capitais-BR.csv", "w") as f:
    for linha in linhas:
        if linha.strip("\n") != "Espírito Santo;Vitória":
            f.write(linha)
with open("capitais-BR.csv", "w") as f:
    for linha in linhas:
        if linha.strip("\n") != "Rio de Janeiro;Rio de Janeiro":
            f.write(linha)
print(linhas)

# 3) Faca uma funcao que le o arquivo lista-cpf.txt, retorne a quantidade de
#CPF unicos (sem repeticao) e os escreva em um arquivo lista-cpf-unicos.txt.
#Eh necessario descompactar o arquivo lista-cpf.txt.tar.gz primeiro. O
#algoritmo precisa ser eficiente, nesse caso especifico a melhor a melhor
#complexidade que pode ser acancada é linear. Algoritmos de complexidade
#quadratica, cubica, fatorial, etc. não sao considerados como eficientes
#pois a complexidade linear eh garantida. Como regra geral, se seu algoritmo
#demorar mais do que alguns segundos, ele, provavelmente, nao eh linear.

import tarfile

t = tarfile.open("lista-cpf.txt.tar.gz")
t.extractall()

with open("lista-cpf.txt", "r") as f:
    linhas = f.readlines()
    count = 0
print(linhas)
