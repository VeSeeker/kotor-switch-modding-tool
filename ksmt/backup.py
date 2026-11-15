from .util import Error, Warning, Success, rootDir, CheckInitializedExists, YesNo, rmrf, Paint
import os
import shutil

rootBackupDir = os.path.join(rootDir, "backups")

def Backup(gameNum, deleteAfterBackup=True):

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

    print(f"Generating backup at {targetBackupDir}")

    if deleteAfterBackup:
        shutil.move(os.path.join(rootDir, f"K{gameNum}romfs"), targetBackupDir)
    else:
        shutil.copytree(os.path.join(rootDir, f"K{gameNum}romfs"), targetBackupDir)

    return True

def Restore(gameNum):
    if CheckInitializedExists(gameNum):
        Warning(f"Kotor {gameNum} is already initialized")
        if YesNo(f"Delete initialized folder?: "):
            rmrf(os.path.join(rootDir, f"K{gameNum}"))
        else:
            Error("Can't restore backup when game is already initialized")
            return False

    backupList = []

    for i in os.listdir(rootBackupDir):
        if i[1] == gameNum:
            backupList.append(i)


    choice = 0

    validIndexes = []
    if len(backupList) != 0:
        print("Available Backups:")
        for j in backupList:
            print(j[:-1] + Paint(j[-1], "34"))
            validIndexes.append(j[-1])
    else:
        Error("No available backups to restore")
        return False

    while True:

        answer = input("Which index do you want to restore?: ")

        if answer in validIndexes:
            choice = answer
            break
        else:
            Warning("Please enter a valid index")


    if YesNo(f"Delete backup {choice} after restore?"):
        shutil.move(os.path.join(rootBackupDir, f"K{gameNum}_Backup_{choice}"), f"K{gameNum}romfs")
    else:
        shutil.copytree(os.path.join(rootBackupDir, f"K{gameNum}_Backup_{choice}"), f"K{gameNum}romfs")
    return True
