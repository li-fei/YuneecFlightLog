import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox

import FlightLog
import params

root = tkinter.Tk()
root.title("YUNEEC")
# root.geometry("600x300+200+100")
curWidth = 600
curHight = 300
scn_w, scn_h = root.maxsize()
cen_x = (scn_w - curWidth) / 2
cen_y = (scn_h - curHight) / 2
size_xy = '%dx%d+%d+%d' % (curWidth, curHight, cen_x, cen_y)
root.geometry(size_xy)
# root["bg"] = "#8FBC8F"


lablePos = tkinter.Label(root, text='Pos文件:')
lablePos.place(x=10, y=20)
lablePhotoTime = tkinter.Label(root, text='PhotoTime文件:')
lablePhotoTime.place(x=10, y=60)


def selectPathPos():
    path_ = tkinter.filedialog.askopenfilename()
    # path_ = path_.replace("/", "\\\\")
    if len(path_) > 0:
        print("--------------------> ", len(path_))
        # global fileNamePos
        params.fileNamePos = path_.split("/")[-1]
        print(os.path.split(path_)[0], os.path.split(path_)[1])
        start = path_.rindex("/")
        params.rootPath = path_[0:start + 1]
        print("rootPath:", params.rootPath)
        print("-----> fileName :", params.fileNamePos, " * ", type(params.fileNamePos))
        pathPos.set(path_)
        lablePos.config(text='pos文件: ' + params.fileNamePos)


def selectPathPhotoTime():
    path_ = tkinter.filedialog.askopenfilename()
    # path_ = path_.replace("/", "\\\\")
    if len(path_) > 0:
        print("--------------------> ", len(path_))
        params.fileNamePhotoTime = path_.split("/")[-1]
        print("-----> fileName :", params.fileNamePhotoTime, " * ", type(params.fileNamePhotoTime))
        pathPhotoTime.set(path_)
        lablePhotoTime.config(text='PhotoTime文件: ' + params.fileNamePhotoTime)


frame = tkinter.Frame(root)
frame.place(x=10, y=100)

pathPos = tkinter.StringVar()
tkinter.Label(frame, height=3, text="pos文件:").grid(row=0, column=0, sticky=tkinter.W)
tkinter.Entry(frame, width=40, textvariable=pathPos).grid(row=0, column=1)
tkinter.Button(frame, text="文件选择", command=selectPathPos).grid(row=0, column=2)

pathPhotoTime = tkinter.StringVar()
tkinter.Label(frame, text="PhotoTime文件:").grid(row=1, column=0)
tkinter.Entry(frame, width=40, textvariable=pathPhotoTime).grid(row=1, column=1)
tkinter.Button(frame, text="文件选择", command=selectPathPhotoTime).grid(row=1, column=2)


def fun():
    # l0.config(text="替换成功")
    oldstr = "120.123456"
    newstr = "121.666666"
    if params.fileNamePos is None:
        tkinter.messagebox.showwarning("提示", "没有选择pos文件")
    elif params.fileNamePhotoTime is None:
        tkinter.messagebox.showwarning("提示", "没有选择PhotoTime文件")
    else:
        # yuneec.replaceStr(fileNamePos, fileNamePhotoTime + "_new", oldstr, newstr)
        FlightLog.creatfile()
        tkinter.messagebox.showinfo("提示", "替换成功")


bt = tkinter.Button(root, text='生成FlightLog.csv文件', command=fun)
bt.place(x=curWidth / 2 - 100, y=230)

root.mainloop()
