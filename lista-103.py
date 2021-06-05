###
# Exercicios
###

book1 = 'Homo Deus by Yuval Noah Harari, 2015'
book2 = 'Antifragile by Nassim Nicholas Taleb, 2012'
book3 = 'Fooled by Randomness by Nassim Nicholas Taleb, 2001'

# 1) Extraia o titulo do livro da string

print(book1.split(' by')[0])
print(book2.split(' by')[0])
print(book3.split(' by N')[0])

# 2) Salve o titulo de cada livro em uma variável

title1 = book1.split(' by')[0]
title2 = book2.split(' by')[0]
title3 = book3.split(' by N')[0]

print(f'{title1} , {title2} , {title3}')

# 3) Quantos caracteres cada título tem?

print(len(title1))
print(len(title2))
print(len(title3))

# 4) Imprima com a formatacao: {Titulo} - {Autor}, {Ano}

autor1 = ' '.join(book1.split(" ")[3:6])
autor2 = ' '.join(book2.split(" ")[2:5])
autor3 = ' '.join(book3.split(" ")[4:7])

age1 = book1.split(",")[1]
age2 = book2.split(",")[1]
age3 = book3.split(",")[1]

print(f' {title1} - {autor1} {age1}')
print(f' {title2} - {autor2} {age2}')
print(f' {title3} - {autor3} {age3}')

# 5) Verifique se uma palavra é uma palindrome perfeita.
# Palindrome perfeito sao palavras que ao serem escritas em ordem reversa,
# resultam na mesma palavra.
# Ignore espacos e caixa alta

palindrome_one = 'ovo'
palindrome_two = 'Natan'
palindrome_three = 'luz azul'
palindrome_four = 'caneta azul'

if palindrome_one == palindrome_one[::-1]:
	print(f'a palavra {palindrome_one} eh um palindrome')
else:
	print(f'a palavra {palindrome_one} nao eh um palindrome')

if palindrome_two == palindrome_two[::-1]:
	print(f'a palavra {palindrome_two} eh um palindrome')
else:
	print(f'a palavra {palindrome_two} nao eh um palindrome')	

if palindrome_three == palindrome_three[::-1]:
	print(f'a palavra {palindrome_three} eh um palindrome')
else:
	print(f'a palavra {palindrome_three} nao eh um palindrome')

if palindrome_four == palindrome_four[::-1]:
	print(f'a palavra {palindrome_four} eh um palindrome')
else:
	print(f'a palavra {palindrome_four} nao eh um palindrome')
