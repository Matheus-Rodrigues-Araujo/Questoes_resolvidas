'''
    Academia Capgemini
    * Questão 3
    * Linguagem utilizada: Python 3.10.1
'''

'''
    É utilizada a biblioteca "collections", e a partir dela será importada a Classe 'Counter',
    em que recebe uma String e que retorna um dicionário, sendo as chaves as letras e, os valores a quantidade
    de vezes que uma letra se repetiu.
'''
from collections import Counter
'''     Parte 1     '''
def anagramas_Pares(palavra):
    # ==========================================================================
    letras_pares = []
    contador_pares = 0
    
    # É criada uma variável, que recebe a Classe Counter, e que depois passamos como parâmetro um valor(string),
    # que foi recolhido através do parâmetro da função subStrings
    c = Counter(palavra)
    # Aqui iremos utilizar um 'for' e um 'if' para ver se há alguma letra repetida no nosso dicionário criado
    # Se houver par de uma letra, a variável 'contador_pares' é somada. Ex: letra 'i' repetida duas vezes = 1 par
    for item in c.items():
        if item[1] == 2:
            contador_pares+=1
            # Colocamos em uma lista as letras que se repetiram
            # item[0] significa as chaves do dicionário, que no caso, são as letras
            # item[1] significa a quantidade de vezes que a letra se repetiu na palavra(string)
            letras_pares.append(item[0])

    all_substrings = []
    lista_ordenada = []

    # ==========================================================================
    
    '''Parte 2'''
    # Agora utilizaremos o 'for' duas vezes e o fatiamento de strings, para descobrirmos as substrings da string principal
    # Exemplo: palavra = 'lua'
    # palavra[0] = 'l'; palavra[0:2] = 'lu'; palavra[0:3] = 'lua',etc
    # Obs: O último valor é descartado -> 'lua' -> l:0| u: 1| a: 2-> palavra[0:2] = 'lu'
    for i in range(len(palavra)):
        for j in range(i+1, len(palavra)+1):
            # Aqui utilizaremos a lista 'all_substrings' e adicionaremos as substrings
            all_substrings.append(palavra[i:j])
    
    # ==========================================================================

    '''Parte 3'''
    # Na parte 3 iremos extrair as substrings em que estão presentes as letras que se repetiram duas vezes
    for j in all_substrings:
        for p in range(len(letras_pares)):
            # Abaixo utiliza-se um 'if' para recolher apenas as substrings em que as letras repetidas estão presentes e que ainda não estão
            # na lista 'lista_ordenada', para evitar repetição
            if letras_pares[p] in j and not j in lista_ordenada:
                lista_ordenada.append(j)
    
    # ==========================================================================
    '''Parte 4'''
    # Parte 4
    # É criada a lista 'lista_set', que irá armazenar as substrings sem nenhuma letra repetida
    lista_set = []
    #  Para cada substring em lista_ordenada, se o tamnho de uma substring original for igual ao tamanho da 
    #  substring que usa o método set, que retira as letras repetidas, significa que pode ser adicionada na 'lista_set'
    for values in lista_ordenada:
        if len(values) == len(set(values)):
            # Nesse comando os elementos são adicionados e ordenados ao mesmo tempo com o método sorted().
            # São ordenados porque precisamos detectar um par de anagramas, e só descobrimos os pares se cada par estiver com as
            # letras em ordem alfabetica, tiverem o mesmo tamanho e terem as letras iguais.
            lista_set.append(sorted(values))
    # ==========================================================================
    '''Parte 5''' 
    # Na parte 5, verificaremos se há elemetos iguais(pares), e se tiver, colocamos a variavel 'contador_pares' para somar mais 1,
    # ou seja, mais um anagrama para foi descoberto!.
    for element in lista_set:
        if lista_set.count(element) > 1:
            contador_pares+=1
            break
    # Finalmente, retornamos o total de pares achados retornando o valor de 'contador_pares'
    return contador_pares
    # ==========================================================================

# Execução do código
# Abaixo estão as palavras que foram utilizadas nos exemplos da Questão 3
# Basta retirar '#' da linha e o código será executado

a = anagramas_Pares('ifailuhkqq')
print(a)

# b = anagramas_Pares('ovo')
#print(b)