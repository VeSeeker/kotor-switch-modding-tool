from .util import Success, Warning, Error, CheckInitializedExists, CheckFileLists, CheckCaseSensitive, MirrorFolders, rootDir
import os

def Initialize(gameNum):

    print("")
    print("Running pre-flight checks... ")
    print("")

    print("Checking file lists")
    if CheckFileLists():
        Success("File lists present")
    else:
        Warning("Some file lists are not present")

    if CheckCaseSensitive():
        Warning(f"Case sensitive folder detected, this can cause undesired outcomes")
    else:
        Success(f"Case insensitive folder detected")

    if CheckInitializedExists(gameNum):
        Error(f"Kotor {gameNum} is already initialized")
        return False

    print("Mirroring PC folder structure... ")

    if MirrorFolders(os.path.join(rootDir, f"K{gameNum}romfs"), f"K{gameNum}PCFolders.txt"):
        return True
    else:
        Error("Folder mirroring failed")
        return False
