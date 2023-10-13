import os
from datetime import datetime

def makemydir() :
    now = datetime.now()
    s =  str(now.strftime("%d/%m/%Y"))
    try:
        os.makedirs(s)
    except:
        pass
    os.chdir(s)

makemydir()