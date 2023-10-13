import os
import datetime

def makemydir() :
    s =  str(datetime.date.today())
    DownDir = "Downloads"
    os.chdir(DownDir)
    try:
        if os.path.exists(s):
            pass
        else :
            os.makedirs(s)
    except:
        pass
    os.chdir(s)

makemydir()