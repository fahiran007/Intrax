from  datetime import time as timeMaker
Minutes = []
Timelist2 = []
def TimeConverter(startTime,minutes):
    global Minutes,Timelist2
    m = minutes
    stTimes = str(startTime)
    stminutes = int(stTimes[3:5])
    sthours = int(stTimes[0:2])
    hours = int(minutes/60)
    minutes = minutes%60
    minutes = stminutes+minutes
    hour2 = int(minutes/60)
    minutes = minutes%60
    stminutes = minutes
    hours += hour2
    sthours = sthours+hours
    if startTime == timeMaker(22,00):
        if sthours > 12:
            sthours = sthours-12
    Time = timeMaker(sthours,stminutes)
    Hour = int(m/60)
    mint = m%60
    Hour = str(Hour)+"."+str(mint)+"h"
    Minutes.append(Hour)
    return Time
def Timerule(collage,writting):
        if collage == 'no' and writting == "yes":   
            startTime = timeMaker(5,00)                             
            exerciseTime = TimeConverter(startTime, 20)
            freshingTime = TimeConverter(exerciseTime, 20)
            beats = TimeConverter(freshingTime, 10)
            comTime = TimeConverter(beats, 75)
            LearningTime = TimeConverter(comTime, 115)
            breakFast = TimeConverter(LearningTime, 10)
            restTime = TimeConverter(breakFast, 50)
            computer = TimeConverter(restTime, 180)
            LearningTime1 = TimeConverter(computer, 60)
            BLC = TimeConverter(LearningTime1, 40)
            RelaxingTime = TimeConverter(BLC, 60)
            computer1 = TimeConverter(RelaxingTime, 30)
            writtingTime = TimeConverter(computer1, 105)
            tuitionTime = TimeConverter(writtingTime, 115)
            readingTime = TimeConverter(tuitionTime, 100)
            dinnerTime = TimeConverter(readingTime, 10)
            RestTime = TimeConverter(dinnerTime, 20)
            sleepTime = TimeConverter(RestTime,420 ) 
            itemsList = [
            startTime,
            exerciseTime,
            freshingTime,
            beats,
            comTime,
            LearningTime,
            breakFast,
            restTime,
            computer,
            LearningTime1,
            BLC,
            RelaxingTime,
            computer1,
            writtingTime,
            tuitionTime,
            readingTime,
            dinnerTime,
            RestTime,
            sleepTime,
            ]
        elif collage == 'no' and writting == "no":   
            startTime = timeMaker(5,00)                             
            exerciseTime = TimeConverter(startTime, 20)
            freshingTime = TimeConverter(exerciseTime, 20)
            beats = TimeConverter(freshingTime, 10)
            comTime = TimeConverter(beats, 75)
            LearningTime1 = TimeConverter(comTime, 115)
            breakFast = TimeConverter(LearningTime1, 10)
            restTime = TimeConverter(breakFast, 50)
            computer1 = TimeConverter(restTime, 180)
            LearningTime2 = TimeConverter(computer1, 60)
            BLC = TimeConverter(LearningTime2, 40)
            RelaxingTime = TimeConverter(BLC, 60)
            computer = TimeConverter(RelaxingTime, 70)
            LearningTime = TimeConverter(computer,65)
            tuitionTime = TimeConverter(LearningTime, 115)
            readingTime = TimeConverter(tuitionTime, 100)
            dinnerTime = TimeConverter(readingTime, 10)
            RestTime = TimeConverter(dinnerTime, 20)
            sleepTime = TimeConverter(RestTime,420 ) 
            itemsList = [
            startTime,
            exerciseTime,
            freshingTime,
            beats,
            comTime,
            LearningTime1,
            breakFast,
            restTime,
            computer1,
            LearningTime2,
            BLC,
            RelaxingTime,
            computer,
            LearningTime,
            tuitionTime,
            readingTime,
            dinnerTime,
            RestTime,
            sleepTime,
            ]
    
        elif writting == 'no' and collage == "yes":   
            startTime = timeMaker(5,00)                             
            exerciseTime = TimeConverter(startTime, 20)
            freshingTime = TimeConverter(exerciseTime, 20)
            beats = TimeConverter(freshingTime, 10)
            comTime = TimeConverter(beats, 75)
            LearningTime1 = TimeConverter(comTime, 115)
            breakFast = TimeConverter(LearningTime1, 10)
            restTime = TimeConverter(breakFast, 15)
            collageTime = TimeConverter(restTime, 345)
            BLC = TimeConverter(collageTime, 40)
            computer = TimeConverter(BLC, 70)
            LearningTime = TimeConverter(computer, 55)
            tuitionTime = TimeConverter(LearningTime, 115)
            readingTime = TimeConverter(tuitionTime, 100)
            dinnerTime = TimeConverter(readingTime, 10)
            RestTime = TimeConverter(dinnerTime, 20)
            sleepTime = TimeConverter(RestTime,420 ) 
            itemsList = [
            startTime,
            exerciseTime,
            freshingTime,
            beats,
            comTime,
            LearningTime1,
            breakFast,
            restTime,
            collageTime,
            BLC,
            computer,
            LearningTime,
            tuitionTime,
            readingTime,
            dinnerTime,
            RestTime,
            sleepTime,
            ]
        elif collage == 'yes' and writting=="yes":
            startTime = timeMaker(5,00)                             
            exerciseTime = TimeConverter(startTime, 20)
            freshingTime = TimeConverter(exerciseTime, 20)
            beats = TimeConverter(freshingTime, 10)
            comTime = TimeConverter(beats, 75)
            LearningTime = TimeConverter(comTime, 115)
            breakFast = TimeConverter(LearningTime, 10)
            restTime = TimeConverter(breakFast, 15)
            collageTime = TimeConverter(restTime,345)
            BLC = TimeConverter(collageTime, 40)
            writtingTime = TimeConverter(BLC, 100)
            computer = TimeConverter(writtingTime, 25)
            tuitionTime = TimeConverter(computer, 115)
            readingTime = TimeConverter(tuitionTime, 100)
            dinnerTime = TimeConverter(readingTime, 10)
            RestTime = TimeConverter(dinnerTime, 20)
            sleepTime = TimeConverter(RestTime,420 )
            itemsList = [startTime,exerciseTime,freshingTime,beats,comTime,LearningTime,breakFast,
                        restTime,collageTime,BLC,writtingTime,computer,tuitionTime,readingTime,dinnerTime,RestTime,sleepTime,]
        else:
            print("Nothing Matched")
        return itemsList
def Dictionary(collage,writting):
    if collage == "yes" and writting == "yes":
        listingTime = Timerule(collage, writting)
        TitleList = [
                    'Body Exercise',
                    'Freshing',
                    'Mind Exercise',
                    "Computer",
                    "Learning Tech",
                    "Breakfast",
                    "Rest Time",
                    "Collage",
                    "B.L.C",
                    "Writting",
                    "Computer",
                    "Tuition",
                    "Reading",
                    "Dinner",
                    'Rest Time',
                    "Sleeping"
                    ]
    elif collage == "yes" and writting == "no":
        listingTime = Timerule(collage, writting)
        TitleList = [
                    'Body Exercise',
                    'Freshing',
                    'Mind Exercise',
                    "Computer",
                    "Learning Tech",
                    "Breakfast",
                    "Rest Time",
                    "Collage",
                    "B.L.C",
                    "Computer",
                    "Learning Tech",
                    "Tuition",
                    "Reading",
                    "Dinner",
                    'Rest Time',
                    "Sleeping"
                    ]
    elif collage == "no" and writting == "yes":
        listingTime = Timerule(collage, writting)
        TitleList = [
                    'Body Exercise',
                    'Freshing',
                    'Mind Exercise',
                    "Computer",
                    "Learning Tech",
                    "Breakfast",
                    "Rest Time",
                    "Computer",
                    "Learning Tech",
                    "B.L.C",
                    "Relaxing",
                    "Computer",
                    "Writting",
                    "Tuition",
                    "Reading",
                    "Dinner",
                    'Rest Time',
                    "Sleeping"
                    ]
    elif collage == "no" and writting == "no":
        global Timelist2
        listingTime = Timerule(collage, writting)
        TitleList = [
                    'Body Exercise',
                    'Freshing',
                    'Mind Exercise',
                    "Computer",
                    "Learning Tech",
                    "Breakfast",
                    "Rest Time",
                    "Computer",
                    "Learning Tech",
                    "B.L.C",
                    "Relaxing",
                    "Computer",
                    "Learning",
                    "Tuition",
                    "Reading",
                    "Dinner",
                    'Rest Time',
                    "Sleeping"
                    ]
    data = {}
    for i in range(len(TitleList)):
        dat = {f"d{i}":{}}
        data.update(dat)
    for i in range(len(TitleList)):
        datas = {"title":TitleList[i],"from":str(listingTime[i])[0:5],"to":str(listingTime[i+1])[0:5],"hour":Minutes[i]}
        data[f"d{i}"].update(datas)
    return data
def times():
    from datetime import datetime
    from datetime import time as timeMake
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    hour = int(current_time[0:2])
    minute = int(current_time[3:5])
    time = timeMaker(hour,minute)
    return time
def serialNum(collage,writting,serial): 
    timedict = Dictionary(collage,writting)
    for i in range(len(timedict)):
        strtime = timedict[f'd{i}']['from'] 
        strhour = int(strtime[0:2])
        strmin = int(strtime[3:5])
        strtime = timeMaker(strhour,strmin)
        time = times()
        if strtime <= time:
            serial = serial+1
    return serial