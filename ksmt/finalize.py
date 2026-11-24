from .util import CheckFinalizedExists, CheckInitializedExists, CheckCaseSensitive, Error, Warning, Success, K1TitleID, K2TitleID, YesNo, rmrf, rootDir, fileListDir, MirrorFolders
from .backup import Backup
import os
import shutil
from .tga2tpc import converter, tex2tga
import struct
from .imageresize import downscale, resize

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

    k2Languages = ["English", "French", "German", "Italian", "Japanese", "Spanish"]

    if gameNum == "1":
        localizedPath = targetFolderPath
    else:
        for i in range(len(k2Languages)):
            print(f"[{i}] {k2Languages[i]}")
        while True:
            idx = 100
            choice = input("Select game language (I have only tested English so good luck): ")
            if choice.isdigit():
                idx = int(choice)
            if idx in range(len(k2Languages)):
                break
            else:
                print("Please enter a valid number")
        localizedPath = os.path.join(targetFolderPath, "Localized", k2Languages[idx])

    if CheckCaseSensitive():
        Warning(f"Case sensitive folder detected, this can cause undesired outcomes")
    else:
        Success(f"Case insensitive folder detected")

    if not CheckInitializedExists(gameNum):
        Error(f"Cannot finalize when no initialized folder exists")
        return False

    if CheckFinalizedExists(gameNum):
        Warning(f"Kotor {gameNum} has already been finalized")

        if YesNo(f"Delete finalized folder?: "):
            rmrf(targetFolderPath)
        else:
            Error("Cannot finalize when finalized folder already exists")
            return False

    switchFolders = os.path.join(fileListDir, f"K{gameNum}SwitchFolders.txt")
    switchFiles = os.path.join(fileListDir, f"K{gameNum}SwitchFiles.txt")
    initFolder = os.path.join(rootDir, f"K{gameNum}romfs")
    overrideDir = os.path.join(initFolder, "override")

    # This should be fine because it needs to be case insensitive, so it finds override and Override. Maybe add a check here that warns about case sensitivity again

    if not os.path.isfile(switchFolders):
        Error(f"Missing file list: {switchFolders}")
        return False
    else:
        print(f"{switchFolders} present")

    if not os.path.isfile(switchFiles):
        Error(f"Missing file list: {switchFiles}")
        return False
    else:
        print(f"{switchFiles} present")

    Backup(gameNum, False)

    # Here the bash version deletes dialog.tlk and swplayer.ini if they are unmodified. I'm not really sure what the point of that is, so I'm leaving that out for now.

    # print("Finding mod files")
    '''
    modFiles = []
    for root, dirs, filenames in os.walk(initFolder):
        for filename in filenames:
            modFiles.append(filename)
    '''
    # print(f"Found {len(modFiles)} modded files")

    print("Building Switch file set")

    switchTpcs = set()

    with open(switchFiles, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.replace("\n", '')
            directory, fullName = os.path.split(i)
            root, extension = os.path.splitext(fullName)
            if extension.lower() == ".tpc":
                switchTpcs.add(root.lower())
    print(f"Found {len(switchTpcs)} Switch .tpc files")

    print("Checking for duplicate textures")

    # Check if local tga/txi/dds files have a local tpc file in the same directory, and if not, check if they are part of the Switch's .tpc files, and if so, add them to dupTga
    invalidPath = os.path.join(initFolder, "ConvertMe")
    def MoveListToInvalidFolder(fileList):
        os.makedirs(invalidPath, exist_ok=True)
        for i in fileList:
            pt = os.path.join(overrideDir, i)
            shutil.move(pt, os.path.join(invalidPath, i))
            root, extension = os.path.splitext(i)
            maybeTxi = f"{root}.txi"
            if os.path.exists(os.path.join(overrideDir, maybeTxi)):
                shutil.move(os.path.join(overrideDir, maybeTxi), os.path.join(invalidPath, maybeTxi))
        Warning(f"Convert the files in {invalidPath} to .tpc, move them to override, delete {invalidPath}, and then re-run finalize")
        return
    modTpcSet = set()
    dupTga = []
    dupDds = []

    for i in os.listdir(overrideDir):
        root, extension = os.path.splitext(i)
        if extension.lower() == ".tpc":
            modTpcSet.add(root.lower())
    for j in os.listdir(overrideDir):
        root, extension = os.path.splitext(j)
        if (root.lower() not in modTpcSet) and (root.lower() in switchTpcs):
            if extension.lower() == ".tga":
                dupTga.append(j)
            elif extension.lower() == ".dds":
                dupDds.append(j)

    def ReadTgaSize(path):
        try:
            with open(path, "rb") as f:
                header = f.read(18)
        except OSError:
            return None
        if len(header) < 18:
            return None
        return struct.unpack_from("<HH", header, 12)
    def ReadTpcSize(path):
        try:
            with open(path, "rb") as f:
                header = f.read(128)
        except OSError:
            return None
        if len(header) < 128:
            return None
        return struct.unpack_from("<HH", header, 8)

    if len(dupTga) + len(dupDds) > 0:
        Warning(f"{len(dupTga) + len(dupDds)} files would be overridden by a base game .tpc file")

        convertTga = YesNo(f"Convert {len(dupTga) + len(dupDds)} files to .tpc using tga2tpc-py?")
        if not convertTga:
            MoveListToInvalidFolder(dupTga)
            MoveListToInvalidFolder(dupDds)
            return False
    downScale = YesNo("Downscale all 4k modded textures?: ")
    fourKTpc = []
    fourKTga = []
    if downScale:
        tga4K = 65000000
        tpc4K = 21000000
        for i in os.listdir(overrideDir):
            root, extension = os.path.splitext(i)
            size = os.path.getsize(os.path.join(overrideDir, i))
            if extension.lower() == ".tpc":
                if size > tpc4K:
                    fourKTpc.append(i)
            elif extension.lower() == ".tga":
                if size > tga4K:
                    fourKTga.append(i)
        print(f"Found {len(fourKTpc)} 4K .tpc files and {len(fourKTga)} 4K .tga files")

    oneNineTwo = []
    oneNineTwoSize = 123
    print("Finding non-power of 2 textures")
    for i in os.listdir(overrideDir):
        root, extension = os.path.splitext(i)
        if extension.lower() == ".tga":
            size = os.path.getsize(os.path.join(overrideDir, i))
            if size < oneNineTwoSize:
                imgSize = ReadTgaSize(os.path.join(overrideDir, i))
                if imgSize is None:
                    Warning(f"Couldn't read the size of {i}, skipping")
                    continue
                width, height = imgSize
                if width == 192 or width == 172:
                    if height == 192 or height == 172:
                        oneNineTwo.append(i)
    cnt = 0
    for i in oneNineTwo:
        pth = os.path.join(overrideDir, i)
        resize(pth, 256, 256, True)
        cnt += 1
        print(f"\rResized {cnt}/{len(oneNineTwo)}", end='')
    print("")

    options = tex2tga.TextureOptions()
    failedDds = []
    ddsCompleted = 0
    if len(dupDds) > 0:
        print("Converting DDS files to TGA")
    for i in dupDds:
        root, _ = os.path.splitext(i)
        newTga = os.path.join(overrideDir, f"{root}.tga")
        try:
            tex2tga.convert_file(os.path.join(overrideDir, i), newTga, options)
            ddsCompleted += 1
            dupTga.append(f"{root}.tga")
        except tex2tga.TextureConversionError as exc:
            Error(f"Failed to convert {i} to TGA: {exc}")
            failedDds.append(i)
        except Exception as exc:
            Error(f"Unexpected failure on {i}: {type(exc).__name__}: {exc}")
            failedDds.append(i)
        print(f"\rConverted {ddsCompleted}/{len(dupDds)}, {len(failedDds)} failures", end='')
    print("")
    if len(failedDds) > 0:
        MoveListToInvalidFolder(failedDds)
        return False

    tpcCompleted = 0
    failedTpcConvert = []
    if len(fourKTpc) > 0:
        print("Converting TPC files to TGA for downscaling")
    for i in fourKTpc:
        root, _ = os.path.splitext(i)
        newTga = os.path.join(overrideDir, f"{root}.tga")
        try:
            tex2tga.convert_file(os.path.join(overrideDir, i), newTga, options)
            tpcCompleted += 1
            dupTga.append(f"{root}.tga")
        except tex2tga.TextureConversionError as exc:
            Error(f"Failed to convert {i} to TGA: {exc}")
            failedTpcConvert.append(i)
        except Exception as exc:
            Error(f"Unexpected failure on {i}: {type(exc).__name__}: {exc}")
            failedTpcConvert.append(i)
        print(f"\rConverted {tpcCompleted}/{len(fourKTpc)}, {len(failedTpcConvert)} failures", end='')
    print("")
    if len(failedTpcConvert) > 0:
        print("Failed to convert some TPC files to TGA for downscaling")
        for i in failedTpcConvert:
            fourKTpc.remove(i)
    if len(fourKTpc) > 0:
        cnt = 0
        print("Downscaling 4K TPC files")
        for i in fourKTpc:
            root, _ = os.path.splitext(i)
            downscale(os.path.join(overrideDir, f"{root}.tga"), 50)
            cnt += 1
            print(f"\rDownscaled {cnt}/{len(fourKTpc)}", end='')
    print("")

    if len(fourKTga) > 0:
        cnt = 0
        print("Downscaling 4K TGA files")
        for i in fourKTga:
            downscale(os.path.join(overrideDir, i), 50)
            cnt += 1
            print(f"\rDownscaled {cnt}/{len(fourKTga)}", end='')
    print("")

    options = converter.ConversionOptions().normalised()

    if len(dupTga) > 0:
        print("Converting textures to TPC")

    completed = 0
    failedFiles = []

    for i in dupTga:
        root, extension = os.path.splitext(i)
        newTpc = os.path.join(overrideDir, f"{root}.tpc")
        try:
            converter.convert_file(os.path.join(overrideDir, i), newTpc, options)
            completed += 1
            modTpcSet.add(root.lower())
        except converter.ConversionError as exc:
            Error(f"Failed to convert {i}: {exc}")
            failedFiles.append(i)
        print(f"\rConverted {completed}/{len(dupTga)}, {len(failedFiles)} failures", end='')

    print("")

    print(f"{completed} files converted, {len(failedFiles)} files failed to convert")
    if len(failedFiles) > 0:
        MoveListToInvalidFolder(failedFiles)
        return False

    if os.path.isdir(invalidPath):
        Error(f"{invalidPath} needs to be deleted before finalizing")
        if YesNo(f"Delete {invalidPath}?: "):
            rmrf(invalidPath)
        else:
            return False

    print("Cleaning up redundant texture files")
    redTpc = []
    redTga = []
    badExt = [".tga", ".txi", ".dds"]
    for i in os.listdir(overrideDir):
        root, ext = os.path.splitext(i)
        if ext.lower() == ".tpc":
            redTpc.append(root)
    for i in os.listdir(overrideDir):
        root, ext = os.path.splitext(i)
        if ext.lower() in badExt:
            if root in redTpc:
                redTga.append(i)
    print(f"Found {len(redTga)} redundant files")
    for i in redTga:
        os.remove(os.path.join(overrideDir, i))
    Success("Cleaned up redundant files")

    print(f"Mirroring Kotor {gameNum} Switch ROM folder structure")

    if MirrorFolders(targetFolderName, f"K{gameNum}SwitchFolders.txt"):
        Success("Mirrored Switch ROM folder structure")
    else:
        Error("Switch ROM folder structure mirroring failed")
        return False

    # The rest of the logic

    print("Building Switch file dictionary")

    allSwitchFiles = dict()

    with open(switchFiles, 'r', encoding='utf-8') as f:
        for i in f.readlines():
            i = i.replace("\n", '')
            _, fullName = os.path.split(i)
            allSwitchFiles[fullName.lower()] = i

    Success(f"Indexed {len(allSwitchFiles)} Switch files")

    print("Finding modded base game files")

    vanillaModFiles = []

    for root, _, filenames in os.walk(initFolder):
        for i in filenames:
            if i.lower() in allSwitchFiles:
                vanillaModFiles.append(os.path.join(root, i))

    count = 0
    for i in vanillaModFiles:
        _, fullName = os.path.split(i)
        shutil.move(i, os.path.join(targetFolderPath, allSwitchFiles[fullName.lower()]))
        count += 1
        print(f"\rMoving modded base game files: {count}/{len(vanillaModFiles)}", end='')
    print("")

    newTextures = []
    textureExt = [".tga", ".txi", ".tpc", ".dds"]
    new2da = []
    newLocalized = []
    basicFile = []

    for root, _, filenames in os.walk(initFolder):
        relPath = os.path.relpath(root, initFolder).split(os.sep)[0]
        lowRelPath = relPath.lower()
        for i in filenames:
            if lowRelPath == "override":
                _, ext = os.path.splitext(i)
                if ext.lower() in textureExt:
                    newTextures.append(os.path.join(root, i))
                elif ext.lower() == ".2da":
                    new2da.append(os.path.join(root, i))
                else:
                    basicFile.append(os.path.join(root, i))
            elif lowRelPath == "docs":
                newLocalized.append(os.path.join(root, i))
            elif lowRelPath == "streamvoice":
                newLocalized.append(os.path.join(root, i))
            elif lowRelPath == "streamwaves":
                newLocalized.append(os.path.join(root, i))
            elif lowRelPath == "lips":
                newLocalized.append(os.path.join(root, i))
            else:
                basicFile.append(os.path.join(root, i))
    targetOverride = os.path.join(targetFolderPath, "override")

    if gameNum == "1":
        texPath = os.path.join(targetOverride, "Textures")
        twoDAPath = os.path.join(targetOverride, "2da")
    else:
        texPath = os.path.join(targetOverride, "textures")
        twoDAPath = os.path.join(targetOverride, "2DA")

    if len(newTextures) > 0:
        print("Moving modded textures files")
        cnt = 0
    for i in newTextures:
        _, name = os.path.split(i)
        shutil.move(i, os.path.join(texPath, name))
        cnt += 1
        print(f"\rMoved texture files: {cnt}/{len(newTextures)}", end='')
    print("")

    if len(new2da) > 0:
        print("Moving modded 2da files")
        cnt = 0
    for i in new2da:
        _, name = os.path.split(i)
        shutil.move(i, os.path.join(twoDAPath, name))
        cnt += 1
        print(f"\rMoved 2da files: {cnt}/{len(new2da)}", end='')
    print("")

    if len(newLocalized) > 0:
        print("Moving localized files")
        cnt = 0
    for i in newLocalized:
        path, name = os.path.split(i)
        relPath = os.path.relpath(path, initFolder)
        shutil.move(i, os.path.join(localizedPath, relPath, name))
        cnt += 1
        print(f"\rMoved localized files: {cnt}/{len(newLocalized)}", end='')
    print("")

    if len(basicFile) > 0:
        print("Moving remaining files")
        cnt = 0
    for i in basicFile:
        path, name = os.path.split(i)
        relPath = os.path.relpath(path, initFolder)
        shutil.move(i, os.path.join(targetFolderPath, relPath, name))
        cnt += 1
        print(f"\rMoved remaining files: {cnt}/{len(basicFile)}", end='')
    print("")

    Success(f"Finalized folder created at {targetFolderPath}")

    # Check if there are any files left in the init folder, and if not, delete the init folder

    return True
