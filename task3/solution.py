strInFile = int(input())
spaceList = []
clickNumber = 0
for i in range(strInFile):
    spaceList.append(int(input()))

for i in spaceList:
    clickNumber += i // 4
    temp = i % 4
    if temp == 1:
        clickNumber += 1 # space
    elif temp == 3 or temp == 2:#tab + backspace or space+ space
        clickNumber += 2
print(clickNumber)
