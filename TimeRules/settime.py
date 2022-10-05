from datetime import datetime as datetimes
from datetime import time as timeMake
import datetime
def times():
    now = datetimes.now()
    current_time = now.strftime("%H:%M")
    hour = int(current_time[0:2])
    minute = int(current_time[3:5])
    time = timeMake(hour,minute)
    return time
def serialNum(collage,writting):
    # collage no, writting yes
    if collage == "no" and writting == "yes":
        l1 = [datetime.time(5, 0), datetime.time(5, 20), datetime.time(5, 40), datetime.time(5, 50), datetime.time(7, 5), datetime.time(9, 0), datetime.time(9, 10), datetime.time(10, 0), datetime.time(13, 0), datetime.time(14, 0), datetime.time(14, 40), datetime.time(15, 40), datetime.time(16, 10), datetime.time(17, 55), datetime.time(19, 50), datetime.time(21, 30), datetime.time(21, 40), datetime.time(22, 0)]
        num = serialFinal(l1)

    # collage no, writting no
    if collage == "no" and writting == "no":
        l2 = [datetime.time(5, 0), datetime.time(5, 20), datetime.time(5, 40), datetime.time(5, 50), datetime.time(7, 5), datetime.time(9, 0), datetime.time(9, 10), datetime.time(10, 0), datetime.time(13, 0), datetime.time(14, 0), datetime.time(14, 40), datetime.time(15, 40), datetime.time(16, 50), datetime.time(17, 55), datetime.time(19, 50), datetime.time(21, 30), datetime.time(21, 40), datetime.time(22, 0)]
        num = serialFinal(l2)

    # collage yes, writting yes
    if collage == "yes" and writting == "yes":
        l3 = [datetime.time(5, 0), datetime.time(5, 20), datetime.time(5, 40), datetime.time(5, 50), datetime.time(7, 5), datetime.time(9, 0), datetime.time(9, 10), datetime.time(9, 25), datetime.time(15, 10), datetime.time(15, 50), datetime.time(17, 30), datetime.time(17, 55), datetime.time(19, 50), datetime.time(21, 30), datetime.time(21, 40), datetime.time(22, 0)]
        num = serialFinal(l3)

    # collage yes, writting no
    if collage == "yes" and writting == "no":
        l4 = [datetime.time(5, 0), datetime.time(5, 20), datetime.time(5, 40), datetime.time(5, 50), datetime.time(7, 5), datetime.time(9, 0), datetime.time(9, 10), datetime.time(9, 25), datetime.time(15, 10), datetime.time(15, 50), datetime.time(17, 0), datetime.time(17, 55), datetime.time(19, 50), datetime.time(21, 30), datetime.time(21, 40), datetime.time(22, 0)]
        num = serialFinal(l4)
    return num
def serialFinal(l):
    time = times()
    serial = 0
    for i in range(len(l)):
        print(time)
        if l[i] <= time:
            serial = serial + 1
            print(serial)
            print(l[i])
    return serial