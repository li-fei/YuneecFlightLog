# yuneec1 120.123456 31.123456 81.123
# yuneec2 120.265432 31.265432 81.234
import re
import sys
import os

filename1 = "1"
filename2 = "2"


def printFun(funName, str):
    print(funName, " function  ------------------------ ", str)
    return


def readfile(fname):
    f = open(fname, "r")
    data = f.read()
    f.close()


def writefile(fname, num):
    f = open(fname, "a")
    f.write("\nyuneec" + num + " 120.365432 31.365432 81.334")
    f.close()


def replaceStr(fname1, fname2, old, new):
    print(fname1, fname2, old, new)
    f = open(fname1, 'r')
    alllines = f.readlines()
    print(alllines)
    f.close()
    f = open(fname2, 'w+')
    for eachline in alllines:
        a = re.sub(old, new, eachline)
        f.writelines(a)
    f.close()


def getFileNameArgv():
    global filename1
    global filename2
    print(len(sys.argv))
    print(sys.argv[0], type(sys.argv[0]))
    if len(sys.argv) > 1:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print(arg1, type(arg1))
        print(arg2, type(arg2))
        filename1 = arg1
        filename2 = arg2
    else:
        print(" no argv ... ")


def file_name(file_dir):
    print(file_dir)
    list = os.listdir(file_dir)
    for line in list:
        print(line)
    printFun(sys._getframe().f_code.co_name, "end")


def main():
    printFun(sys._getframe().f_code.co_name, "start")
    # file_name(os.getcwd())
    # getFileNameArgv()
    # readfile(filename1)
    # for i in range(3):
    #     writefile(filename1, str(i))
    # readfile(filename1)

    oldstr = "120.123456"
    newstr = "121.666666"
    replaceStr(filename1, filename2, oldstr, newstr)
    printFun(sys._getframe().f_code.co_name, "end")

# main()
