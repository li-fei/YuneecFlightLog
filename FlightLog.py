import sys
import os

import params
import yuneec

print("*" * 20, "FlightLog.py")
FlightLogTitle = "Sourcefile,gpslatitude,gpslongitude,gpsaltitude,gpslatituderef,gpslongituderef,gpsaltituderef\n"
flightLogFile = None
timeFileAlllines = None
posFileAlllines = None


def creatfile():
    if os.path.exists(params.rootPath + params.FlightLogFileName):
        os.remove(params.rootPath + params.FlightLogFileName)
    global flightLogFile
    flightLogFile = open(params.rootPath + params.FlightLogFileName, "a")
    flightLogFile.write(FlightLogTitle)
    readPhotoTimeFile()
    readPosFile()
    writeFileToFlightLog()


def readPhotoTimeFile():
    yuneec.printFun(sys._getframe().f_code.co_name, "start")
    print(params.rootPath + params.fileNamePhotoTime)
    f = open(params.rootPath + params.fileNamePhotoTime, "r")
    global timeFileAlllines
    timeFileAlllines = f.readlines()
    for line in timeFileAlllines:
        # print(line)
        pass
    f.close()


def readPosFile():
    yuneec.printFun(sys._getframe().f_code.co_name, "start")
    print(params.rootPath + params.fileNamePos)
    f = open(params.rootPath + params.fileNamePos, "r")
    global posFileAlllines
    posFileAlllines = f.readlines()
    f.close()


def find_close(list, number):
    fnum = float(number)
    print("fnum", fnum, ",type(fnum):", type(fnum))
    print("type(list):", type(list), " ,type(number):", type(number), ",number:", number)
    result = min(list, key=lambda x: abs(x - fnum))
    print("find_close result:", result, " ;index", list.index(result))
    return list.index(result)


def findPosLineTooClose(millisecond, tragetPosMillisecond, tragetPosLines):
    print("photo file ,millisecond:", millisecond)
    # for msecond in tragetPosMillisecond:
    #     print("pos file, millisecond:", msecond)
    index = find_close(tragetPosMillisecond, millisecond)
    print("pos file, close line:", tragetPosLines[index])
    for line in tragetPosLines:
        print("pos file, line:", line)
    return index


def writeFileToFlightLog():
    for line in timeFileAlllines:
        writeFileToFlightLogLine(line.split(","))

    flightLogFile.close()


def writeFileToFlightLogLine(timeFileLine):
    # print(timeFileAlllines[0])
    # timeFileLine = timeFileAlllines[7].split(",")
    for str in timeFileLine:
        print(str)
    print(type(timeFileLine), timeFileLine)
    print(type(timeFileLine), " fileNamePhotoTime lines : ", len(timeFileAlllines))

    print(type(posFileAlllines), " fileNamePhotoTime lines : ", len(posFileAlllines))

    jpgName = timeFileLine[0]
    timeWeekMillisecond = timeFileLine[1][0: (len(timeFileLine[1]) - 3)]
    timeWeek = timeFileLine[1].split(".")[0]
    millisecond = timeFileLine[1].split(".")[1][0:3]
    print("*** jpgName:", jpgName, ";timeWeekMillisecond:", timeWeekMillisecond, ";timeWeek:", timeWeek,
          ";millisecond:", millisecond)

    tragetPosLines = []
    tragetPosMillisecond = []
    for line in posFileAlllines:
        if line.strip().find(timeWeek) != -1:
            if "." in line:
                tragetPosLines.append(line)
                tragetPosMillisecond.append(float(line.split(",")[1].split(".")[1]))
                # print("find in pos :", line)
    index = findPosLineTooClose(millisecond, tragetPosMillisecond, tragetPosLines)
    print("pos file. close line:", tragetPosLines[index], type(tragetPosLines[index]))
    listTragetPosLines = tragetPosLines[index].split(",")
    lat = listTragetPosLines[2].replace(" ", "")
    lon = listTragetPosLines[3].replace(" ", "")
    height = listTragetPosLines[4].replace(" ", "")
    flightLogLine = [jpgName + ",", lat + ",", lon + ",", height + ",", "N,E,above sea level", "\n"]
    writeLineStrToFlightLog(flightLogLine)


def writeLineStrToFlightLog(line):
    if flightLogFile is None:
        print("FlightLogFile is None")
    else:
        flightLogFile.writelines(line)
        flightLogFile.flush()
