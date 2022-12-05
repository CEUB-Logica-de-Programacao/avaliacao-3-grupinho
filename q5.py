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
            caracteres = []
    for i in s:
        caracteres.append(i)
    
    caracteres2 = list(set(caracteres))
    frequencia = []
    
    for j in caracteres2:
        frequencia.append(caracteres.count(j))
        
    if len(list(set(frequencia))) == 1:
        return True
    
    else:
        caracteres3 = caracteres
        for k in caracteres2:
            caracteres3.remove(k)
            if len(list(set(caracteres3))) == 1:
                return True
        return False

if __name__ == '__main__':
    print(q5('abcc'))
