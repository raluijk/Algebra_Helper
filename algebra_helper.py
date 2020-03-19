import re
#test = "x + 4x + 5 + 3x + 2x + 5x - x - 6x - 7x - 8 = 2x - 1"
#test = "5x = 8"
#test = "x + 3x = 4 + 4"

def createList(splitPart):
    for i in range(len(splitPart) - 1):
        if splitPart[i] == "x":
            splitPart[i] = "1x"

    for term in splitPart:
        if term == "":
            splitPart.remove(term)

    newList = [[splitPart[0], "+"]]

    count = 0
    for term in splitPart:
        if count > 0 and not term in ["+","-"]:
            newList.append([term, splitPart[count - 1]])
        count += 1
    return newList

def populateLists(termSide):
    pList = []
    mList = []
    pNumList = []
    mNumList = []
    for term in termSide:
        if term[0].find("x") > -1:
            if term[1] == "+":
                pList.append(term[0])
            elif term[1] == "-":
                mList.append(term[0])
        elif term[1] == "+":
            pNumList.append(term[0])
        elif term[1] == "-":
            mNumList.append(term[0])
    return pList, mList, pNumList, mNumList

def calcTotalX(terms, operand):
    total = 0
    for term in terms:
        if term.find("x") > -1:
            xterm = term.replace("x", "")
            if operand == "+":
                total += int(xterm)
            else:
                total -= int(xterm)
        elif operand == "+":
            total += int(term)
        else:
            total -= int(term)
    return total

def findx():
    expression = input("Enter an equation:")
    pattern = '[0-9]*x[0-9]*'
    numPat = '[0-9]+'
    total = 0

    p1split = expression.split("=")[0].split(" ")
    p2split = expression.split("=")[1].split(" ")

    leftTerms = createList(p1split)
    rightTerms = createList(p2split)    

    seperatedLeft = populateLists(leftTerms)
    seperatedRight = populateLists(rightTerms)

    leftXPosi = calcTotalX(seperatedLeft[0], "+")
    rightXPosi = calcTotalX(seperatedRight[0], "+")
    leftXNeg = calcTotalX(seperatedLeft[1], "-")
    rightXNeg = calcTotalX(seperatedRight[1], "-")

    totalXL = (leftXPosi - rightXPosi) + (leftXNeg - rightXNeg)

    leftNumPosi = calcTotalX(seperatedLeft[2], "+")
    rightNumPosi = calcTotalX(seperatedRight[2], "+")
    leftNumNeg = calcTotalX(seperatedLeft[3], "-")
    rightNumNeg = calcTotalX(seperatedRight[3], "-")

    totalNumR = (rightNumPosi - leftNumPosi) + (rightNumNeg - leftNumNeg)

    xVal = totalNumR/totalXL

    print("x = ", str(xVal))

findx()
