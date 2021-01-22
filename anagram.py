
# def search_anagram(items):
#
#     for index, item in enumerate(items):
#
#         if index < len(items) - 1:
#             index_n = index + 1
#             current = item
#             next = items[index_n]
#
#             if(sorted(current) == sorted(next)):
#                 del items[index_n]
#
#     return items
#
#
# if __name__ == '__main__':
#     result = search_anagram(['casa', 'saca', 'paulo', 'oluap', 'morena'])
#     print(result)


#############################################################################
# def find_anagrams(s, p):
#     blocks = ""
#     longest_word = ""
#     # last_longest_word = ""
#
#     for i in range(len(s)):
#         if s[i] in blocks:
#             if len(blocks) > len(longest_word):
#                 longest_word = blocks
#
#             # get position of the last repeated letter
#             pos = blocks.find(s[i])
#
#             # update the block with the sequence of non-repeated letters
#             blocks = blocks[pos+1:] + s[i]
#             continue
#
#         blocks += s[i]
#         # last_longest_word = blocks
#
#     if len(blocks) > len(longest_word):
#         return blocks
#     return longest_word
#
#
# if __name__ == '__main__':
#     result = length_of_longest_substring("anviaj")
#     print("The longest word is >>", result, "<< and the size is >>", len(result), "<<")

#####################################################################
"""
Descobrir se a string B string esta contida dentro da string A
"""

#
# def gerar_dicionario():
#     alfabeto = "abcdefghijlmnopqrstuvxyz"
#
#     mapper = dict.fromkeys(list(alfabeto), 0)
#     return mapper


def mapeamento_dicionario(a, alfabeto):

    mapper = dict.fromkeys(list(alfabeto), 0)

    # Adiciona +1 nas de mapper contidas em a
    for l in a:
        mapper[l] += 1

    return mapper


def esta_contido(str1, str2):
    alfabeto = "abcdefghijlmnopqrstuvxyz"

    mapper1 = mapeamento_dicionario(str1, alfabeto)
    mapper2 = mapeamento_dicionario(str2, alfabeto)

    quants_negativos_tem = 0

    for l in alfabeto:
        if mapper1[l] - mapper2[l] < 0:
            quants_negativos_tem += 1
            print("nao esta contido")

    print("a quantidade de negativos é: ", quants_negativos_tem)


# result = esta_contido("abcdefghijyz", "abcdlep")

###################################################################

"""
Recebe uma solicitacao de pontos, um calculador de distancia e uma variavel pra percorrer a lista.
"""
anagrams = ["abc", "abcd", "cba", "efg", "abcd"]


# def is_anagram(a, b):
#     if a == b:
#         print("nao sao anagramas, sao iguais: ", a, b)
#         return False
#     temp = []
#     if sorted(a) == sorted(b):
#         for l in a:
#             temp[:-1] = l
#
#     # return sorted(a) == sorted(b)
#
#
# def percorredor_de_lista(anagrams):
#     i = 0
#     j = i + 1
#
#     quantidade_anagramas = 0
#
#     for i in range(len(anagrams)):
#         for j in range(len(anagrams)):
#             if is_anagram(anagrams[i], anagrams[j]):
#                 print("é anagram: ", anagrams[i], anagrams[j])
#                 quantidade_anagramas += 1
#             j = i + 1
#
#     print("A quantidade de anagramas nesta lista é: ", quantidade_anagramas)
#
#
# result = percorredor_de_lista(anagrams)
# print(result)

























def mapeamento_dicionario(s):
    tamanho_da_string = len(s)
    mapper = dict()  # cria um dicionario de mapeamento das substrings

    # faz o loop no tamanho total da string
    for i in range(tamanho_da_string):
        substring = ''
        for j in range(i, tamanho_da_string):
            substring = ''.join(sorted(substring + s[j]))

            # Insere a substring no mapper
            mapper[substring] = mapper.get(substring, 0)

            # Aumenta o contador da substring correspondente
            mapper[substring] += 1
    ## Até aqui eu montei o dicionario mapeado com todas as substrings, proximo passo e percorrer
    ## e verificar quais pares sao anagramas

    return mapper


def numero_total_de_anagramas(s):

    # Recebe um dicionario mapeado com as substrings
    mapper = mapeamento_dicionario(s)
    print(mapper)

    # Variavel para contar o numero de anagramas
    num_anagramas = 0

    # Retorna o total de numeros de anagramas
    for k, v in mapper.items():

        # Aqui eu faço a multiplicao do valor pelo valor -1, dividindo o resultado por 2 por ser pares e
        # adiciono o resultado ao num_anagramas
        num_anagramas += (v * (v - 1)) // 2
    return num_anagramas


s = "ABBA"
print(numero_total_de_anagramas(s))

# This code is contributed by fgaim




























# python code to demonstrate working of reduce()

# importing functools for reduce()
# import functools
#
# # initializing list
# lis = [1, 3, 5, 6, 2, ]
#
# # using reduce to compute sum of list
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a, b: a * b, lis))

# using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))