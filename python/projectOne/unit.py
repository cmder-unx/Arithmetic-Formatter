                if len(substraction[0]) < len(substraction[1]):
                    substraction[1] = "- "+substraction[1]
                    
                    nbSpaces = len(substraction[1])-len(substraction[0])
                    strSpaces = ""
                    for _ in range(nbSpaces):
                        strSpaces+=" "
                    substraction[0] = strSpaces+substraction[0]
                    
                    strSep = ""
                    for _ in range(len(substraction[1])):
                        strSep+="-"
                    
                    if len(answer) < len(substraction[1]):
                        nbSpacesA = len(substraction[1])-len(answer)
                        strSpacesA = ""
                        for _ in range(nbSpacesA):
                            strSpacesA+=" "
                        answer = strSpacesA+answer
                    
                    if answers:
                        formatter = f"{substraction[0]}\n{substraction[1]}\n{strSep}\n{answer}"
                    else:
                        formatter = f"{substraction[0]}\n{substraction[1]}\n{strSep}\n"
                    return formatter
                
                elif len(substraction[0]) > len(substraction[1]):
                    substraction[0] = "  "+substraction[0]
                    
                    nbSpaces = len(substraction[0])-len(substraction[1])
                    strSpaces = "-"
                    for _ in range(nbSpaces-1):
                        strSpaces+=" "
                    substraction[1] = strSpaces+substraction[1]
                    
                    strSep = ""
                    for _ in range(len(substraction[0])):
                        strSep+="-"
                    
                    if len(answer) < len(substraction[1]):
                        nbSpacesA = len(substraction[1])-len(answer)
                        strSpacesA = ""
                        for _ in range(nbSpacesA):
                            strSpacesA+=" "
                        answer = strSpacesA+answer
                    
                    if answers:
                        formatter = f"{substraction[0]}\n{substraction[1]}\n{strSep}\n{answer}"
                    else:
                        formatter = f"{substraction[0]}\n{substraction[1]}\n{strSep}\n"
                    return formatter
                
                elif len(substraction[0]) == len(substraction[1]):
                    substraction[0] = "  "+substraction[0]
                    substraction[1] = "- "+substraction[1]
                    
                    strSep = ""
                    for _ in range(len(substraction[0])):
                        strSep+="-"
                    
                    if len(answer) < len(substraction[1]):
                        nbSpacesA = len(substraction[1])-len(answer)
                        strSpacesA = ""
                        for _ in range(nbSpacesA):
                            strSpacesA+=" "
                        answer = strSpacesA+answer
                    
                    if answers:
                        formatter = f"{substraction[0]}\n{substraction[1]}\n{strSep}\n{answer}"
                    else:
                        formatter = f"{substraction[0]}\n{substraction[1]}\n{strSep}\n"
                    return formatter