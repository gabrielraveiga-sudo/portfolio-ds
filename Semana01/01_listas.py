#1
nomes = ["Ariquemes", "Cabixi", "Cacoal", "Cerejeiras", "Colorado do Oeste", "Corumbiara", "Costa Marques",
"Jaru", "Ji-Paraná", "Porto Velho"] #Como e uma lista estática, eu so preciso inicar a lista ja com cada elemento

populacoes = [109731, 5640, 98884, 16957, 16432, 7938, 13499, 55774, 140800, 520379] 
#Como e uma lista estática, eu so preciso inicar a lista ja com cada elemento

#2
print(f"1 elemento: {populacoes[0]} \n3 elemento: {populacoes[2]} \nUltimo elemento: {populacoes[-1]}") 
'''usando a funcao f-print para misturar texto com variaveis. O primeiro element
a contagem de elementos em uma lista comeca no 0, entao para acessar o primeiro basta usar o indice 0
entre colchetes colado com populacoes. Do mesmo jeito, para acessar o 3 elemento, eu preciso comecar contando
a partir do 0, assim parando no indice '2'. Agora se eu quiser acessar o ultimo elemento, basta usar o indice '-1' 
'''

#3
print(f"{populacoes[2:5]}") 
''' Como a contagem comeca em 0, o fatiamento conta a partir do 3 elemento representado pelo numero '2' 
e ira imprim-lo junto do 4 e 5 elemento com indices 3 e 4 respectivamente. O 6 elemento, de indice 5, ficara de
fora pois esse comando pega os elementos a partir do ponto de partido ate indice de parada menos 1'''

#4
print(f"Populacao Total: {sum(populacoes)} \nMedia: {sum(populacoes)/len(populacoes)}")
print(f"Maior Valor: {max(populacoes)} \nMenor Valor: {min(populacoes)}")
''' A funcao sum() retorna a soma de todos os elementos da lista, o que usei para encontrar a populacao total
das cidades selecionadas. A media, e calculada pela soma dos elementos divido pela numero de elementos, usando a
funcao sum() eu consegui a soma dos elemento e com len() consigro descobrir o tamanho da lista, ou seja, o
numero de elementos e como as duas funcoes retornam um numero, posso dividir sem problemas. Usei a funcao max()
que acha o maior valor de uma lista e min() para achar o menor valor de uma lista '''

#5
soma = 0
for i in range(len(populacoes)):
    soma += populacoes[i]
''' como por padrao a variavei contadora comeca em 0, eu nao preciso definir o ponto de partida e o ponto de
parada e o ponto definido menos 1, por isso usei a funcao len(). Isso significa que i vai de 0 ate len(populacoes)
-1 '''
print(f"Soma com sum(): {sum(populacoes)} \nSoma sem sum(): {soma}")

#6
for nmr, municipio in enumerate(nomes, start= 1):
    print(nmr, municipio)
''' Aprendi a usar enumerate, eu nao posso apenas escrever: print(enumerate(nomes,start= 1)). 
Emunerate devolve 2 valores, e eu estava armazenar em um so. Por isso criei uma seperacao, a variavel nmr
representa em qual posicao esta e municipio define a cidade respectiva. Coloquei para comecar enumerar a partir de 1 '''

#7
print(populacoes)
sorted(populacoes) #nao altera a lista original
print(populacoes) 
populacoes.sort() #altera a lista original
print(populacoes)
populacoes = populacoes.sort() #perde referencia, sort() retorna None
print(populacoes) #None

#8
print(populacoes[10]) 

''' Exception has occurred: TypeError
'NoneType' object is not subscriptable
  File "C:\Users\g           abri\Desktop\portfolio-ds\Semana01\01_listas.py", line 57, in <module>
    print(populacoes[10])
          ~~~~~~~~~~^^^^
TypeError: 'NoneType' object is not subscriptable
'''
''' Ao criar uma lista, e reservada um espaco na memoria para armazenar-la, ao acessarmos um indice que nao existe,
 estamos tentando acessar uma posicao que nao tem um endereco definido na memoria '''