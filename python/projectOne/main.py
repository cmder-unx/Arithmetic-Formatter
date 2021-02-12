from math import sqrt
import re

"""
RULES :
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will **return** a **string** 
that describes an error that is meaningful to the user.  
* Situations that will return an error:
    ✅ * If there are **too many problems** supplied to the function. The limit is **five**, anything more will return:
    `Error: Too many problems.`
    ✅ * The appropriate operators the function will accept are **addition** and **subtraction**. 
    Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. 
    The error returned will be:
    `Error: Operator must be '+' or '-'.` 
    ✅ * Each number (operand) should only contain digits. Otherwise, the function will return:
    `Error: Numbers must only contain digits.`
    ✅ * Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be:
    `Error: Numbers cannot be more than four digits.`
*  If the user supplied the correct format of problems, the conversion you return will follow these rules:
    ✅ * There should be a single space between the operator and the longest of the two operands, the operator will be on the same line 
    as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom.
    ✅ * Numbers should be right-aligned.
    ✅ * There should be four spaces between each problem.
    ✅ * There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. 
    (The example above shows what this should look like.)
"""

def goToSpace(toSpaced, nb, sign):
    nbSpaces = int(sqrt((len(toSpaced[0])-len(toSpaced[1]))**2))
    if nb:
        strSpaces = ""
        for _ in range(nbSpaces):
            strSpaces+=" "
        toSpaced[0] = strSpaces+toSpaced[0]
        return toSpaced[0]
    else:
        strSpaces = "+" if sign == "+" else "-"
        for _ in range(nbSpaces-1):
            strSpaces+=" "
        toSpaced[1] = strSpaces+toSpaced[1]
        return toSpaced[1]

def getSep(toSep, op):
    strSep = ""
    for _ in range(len(toSep[0] if op else toSep[1])):
        strSep+="-"
    return strSep

def formatted(toFormat, strSep, answer, answers):
    if answers:
        formatter = f"{toFormat[0]}\n{toFormat[1]}\n{strSep}\n{answer}"
        return formatter
    else:
        formatter = f"{toFormat[0]}\n{toFormat[1]}\n{strSep}\n"
        return formatter

def rsltFormat(answer, op):
    if len(answer) < len(op[1]):
        nbSpacesA = len(op[1])-len(answer)
        strSpacesA = ""
        for _ in range(nbSpacesA):
            strSpacesA+=" "
        answer = strSpacesA+answer
        return answer
    else:
        return answer

def casesD(op, sign, answer, answers):
    if len(op[0]) < len(op[1]):
        op[1] = "+ "+op[1] if sign == "+" else "- "+op[1]
        op[0] = goToSpace(op, True, sign)
        strSep = getSep(op, False)
        answer = rsltFormat(answer, op)
        formatter = formatted(op, strSep, answer, answers)
    elif len(op[0]) > len(op[1]):
        op[0] = "  "+op[0]
        op[1] = goToSpace(op, False, sign)
        strSep = getSep(op, True)
        answer = rsltFormat(answer, op)
        formatter = formatted(op, strSep, answer, answers)
    elif len(op[0]) == len(op[1]):
        op[0] = "  "+op[0]
        op[1] = "+ "+op[1] if sign == "+" else "- "+op[1]
        strSep = getSep(op, True)
        answer = rsltFormat(answer, op)
        formatter = formatted(op, strSep, answer, answers)
    return formatter

def arithmetic_arranger(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        clc = []
        for pb in problems:
            if bool(re.search("[a-zA-Z]", pb)) == False:
                if len(pb.split("+")) > 1:
                    addition = pb.split("+")
                    additionZ = addition[0].split(" ")
                    additionU = addition[1].split(" ")
                    addition[0] = additionZ[0] if len(additionZ[0]) > 0 else additionZ[1]
                    addition[1] = additionU[0] if len(additionU[0]) > 0 else additionU[1]
                    if len(addition[0]) <= 4 and len(addition[1]) <= 4:
                        answer = str(int(addition[0])+int(addition[1]))
                        clc.append(casesD(addition, "+", answer, answers))
                    elif len(addition[0]) >= 5 or len(addition[1]) >= 5:
                        return "Error: Numbers cannot be more than four digits."
                elif len(pb.split("-")) > 1:
                    substraction = pb.split("-")
                    substractionZ = substraction[0].split(" ")
                    substractionU = substraction[1].split(" ")
                    substraction[0] = substractionZ[0] if len(substractionZ[0]) > 0 else substractionZ[1]
                    substraction[1] = substractionU[0] if len(substractionU[0]) > 0 else substractionU[1]
                    if len(substraction[0]) <= 4 and len(substraction[1]) <= 4:
                        answer = str(int(substraction[0])-int(substraction[1]))
                        clc.append(casesD(substraction, "-", answer, answers))
                    elif len(substraction[0]) >= 5 or len(substraction[1]) >= 5:
                        return "Error: Numbers cannot be more than four digits."
                elif  len(pb.split("/")) > 1 or len(pb.split("*")) > 1:
                    return "Error: Operator must be '+' or '-'."
            else:
                return "Error: Numbers must only contain digits."
        allClcStr = ""
        top = []
        bot = []
        sep = []
        rslt = []
        btwClc = "    "
        for c in clc:
            csplit = c.split("\n")
            top.append(csplit[0]+btwClc)
            bot.append(csplit[1]+btwClc)
            sep.append(csplit[2]+btwClc)
            rslt.append(csplit[3]+btwClc)
        top[-1]+="\n"
        bot[-1]+="\n"
        sep[-1]+="\n"
        rslt[-1]+="\n"
        for t in top:
            allClcStr+=t
        for b in bot:
            allClcStr+=b
        for s in sep:
            allClcStr+=s
        for r in rslt:
            allClcStr+=r
        return allClcStr

print(arithmetic_arranger(["2000-200", "2000 + 2000", "20-2000", "20+2000", "2000 + 20"], True))