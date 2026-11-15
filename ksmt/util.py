import os
from pathlib import Path
import sys
import tempfile
import shutil

# Text colors
Success = lambda t: print(Paint(f"Success! {t}", "32"))
Warning = lambda t: print(Paint(f"Warning: {t}", "33"))
Error = lambda t: print(Paint(f"Error: {t}", "31"))


K1TitleID = "0100854015868000"
K2TitleID = "0100B2C016252000"

scriptDir = Path(__file__).resolve().parent
rootDir = scriptDir.parent
fileListDir = os.path.join(scriptDir, "fileLists")
fileList = ["K1PCFolders.txt"]


def YesNo(text):
    while True:
        answer = input(text)
        if answer.lower() == 'y':
            return True
        elif answer.lower() == 'n':
            return False
        else:
            Warning("Please enter either y or n")

def MirrorFolders(folderName, targetTXT):
    targetFolder = os.path.join(rootDir, folderName)

    if targetTXT not in os.listdir(fileListDir):
        Error(f"{targetTXT} missing from {fileListDir}")
        return False

    with open(os.path.join(fileListDir, f"{targetTXT}"), 'r', encoding='utf-8') as file:
        folders = file.readlines()

    os.mkdir(targetFolder)

    for i in folders:
        name = i.replace("\n", '')
        os.mkdir(os.path.join(targetFolder, name))
        print(f"Created folder: {name}")

    return True

def CheckCaseSensitive():
    tmpHandle, tmpPath = tempfile.mkstemp()
    sens = False
    if os.path.exists(tmpPath.upper()):
        sens = False
    else:
        sens = True
    os.remove(tmpPath)
    return sens

def CheckInitializedExists(gameNum):
    if os.path.isdir(os.path.join(rootDir, f"K{gameNum}romfs")):
        # TODO: add a prompt here to delete the existing folder, if the user says yes then delete it and return false
        return True
    else:
        return False

def rmrf(delPath):
    if os.path.isdir(delPath) and not os.path.islink(delPath):
        shutil.rmtree(delPath)
    elif os.path.exists(delPath):
        os.remove(delPath)

def CheckFinalizedExists(gameNum):
    if gameNum == "1":
        if os.path.isdir(os.path.join(rootDir, K1TitleID)):
            return True
    elif gameNum == "2":
        if os.path.isdir(os.path.join(rootDir, K2TitleID)):
            return True
    return False

def CheckFileLists():
    hasAllFiles = True
    if os.path.isdir(fileListDir):
        hasFile = []
        for i in os.listdir(fileListDir):
            hasFile.append(i)
        for j in fileList:
            if j not in hasFile:
                Warning(f"Missing expected file from file list: {j}")
                hasAllFiles = False
        if hasAllFiles:
            return True
        else:
            return False
    else:
        Error("Can't find file list directory (Expected at ksmt/fileLists)")
        return False

def SupportsColor():
    if os.environ.get("NO_COLOR"):
        return False
    if os.environ.get("FORCE_COLOR"):
        return True
    return sys.stdout.isatty() and os.environ.get("TERM") != "dumb"

useColor = SupportsColor()

if useColor and sys.platform == "win32":
    os.system("")   # Enable ANSI processing

def Paint(text, code):
    return f"\033[{code}m{text}\033[0m" if useColor else text
