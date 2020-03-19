import re
#test = "x + 4x + 5 + 3x + 2x + 5x - x - 6x - 7x - 8 = 2x - 1"
#test = "5x = 8"
#test = "x + 3x = 4 + 4"

def createList(splitPart):
    for term in splitPart:
        if term == "":
            splitPart.remove(term)

    for i in range(len(splitPart)):
        if splitPart[i] == "x":
            splitPart[i] = "1x"    

    #if the first term is not already preceded by a plus or minus it is automatically a positive term
    newList = []
    if not splitPart[0] in ["+","-"]:
        newList = [[splitPart[0], "+"]]

    #adds each term to newList and appends the operator preceding the term
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

def calcTotalX(terms, operator):
    total = 0
    print(terms)
    for term in terms:
        if term.find("x") > -1:
            xterm = term.replace("x", "")
            if operator == "+":
                total += int(xterm)
            elif operator == "-":
                total -= int(xterm)
        elif operator == "+":
            total += int(term)
        elif operator == "-":
            total -= int(term)
    print(total)
    return total

def calcMultiply(toMultiply):
    multiList = []
    hasX = False
    if toMultiply.find("x") > -1:
        hasX = True
        toMultiply = toMultiply.replace("x", "")
    multiTerms = toMultiply.split(" ")
    if not multiTerms[multiTerms.index('*') + 1] in ['+','-']:
        multiTerms.insert((multiTerms.index('*')) + 1, '+')
    multiTerms.remove("*")
    multiList = createList(multiTerms)
    negatives = 0
    total = 1
    for term in multiList:
        total *= int(term[0])
        if term[1] == "-":
            negatives += 1
    if negatives%2 == 1:
        total = "- " + str(total)
    else:
        total = "+ " + str(total)
    if hasX:
        total = str(total) + "x"
    return total

#expression = input("Enter an equation:")
expression = '4x + 2x - 5x * 7 + 3 * - 2x = 8'
#expression = '4x + 2x + 5x * 7 + 3 * - 2 = 8'
pattern = '[0-9]*x[0-9]*'
numPat = '[0-9]+'
total = 0

multiplies = re.findall('[+-] [0-9a-z]+ \* [-]?[ ]?[0-9a-z]+', " ".join(expression.split("=")[0].split(" ")))

for i in range(len(multiplies)):
    replacement = calcMultiply(multiplies[i])
    expression = expression.replace(multiplies[i], replacement)

print(expression)

p1split = expression.split("=")[0].split(" ")
p2split = expression.split("=")[1].split(" ")

leftTerms = createList(p1split)
rightTerms = createList(p2split)    

seperatedLeft = populateLists(leftTerms)
seperatedRight = populateLists(rightTerms)

leftXPosi = calcTotalX(seperatedLeft[0], "+")
leftXNeg = calcTotalX(seperatedLeft[1], "-")
rightXPosi = calcTotalX(seperatedRight[0], "+")
rightXNeg = calcTotalX(seperatedRight[1], "-")

totalXL = (leftXPosi - rightXPosi) + (leftXNeg - rightXNeg)

leftNumPosi = calcTotalX(seperatedLeft[2], "+")
rightNumPosi = calcTotalX(seperatedRight[2], "+")
leftNumNeg = calcTotalX(seperatedLeft[3], "-")
rightNumNeg = calcTotalX(seperatedRight[3], "-")

totalNumR = (rightNumPosi - leftNumPosi) + (rightNumNeg - leftNumNeg)

xVal = totalNumR/totalXL

print("x = ", str(xVal))
