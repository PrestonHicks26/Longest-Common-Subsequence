def LCS_Length(x, y):
    m = len(x)
    n = len(y)
    numberTable = []
    symbolTable = []
    for i in range(m):
        numberTable.append([])
        symbolTable.append([])
        for j in range(n):
            numberTable[i].append(0)
            symbolTable[i].append(0)
    for i in range(1,m):
        for j in range(1,n):
            if x[i] == y[j]:
                numberTable[i][j] = numberTable[i-1][j-1] + 1
                symbolTable[i][j] = "d"
            elif numberTable[i-1][j] >= numberTable[i][j-1]:
                numberTable[i][j] = numberTable[i-1][j]
                symbolTable[i][j] = "u"
            else:
                numberTable[i][j] = numberTable[i][j-1]
                symbolTable[i][j] = "l"
    return {"numbers": numberTable, "symbols": symbolTable}

def Print_LCS(symbolTable, x, i, j):
    if i == 0 or j == 0:
        return
    if symbolTable[i][j] == "d":
        Print_LCS(symbolTable, x, i-1, j-1)
        print(x[i])
    elif symbolTable[i][j] == "u":
        Print_LCS(symbolTable, x, i-1, j)
    else:
        Print_LCS(symbolTable, x, i, j-1)

#test LCS methods
str1 = "10010101"
str2 = "010110110"
string1 = ['xi']
string2 = ['yj']
for i in str1:
    string1.append(i)
for i in str2:
    string2.append(i)

#test length method
tables = LCS_Length(string1, string2)
print("Number Table")
for i in tables["numbers"]:
    print(str(i)+"\n")
print(("Symbol Table"))
for i in tables["symbols"]:
    print(str(i) + "\n")

#test print method
Print_LCS(tables["symbols"], string1, len(string1)-1, len(string2)-1)
