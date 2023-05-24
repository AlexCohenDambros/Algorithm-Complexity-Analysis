import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.title("Desempenho de algoritmos de ordenação")
plt.xlabel("N (em centenas)")
plt.ylabel("t (em milisegundos)")
plt.legend()

data = pd.read_excel("resultado.xlsx")

X = data["N"]


def printCol(col):
    x1 = np.polyfit(X, data[col], 2)
    f1 = np.poly1d(x1)
    s1 = 'f1(x) = ' + \
        str(f1).split('\n')[1].replace(' x', 'x^2', 1).replace(' x', 'x', 1)
    print(s1)
    XX = X.copy()
    XX = pd.concat([XX, pd.Series(XX[XX.shape[0]-1]*2)])
    predict = list(map(f1, XX))
    plt.plot(X, data[col], "o-", label=col)
    plt.plot(XX, predict, "--", label=f"{col} {s1}")


BASE_LINE = "BASE_LINE"

columns = data.columns.to_list()[1:]
print(columns)
col = 0

printCol(columns[0])
printCol(columns[1])
printCol(BASE_LINE)
plt.legend(loc='upper left')
plt.show()

printCol(columns[2])
printCol(columns[3])
printCol(columns[4])
printCol(BASE_LINE)
plt.legend(loc='upper left')
plt.show()

printCol(columns[5])
printCol(columns[6])
printCol(BASE_LINE)
plt.legend(loc='upper left')
plt.show()

printCol(columns[8])
printCol(columns[9])
printCol(BASE_LINE)
plt.legend(loc='upper left')
plt.show()

exit(0)