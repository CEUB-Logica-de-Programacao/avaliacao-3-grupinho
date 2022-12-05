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
    senha2 = {}
    x = 0
    y = 0
    for n in range(0,len(s)):
        if s[n] in dict == False:
            dict[s[n]] = 0
        else:
            dict[s[n]] = valor(s[n]) +1
    for n in dict.keys():
        if valor(s[n]) > x:
            x = valor(s[n])
            xn = n
    x -=1
    senha2 = s
    senha2[xn] = x
    for i in range(0, len(dict)):
        if valor(s[i]) == valor(s[len(dict)]) or valor(senha2) == valor(senha2[len(dict)]:
            y = 1
    if y = 1:
        return True
    else:
        return False
    def valor(nome):
        for k, v in dict.items():
             if nome == k:
                 return v
        

if __name__ == '__main__':
    print(q5('abcc'))
