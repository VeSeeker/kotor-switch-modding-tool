from .util import CheckFinalizedExists, CheckInitializedExists, Error, Warning, Success, K1TitleID, K2TitleID, YesNo, rmrf, rootDir, fileListDir, MirrorFolders
from .backup import Backup, Restore
import os
import shutil

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

    switchFolders = os.path.join(fileListDir, f"K{gameNum}SwitchFolders")
    switchFiles = os.path.join(fileListDir, f"K{gameNum}SwitchFiles.txt")
    switchDups = os.path.join(fileListDir, f"K{gameNum}SwitchDuplicateFiles.txt")
    initFolder = os.path.join(rootDir, f"K{gameNum}romfs")
    overrideDir = os.path.join(initFolder, "override")

    # This should be fine because it needs to be case insensitive, so it finds override and Override. Maybe add a check here that warns about case sensitivity again

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

    print("Finding mod files")

    modFiles = []
    for root, dirs, filenames in os.walk(initFolder):
        for filename in filenames:
            modFiles.append(filename)

    print(f"Found {len(modFiles)} modded files")

    print(f"Mirroring Kotor {gameNum} Switch ROM folder structure")

    if MirrorFolders(targetFolderName, f"K{gameNum}SwitchFolders"):
        Success("Mirrored Switch ROM folder structure")
    else:
        Error("Switch ROM folder structure mirroring failed")
        return False

    print("Checking for duplicate textures")

    # Check if local tga/txi/dds files have a local tpc file in the same directory
    tpcSet = set()
    problemExt = [".tga", ".txi", ".dds"]
    dupTga = []

    for dirPath, dirNames, fileNames in os.walk(overrideDir):
        for i in fileNames:
            root, extension = os.path.splitext(i)
            if extension == ".tpc":
                tpcSet.add(root)
    for dirPath, dirNames, fileNames in os.walk(overrideDir):
        for j in fileNames:
            root, extension = os.path.splitext(j)
            if extension in problemExt:
                if root in tpcSet:
                    dupTga.append(j)

    if len(dupTga) > 0:
        Warning(f"{len(dupTga)} files would be overridden by a .tpc file")
        # word this better ^
        tpcBackup = (os.path.join(initFolder, "TPCBackup"))
        os.mkdir(tpcBackup)
        count = 0
        for i in dupTga:
            root, extension = os.path.splitext(i)
            moveMe = os.path.join(overrideDir, root + ".tpc")
            if os.path.exists(moveMe):
                shutil.move(moveMe, tpcBackup)
                count += 1
                print(f"\nTpc files moved: {count}", end='')
        print(f"Moved redundant TPC files to {tpcBackup}")

    # Print a cool counter like this:
    # for i in X:
    #   print(f"\rThing: {i}/{total}", end='')




    # Check local tga/txi/dds files for a switch original tpc file

    print("Building file dictionary")

    fileDict = dict()

    with open(switchFiles, 'r', encoding='utf-8') as f:
        files = f.readlines()

    for i in files:
        if '/' not in i:
            fileName = i
            filePath = ''
        else:
            splt = i.rsplit('/', 1)
            fileName = splt[-1]
            filePath = splt[:-1]

        fileDict[fileName] = filePath
        print(f"Added file {fileName} with {filePath}")

    Success(f"Created {len(fileDict)} dictionary")








    # Add a YesNo. If yes, then I will use the same logic as from the tga2tpc-py to automatically convert the textures that need to be converted. If no, then it just does what the original program does and moves the problem files into a new directory to be converted.




    return
