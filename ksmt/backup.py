from .util import Error, Warning, Success, rootDir, CheckInitializedExists
import os
import shutil

rootBackupDir = os.path.join(rootDir, "backups")

def Backup(gameNum):

    print("Running pre-flight checks... ")

    if not CheckInitializedExists(gameNum):
        Error(f"No Kotor {gameNum} folder to backup")
        return False
    if not os.path.isdir(rootBackupDir):
        print("Creating backup folder")
        os.mkdir(rootBackupDir)

    print("Generating next backup name... ")
    # Backups will be called "K{gameNum}_Backup_{index}

    nextIndex = 0

    backupList = []
    for i in os.listdir(rootBackupDir):
        if i[1] == gameNum:
            backupList.append(i)
    if len(backupList) != 0:
        backupList = sorted(backupList)
        nextIndex = int(backupList[-1][-1]) + 1

    targetBackupDir = os.path.join(rootBackupDir, f"K{gameNum}_Backup_{nextIndex}")

    print(f"Generating backup at {targetBackupDir}... ")

    shutil.move(os.path.join(rootDir, f"K{gameNum}romfs"), targetBackupDir)

    return True

def Restore(gameNum):
    return
