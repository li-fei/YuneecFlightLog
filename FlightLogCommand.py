import sys
import FlightLog
import params


def getFileNameArgv():
    global filename1
    global filename2
    print(sys.argv[0], type(sys.argv[0]))
    argvsLen = len(sys.argv)
    print("argvsLen = ", argvsLen)
    if argvsLen > 1:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print(arg1, type(arg1))
        print(arg2, type(arg2))
        filename1 = arg1
        filename2 = arg2
    else:
        print(" no argv ... ")


if __name__ == '__main__':
    getFileNameArgv()

    params.fileNamePos = filename1.split("/")[-1]
    start = filename1.rindex("/")
    params.rootPath = filename1[0:start + 1]
    print("rootPath:", params.rootPath)
    print("-----> fileName :", params.fileNamePos, " * ", type(params.fileNamePos))

    params.fileNamePhotoTime = filename2.split("/")[-1]
    print("-----> fileName :", params.fileNamePhotoTime, " * ", type(params.fileNamePhotoTime))

    FlightLog.creatfile()
