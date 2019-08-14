import subprocess
import tkinter
# what the fuck is going on


def get_clipboard():
    # p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    # data = str(p.stdout.read())
    mytk = tkinter.Tk().clipboard_get()
    tkinter.Tk().withdraw()
    print(str(mytk))

def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    print(data)
    return data

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()
# while True:
#     get_clipboard()

getClipboardData()
