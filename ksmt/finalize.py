from .util import CheckFinalizedExists, CheckInitializedExists, Error, Warning, Success, K1TitleID, K2TitleID, YesNo, rmrf, rootDir, fileListDir, MirrorFolders
from .backup import Backup, Restore
import os

def Finalize(gameNum):

    print("Running checks")

    if gameNum == "1":
        targetFolderName = K1TitleID
    elif gameNum == "2":
        targetFolderName = K2TitleID
    else:
        Error(f"Invalid game number: {gameNum}")
        return False
    targetFolderPath = os.path.join(rootDir, targetFolderName)


    if not CheckInitializedExists(gameNum):
        Error(f"Cannot finalize when no initialized folder exists")

    if CheckFinalizedExists(gameNum):
        Warning(f"Kotor {gameNum} has already been finalized")

        if YesNo(f"Delete finalized folder?: "):
            rmrf(targetFolderPath)
        else:
            Error("Cannot finalize when finalized folder already exists")
            return False

    switchFolders = (os.path.join(fileListDir, f"K{gameNum}SwitchFolders"))
    switchFiles = (os.path.join(fileListDir, f"K{gameNum}SwitchFiles"))
    switchDups = (os.path.join(fileListDir, f"K{gameNum}SwitchDuplicateFiles"))

    if not os.path.isdir(switchFolders):
        Error(f"Missing file list: {switchFolders}")
        return False
    else:
        print(f"{switchFolders} present")

    if not os.path.isdir(switchFiles):
        Error(f"Missing file list: {switchFiles}")
        return False
    else:
        print(f"{switchFiles} present")

    if not os.path.isdir(switchDups):
        Error(f"Missing file list: {switchDups}")
        return False
    else:
        print(f"{switchDups} present")

    Backup(gameNum, False)

    # Here the bash version deletes dialog.tlk and swplayer.ini if they are unmodified. I'm not really sure what the point of that is, so I'm leaving that out for now.

    print(f"Mirroring Kotor {gameNum} Switch ROM folder structure")

    if MirrorFolders(targetFolderName, f"K{gameNum}SwitchFolders"):
        Success("Mirrored Switch ROM folder structure")
    else:
        Error("Switch ROM folder structure mirroring failed")
        return False
    






    # Add a YesNo. If yes, then I will use the same logic as from the tga2tpc-py to automatically convert the textures that need to be converted. If no, then it just does what the original program does and moves the problem files into a new directory to be converted.




    return
