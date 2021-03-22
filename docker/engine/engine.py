import os
import time

while True:
    print("")
    print("-- cycle start --")
    # pyPath = os.getcwd() + "/PyFiles"
    pyPath = "/app/PyFiles"
    pyFiles = [f for f in os.listdir(pyPath) if os.path.isfile(os.path.join(pyPath, f))]

    for pyFile in pyFiles:
        # pyRun = os.getcwd() + "/PyFiles/" + pyFile
        pyRun = "/app/PyFiles/" + pyFile
        os.system('{} {}'.format('python3', pyRun))
    
    print("-- cycle stop --")
    time.sleep(5) 
