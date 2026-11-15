from __future__ import annotations
from .backup import Backup, Restore
from .finalize import Finalize
from .initialize import Initialize
from .util import Error, Warning, Success
import argparse

gameAliases = {
    '1': '1', "k1": '1', "kotor1": '1',
    '2': '2', "k2": '2', "kotor2": '2'
}

def GameType(value):
    try:
        return gameAliases[value.strip().lower()]
    except KeyError:
        valid = ", ".join(gameAliases)
        raise argparse.ArgumentTypeError(f"invalid game {value!r} (choose from: {valid})")

def ParseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "Action",
        help="Select which action you want to use",
        choices=["initialize", "backup", "restore", "finalize"],
        type=str.lower
    )
    parser.add_argument(
        "game",
        help="Select which game you want to mod (1 or 2)",
        type=GameType
    )

    return parser.parse_args()

def main():
    args = ParseArgs()

    if args.Action == "initialize":
        if Initialize(args.game):
            Success(f"Initialized Kotor {args.game} mod folder")
        else:
            Error(f"Kotor {args.game} mod folder initialization failed")
    elif args.Action == "backup":
        if Backup(args.game):
            Success(f"Backed up Kotor {args.game} mod folder")
        else:
            Error(f"Failed to back up Kotor {args.game} mod folder")
    elif args.Action == "restore":
        if Restore(args.game):
            Success(f"Restored Kotor {args.game} mod folder")
        else:
            Error(f"Failed to restore Kotor {args.game} mod folder")
    elif args.Action == "finalize":
        if Finalize(args.game):
            Success(f"Finalized Kotor {args.game} mod folder")
        else:
            Error(f"Failed to finalize Kotor {args.game} mod folder")
