from math import sqrt

def goToSpace(toSpaced, nb):
    nbSpaces = int(sqrt((len(toSpaced[0])-len(toSpaced[1]))**2))
    strSpaces = ""
    for _ in range(nbSpaces):
        strSpaces+=" "
    if nb:
        toSpaced[0] = strSpaces+toSpaced[0]
        return toSpaced[0]
    else:
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
        op[0] = goToSpace(op, True)
        strSep = getSep(op, False)
        answer = rsltFormat(answer, op)
        formatter = formatted(op, strSep, answer, answers)
    elif len(op[0]) > len(op[1]):
        op[0] = "  "+op[0]
        op[1] = goToSpace(op, False)
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

def arithmetic(problems, answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    else:
        clc = []
        for pb in problems:
            if len(pb.split("+")) > 1:
                addition = pb.split("+")
                answer = str(int(addition[0])+int(addition[1]))
                clc.append(casesD(addition, "+", answer, answers))
            elif len(pb.split("-")) > 1:
                substraction = pb.split("-")
                answer = str(int(substraction[0])-int(substraction[1]))
                clc.append(casesD(substraction, "-", answer, answers))
            elif  len(pb.split("/")) > 1 or len(pb.split("*")) > 1:
                return "Error: Operator must be '+' or '-'."
        
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

print(arithmetic(["2000-20000", "20+2000", "2000-2000", "2000+20", "2000-2000"], True))