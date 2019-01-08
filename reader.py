import serial
import datetime
import time
ser = serial.Serial('/dev/ttyACM0', 9600)
outf = open('output.txt', 'a')
outf.truncate(0)

def readValue(s):
    try:
        x = float(s[0])
        y = float(s[1])
        z = float(s[2])
    except:
        x = 0
        y = 0
        z = 0
    return (x, y, z)
    
##dateStart = datetime.datetime.now()
##finishTime = dateStart + datetime.timedelta(seconds=30)
while (True):
    read_serial = ser.readline()
    s = read_serial.split()
    (x, y, z) = readValue(s)
    timeNow = time.time()
    if (x != 0):
        print((str(timeNow) + " " + str(x) + " " + str(y)+ " " + str(z) + "\n"))
        outf.write(str(timeNow) + " " + str(x) + " " + str(y)+ " " + str(z) + "\n")
        outf.flush()
