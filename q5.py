# ## Questão 5
#
# Sherlock considera uma string válida se todos os caracteres dela aparecerem o mesmo número de vezes.
# Também é válida se ele puder remover apenas um caractere, e os caracteres restantes aparecerem o
# mesmo número de vezes. Dada uma cadeia de caracteres, determine se ela é válida. Se for o caso, retorne `True`, caso
# contrário retorne `False`.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# aabbcd
# ```
#
# A saída deve ser:
#
# ```
# False
# ```
#
# Isso porque não é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para a entrada:
#
# ```
# abcc
# ```
#
# A saída deve ser:
#
# ```
# True
# ```
#
# Isso porque é possível remover apenas um caractere para tornar a string válida.
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q5(s):
        dict = {}
        y = 0
        def aab():
            for n in range(0,len(senha)):
                if tem(senha[n]) == False:
                    dict[senha[n]] = 0
                else:
                    dict[senha[n]] = valor(senha[n]) +1
            for i in range(0, len(dict)):
                if valor(senha[i]) != valor(senha[len(dict)]) or bbb() = True:
                    return False
            return True
        def tem(aa):
            for k in dict.keys():
                if aa == k:
                    return True
            return False
        def valor(nome):
            for k, v in dict.items():
                 if nome == k:
                     return v
        def bbb():
            for i in dict(0, len(dict)):
                    if y < valor(senha[i]):
                        y = valor(senha[i])
                        yn = i
                valor(senha[i]) -= 1
            for i in range(0, len(dict))
            if valor(senha[i]) != valor(senha[len(dict)]):
                return False
            return True
    return aab()



if __name__ == '__main__':
    print(q5('abcc'))
