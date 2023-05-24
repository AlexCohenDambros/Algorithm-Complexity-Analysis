import sys
from quick_sort_recursivo import quick_sort_recursivo_wapper
from quick_sort_random import quick_sort_recursivo_random_wapper
from merge_sort_interativo import Merge_Sort_interativo_wapper
from merge_sort_recursivo import merge_sort__recursivo_wapper
from merge_sort_recursivo_random import merge_sort_recursivo_random_wapper
from select_sort_recursivo import select_sort_recursivo_wapper
from select_sort_recursivo_random import select_sort_recursivo_random_wapper
from sellSort_base_line import shellSort_Wapper
from gerador import gerar_dados_crescente
from gerador import gerar_dados_random
from gerador import gerar_dados_decrescente
from gerador import agora
from gerador import dif_time
from insertion_sort_interativo import insertion_sort_interativo
from insertion_sort_recursivo import wrapper
import openpyxl


def execucao(X, i):
    D = []
    D.append(len(X))

    a = agora()
    QS1 = quick_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    QS2 = quick_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    MS1 = Merge_Sort_interativo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    MS2 = merge_sort__recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    MS3 = merge_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    SS1 = select_sort_recursivo_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    SS2 = select_sort_recursivo_random_wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    BASE_LINE = shellSort_Wapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    IS1 = insertion_sort_interativo(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    a = agora()
    IS2 = wrapper(X.copy())
    b = agora()
    D.append(dif_time(b, a))

    return D


limite = sys.getrecursionlimit()
# print('Limite de memória: ', limite)
sys.setrecursionlimit(100000)
limite = sys.getrecursionlimit()
# print('Limite de memória: ', limite)

T = 250
N = 7
L = []

for i in range(1, N+1, 1):
    # print('O tamanho do problema',i, ' é ', i *T)
    X = gerar_dados_crescente(i * T)
    L.append(execucao(X, i))

print('N,QS1,QS2,MS1,MS2,MS3,SS1,SS2,BASE_LINE,IS1,IS2')
for x in L:
    c = len(x) - 1
    i = 0
    for y in x:
        if (i < c):
            print(y, end=',')
        else:
            print(y, end='')
        i += 1
    print()

# Criar um novo arquivo XLSX
workbook = openpyxl.Workbook()
sheet = workbook.active

# Escrever os dados na planilha
header = ['N', 'QS1', 'QS2', 'MS1', 'MS2', 'MS3',
          'SS1', 'SS2', 'BASE_LINE', 'IS1', 'IS2']
sheet.append(header)

for row in L:
    sheet.append(row)

# Salvar o arquivo XLSX
workbook.save('resultado.xlsx')
