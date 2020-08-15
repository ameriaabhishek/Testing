import os
import random
import subprocess
import time
import webbrowser

# config
RobotFilesList = 'RobotFilesList.txt'

baseFolder = 'C:\Abhishek\GIT-Projects\Project-1\data_tests'

# clean up base folder
os.system('rmdir /Q /S ' + baseFolder)
os.mkdir(baseFolder)

# no output to console please
FNULL = open(os.devnull, 'w')

# load list of usernames
f = open(RobotFilesList, 'r')
lines = f.readlines()
f.close()

# spawn subprocess for each user
robotFilePathes = []
processes = set()
for line in lines:
    
    robotFileName = line.strip()
    
    robotFilePath = os.path.join(baseFolder, robotFileName)
    os.mkdir(robotFilePath)
    
    filename = os.path.join("C:\\Abhishek\\GIT-Projects\\Project-1", robotFileName.strip())

    cmdParts = ['robot', filename]
    processes.add(subprocess.Popen(cmdParts, cwd=robotFilePath, stdout=FNULL))
    #print "Robot file executed"

    # random timeout to simulate more realistic user behavior
    #time.sleep(random.randint(0, 4))

# wait until all subprocesses finished

for proc in processes:
    proc.wait()