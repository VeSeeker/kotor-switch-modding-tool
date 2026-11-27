# kotor-switch-modding-tool

This is a python rewrite of DrSnuggly's [kotor-ii-switch-modding](https://github.com/DrSnuggly/kotor-ii-switch-modding). It supports both Kotor 1 & 2, and should run on any OS with Python.
It also optionally uses the same logic as my tga2tpc-py to automatically convert .tga files to .tpc, as well as downscale 4k textures.

Based on and inspired by work from:\
[DrSnuggly](https://github.com/DrSnuggly)\
[jacqylfrost](https://deadlystream.com/profile/48469-jacqylfrost/)\
[JC2](https://deadlystream.com/profile/25613-jc2/)\
[Leilukin](https://deadlystream.com/profile/23862-leilukin/)

## Modding Guides

Use my modding guides!\
[Kotor 1 Switch modding guide](K1Guide.md)\
[Kotor 2 Switch modding guide](K2Guide.md)

## Features

- Provide a folder structure that modding tools expect
- Optionally convert necessary files to `.tpc` format
- Optionally downscale 4K textures
- Once modding is done, restructure the game folder to what the Nintendo Switch version of the game expects
- Call out potential issues along with instructions on how to fix them
- Easy backups and restores during the modding process, to better see where things went wrong

## Usage instructions

### Prerequisites

- A computer to install mods with — mods cannot be installed directly on the Nintendo Switch).
  - This tool uses Python, and requires the following libraries:
    - numpy
    - Pillow
- A Nintendo Switch running custom firmware, or an emulator
- A way to dump game files, either:
    - [nxdumptool](https://github.com/DarkMatterCore/nxdumptool) to dump files directly on the Switch
    - Dumping through an emulator on a computer (easier)

### Setup

1. Download the latest release of this repository from GitHub
1. Extract the downloaded release zip file
1. Open a terminal window and navigate to the extracted folder
   - e.g. `cd "~/Downloads/kotor-switch-modding-tool"`
1. Run the following commands from this directory
    - Every command is run with the following syntax, where gameNumber is 1 or 2:
        - Mac/Linux: ```python -m ksmt <command> <gameNumber>```
        - Windows: ```py -m ksmt <command> <gameNumber>```

### Usage

#### Initialize

```ksmt initialize <gameNumber>```

- This will create a folder `kotor-switch-modding-tool/K<gameNumber>romfs`
- This folder has the PC version's file structure, which is what mod expect
- You will probably want to dump `dialog.tlk` from the Switch's files:
    - Kotor 1: `romfs/dialog.tlk`
    - Kotor 2: `romfs/Localized/<language>/dialog.tlk`
- Place `dialog.tlk` in the root of `K<gameNumber>romfs` that was created from initializing
- Proceed to install mods into `kotor-switch-modding-tool/K<gameNumber>romfs`

#### Backup

```ksmt backup <gameNumber>```

- This creates a backup of your `K<gameNumber>romfs` folder
- Will fail if there is no `K<gameNumber>romfs` folder
- You can have multiple backups of each game
- Backups are stored at `kotor-switch-modding-tool/backups/`

#### Restore

```ksmt restore <gameNumber>```

- This will restore a previously backed up initialized folder
- Will prompt you to select which backup you want to restore:
```
Available Backups:
K1_Backup_0
K1_Backup_1
Which index do you want to restore?: 0
Delete backup 0 after restore? (y/n): y
Success! Restored Kotor 1 mod folder
```
- Will fail if there is already a `K<gameNumber>romfs` folder in `kotor-switch-modding-tool`

#### Finalize

```ksmt finalize <gameNumber>```

- This finalizes your `K<gameNumber>romfs` folder, moving modded files into the directories that the Switch version of the game expects to find them at
- Finalizing automatically backs up your `K<gameNumber>romfs` folder
- Finalize has many extra prompts, each is explained below:
    - `Select game language`: This is only for Kotor 2, as `dialog.tlk` goes to different places depending on the language of the game
    - `Delete finalized folder?`: This occurs if there is already a finalized folder for the game you selected. Entering `y` will delete that folder, and the proceed with the finalization
    - `Convert <X> files to .tpc using tga2tpc-py?`: Will convert necessary .dds and .tga files to .tpc. Saying no will move those files into a folder called `ConvertMe`. You'll need to convert those files to .tpc, then move those new .tpc files to your `K<gameNumber>romfs/override` folder, and re-run finalize
    - `Downscale all 4K modded textures?`: Will downscale 4K modded textures, because too many 4K textures can overwhelm the Switch's RAM
    - `Extra downscales? (VeSeeker's modding guide)`: Downscales textures based on my guide
- After running finalize, a `kotor-switch-modding-tool/<GameID>` folder will have been created
    - Kotor 1 ID: 0100854015868000
    - Kotor 2 ID: 0100B2C016252000
- Move that folder to `/atmosphere/contents/` on your Switch.
    - If that folder already exists on your Switch, delete it first

## Known issues

### Platform-specific known issues and fixes

- The Sith Lords Restored Content Mod (TSLRCM)
  - Button prompts are either missing or showing buttons for the incorrect platform
    - Fix: after installing this mod, use the `dialog.tlk` from [here](https://gbatemp.net/threads/knights-of-the-old-republic-ii-switch-modding.635861/)

### Mods that require additional dumped files

#### Kotor 1

- Leviathan Prison Break
    - `lips/lev_m40aa_loc.mod`

#### Kotor 2

- Darth Sion and Male Exile Mod 1.2.3
    - `lips/702kor_loc.mod`
    - `lips/907mal_loc.mod`
- Extended Korriban arrival 1.2
    - `lips/003EBO_loc.mod`
- Handmaiden and Female Exile - Disciple and Male Exile Romance
    - `lips/262TEL_loc.mod`
    - `lips/402DXN_loc.mod`
    - `lips/903MAL_loc.mod`
    - `lips/localization.mod`
- HQ Skyboxes II
    - `/Modules/401dsn.rim`

## License and attribution

This project is licensed under the GNU GPL v3 (see [LICENSE](LICENSE)).

It is a Python rewrite of [kotor-ii-switch-modding](https://github.com/DrSnuggly/kotor-ii-switch-modding),
Copyright (C) 2023 DrSnuggly, also licensed under GPL v3. The original was based on and inspired by jacqylfrost's work. This version was modified by VeSeeker beginning 2026: ported from Bash to Python, added KotOR 1 support, and added TGA/TPC conversion and downscaling.
