desk = []
Rlist = []
Blist = []

for i in range(8):
    temp = input()
    for j in range(8):
        if temp[j] == 'R':
            Rlist.append((i, j))
        elif temp[j] == 'B':
            Blist.append((i,j))
    desk.append(temp.replace(' ',''))

def beatR(desk, listFigure):
    if len(listFigure) == 0:
        return

    for F in listFigure:
        row = F[0]
        column = F[1]
        while row >= 0:
            row -= 1
            if row >= 0:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column+1:]
        row = F[0]
        while row < 8:
            row += 1
            if row < 8:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column + 1:]
        row = F[0]
        while column >= 0:
            column -= 1
            if column >= 0:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column + 1:]
        column = F[1]
        while column < 8:
            column += 1
            if column < 8:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column + 1:]

def beatB(desk, listFigure):
    for F in listFigure:
        row = F[0]
        column = F[1]
        while row >= 0 and column >= 0:
            row -= 1
            column -= 1
            if row >= 0 and column >= 0:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column + 1:]
        row = F[0]
        column = F[1]
        while row < 8 and column >=0:
            row += 1
            column -= 1
            if row < 8 and column >= 0:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column + 1:]
        row = F[0]
        column = F[1]
        while row >= 0 and column < 8:
            row -= 1
            column += 1
            if row >= 0 and column < 8:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column + 1:]
        row = F[0]
        column = F[1]
        while row < 8 and column < 8:
            row += 1
            column += 1
            if row < 8 and column < 8:
                if desk[row][column] == 'R' or desk[row][column] == 'B':
                    break
                desk[row] = desk[row][:column] + '.' + desk[row][column + 1:]
beatR(desk, Rlist)
beatB(desk, Blist)
result = 0
for i in range(8):
    for j in range(8):
        if desk[i][j] == '*':
            result += 1
print(result)

