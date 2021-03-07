def add_time(start_time, duration, starting_day=""):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
    #INPUTS TREATMENT
    start_time, duration, starting_day = str(start_time), str(duration), str(starting_day.lower())
    
    #START TIME TREATMENT
    start_time_split = start_time.split(":")
    start_time_split2 = start_time_split[1].split(" ")
    hour, minutes, ending = int(start_time_split[0]), int(start_time_split2[0]), start_time_split2[1]
    
    #DURATION TREATMENT
    duration_split = duration.split(":")
    dHours, dMinutes = int(duration_split[0]), int(duration_split[1])
    
    rsltH = hour+dHours
    if minutes < 60 and dMinutes < 60:
        rsltM = minutes+dMinutes
    else:
        return "Error, minutes must be less than 60"
    
    if ending.lower() == "am":
        nbDays = 0
        if rsltM < 60:
            if rsltH <= 12:
                ending = "am"
            elif rsltH > 12:
                while rsltH > 24:
                    rsltH-=24
                    nbDays+=1
                if rsltH <= 12:
                    ending = "am"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "pm"
        if rsltM > 59:
            rsltM-=60
            rsltH+=1
            if rsltH <= 12:
                ending = "am"
            elif rsltH > 12:
                while rsltH > 24:
                    rsltH-=24
                    nbDays+=1
                if rsltH <= 12:
                    ending = "am"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "pm"
        rsltH = "0"+str(rsltH) if len(str(rsltH)) < 2 else str(rsltH)
        nxtD = " (next day)" if nbDays == 1 else ""
        display = rsltH+":"+str(rsltM)+" "+ending.upper()+nxtD
    elif ending.lower() == "pm":
        nbDays = 0
        if rsltM < 60:
            if rsltH <= 12:
                ending = "pm"
            elif rsltH > 12:
                while rsltH > 24:
                    rsltH-=24
                    nbDays+=1
                if rsltH <= 12:
                    ending = "pm"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "am"
        elif rsltM > 59:
            rsltM-=60
            rsltH+=1
            if rsltH <= 12:
                ending = "pm"
            elif rsltH > 12:
                while rsltH > 24:
                    rsltH-=24
                    nbDays+=1
                if rsltH <= 12:
                    ending = "pm"
                elif rsltH > 12:
                    rsltH-=12
                    ending = "am"
        rsltH = "0"+str(rsltH) if len(str(rsltH)) < 2 else str(rsltH)
        nxtD = " (next day)" if nbDays == 1 else ""
        display = rsltH+":"+str(rsltM)+" "+ending.upper()+nxtD
    else:
        return "Error, ending must be AM or PM."
    
    if starting_day:
        starting_day = starting_day.lower().capitalize()
        if starting_day in days:
            if not nxtD:
                if nbDays == 0:
                    starting_day = ", "+starting_day
                    display+=starting_day
                elif nbDays == 2:
                    strtD_index = days.index(starting_day)
                    nD_index = nbDays+strtD_index
                    if nD_index > 6:
                        nD_index-=7
                    tD_later = ", "+days[nD_index]+" "+"(2 days later)"
                    display+=tD_later
                elif nbDays > 2:
                    xD_later = " ("+str(nbDays)+" days later)"
                    display+=xD_later
                
        else:
            return "Error, your starting day isn't a valid day."
    
    return display

print(add_time("5:39 AM", "48:01", "saturday"))