# Kotor 1 Switch Modding Guide
#### By VeSeeker

## 1 Introduction
#### Warning: This is an experimental build. Like, more experimental than the other two builds. I'll update as I test it

This guide is based on the neocities [KOTOR 1 Full Build for PC](https://kotor.neocities.org/modding/mod_builds/k1/full). I have gotten the vast majority of the mods in that build working on the Switch. You will need a modded Switch [running custom firmware](https://switch.hacks.guide/), or an emulator.

Beyond the need for a modded Switch, there are a few things that make modding Kotor on the Switch more difficult. One thing is that the Switch version shipped with a lot of `.tpc` texures in it's override folder. Any modded `.tga` or `.dds` file will not override those files unless we convert them to `.tpc`. My [modding tool](https://github.com/VeSeeker/kotor-switch-modding-tool) handles this.

On the topic of textures, many of the mods we will install use 4k textures. Although quite the visual improvement, they end up causing [5.1 Out of VRAM](#51-out-of-vram). The solution to this that I use is to downscale all the 4k textures by 50%. You could probably min-max this by only downscaling half of them or something, but I don't feel like it would be worth it. My modding tool also takes care of downscaling textures. If you are worried about the quality loss, don't be. The 2k textures are still a massive improvement over the originals. Some modules get extremely close to the VRAM limit, so follow this guide closely.

## 2 Setup
#### You really do need to read this part

You should download the latest release of my [modding tool](https://github.com/VeSeeker/kotor-switch-modding-tool).

Some mods need files from the base game in order to successfully install. You can do this through the Switch with [nxdumptool](https://github.com/DarkMatterCore/nxdumptool), or through an emulator (which I think is easier).

I will annotate mod names based on their installation process as compared to the neocities guide:

Normal installation
~~Mod not working on the Switch~~

I made a few '[patches](https://www.mediafire.com/folder/40ihkqn3tezon/Patches)' to make mods work on the Switch. What these actually are for the most part is just `.txi` files from the base game that aren't included in the mod files.

Finally, many mods use the TSLPatcher. Sometimes, this patcher is set to automatically detect your Kotor install. You'll need to change that setting [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection) if you have the PC version of the game installed (or even if you've had it installed before and the folder still exists). I'll include in the installation instructions if that mod's TSLPatcher automatically detects or not

### 2.1 Tools

#### 2.1.1 Kotor Switch Modding Tool

Download [here](https://github.com/VeSeeker/kotor-switch-modding-tool). This is a really cool tool that I wrote. It is a rewrite of DrSnuggly's [kotor-ii-switch-modding](https://github.com/DrSnuggly/kotor-ii-switch-modding). It's a bit faster, includes automatic downscaling, and *should* work on Windows, Mac, and Linux.

The repository has more detailed information, so check there if you have any questions. To get started, download the latest release and extract the folder somewhere convienient. Open a terminal in that folder and run `ksmt initialize 1`. That should create the folder `kotor-switch-modding-tool/K1romfs`. This is the folder you will be installing all of your mods into.

#### 2.1.2 TSLPatcher automatic installation detection

Simply change 'LookupGameFolder' from 1 to 0 in the patcher `.ini`. It is normally called `changes.ini` and is located in the tslpatchdata folder. If it is called something different, I will include that in the mod's installation instructions.

## 3 Mods

### 3.1 Switch Texture Restoration

- **Author:** jacqylfrost
- **Download:** [Mod](https://deadlystream.com/files/file/2103-kotor-switch-texture-restoration)
- **Method:** Loose-file\
**Installation instructions:** Extract the texture files into override, not a subfolder.

---
### 3.2 Switch Icons and UI Upscale

- **Author:** VeSeeker
- **Download:** [Mod](https://deadlystream.com/files/file/3074-kotor-1-ui-and-icon-upscale-for-nintendo-switch/)
- **Method:** Loose-file\
**Installation instructions:** Extract the textures in both folders into override.

---
### 3.3 KOTOR Dialogue Fixes

- **Author:** Salk & Kainzorus Prime
- **Download:** [Mod](https://deadlystream.com/files/file/1313-kotor-dialogue-fixes/)
- **Method:** Loose-file\
**Installation instructions:** Move one of the `dialog.tlk` files into `K1romfs/`, not override.

---
### 3.4 Character Startup Changes & Patch

- **Author:** jonathan7, patch by A Future Pilot
- **Download:** [Mod](http://deadlystream.com/files/file/349-character-start-up-change/) [Patch](https://mega.nz/file/sRw1GBIK#J8znLBwR6t7ZvZnpQbsUBYcUNfPCWA7wYNW3qU6gZSg)
- **Method:** TSLPatcher, Loose-file\
**Installation instructions:** Run TSLPatcher first, then copy the loose files into override.

---
### 3.5 Thematic KOTOR Companions

- **Author:** Sniggles & JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2665-thematic-kotor-companions/)
- **Method:** TSLPatcher
---
### 3.6 JC's Minor Fixes

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1333-jcs-minor-fixes-for-k1/)
- **Method:** Loose-file\
**Installation instructions:** Move everything from 'Straight Fixes', 'Resolution Fixes', and 'Aesthetic Improvements' into override. From 'Things what bother me' skip N_AdmrlSaulKar.mdl, N_AdmrlSaulKar.mdx, N_SithComF.mdl, N_SithComF.mdx, N_SithComM.mdl, and N_SithComM.mdx. Skip the 'Bugfix' folder.

---
### 3.7 Ajunta Pall Appearance & Patch

- **Author:** Silveredge9, Patch by Future Pilot
- **Download:** [Mod](https://deadlystream.com/files/file/824-ajunta-pall-unique-appearance/) [Patch](https://mega.nz/file/McJF1AIC#Jywhu6zXWCRz4gRghxMxoBAWrbU_A3giD1INsOoHqmA)
- **Method:** TSLPatcher, Loose-file\
**Installation instructions:** Install the patch first. Then move the files in either the 'Transparent' or 'Non-Transparent' folder into override. You can optionally move the 'Sith eyes' files into override as well.

---
### 3.8 KOTOR Community Patch & Patch

- **Author:** Various Authors; Darth Parametric, JCarter426 & A Future Pilot Collate
- **Download:** [Mod](https://deadlystream.com/files/file/1258-kotor-1-community-patch/) [Patch](https://mega.nz/file/gQZR1TZY#U7XN5teK9wjXC5Hnj7MFlmHYb8UFyaV5R17ksIuj7Jc)
- **Method:** HoloPatcher, Loose-file
---
### 3.9 Droid Claw Fix

- **Author:** GearHead
- **Download:** [Mod](https://deadlystream.com/files/file/2456-kotor1-droid-claw-fix/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.10 Ported VO Replacements

- **Author:** Ashton Scorpius
- **Download:** [Mod](https://deadlystream.com/files/file/1426-k1-ported-alien-vo-replacements/)
- **Method:** HoloPatcher\
**Installation instructions:** Install the main mod, then re-run the patcher and select the K1CP compatibility install options if using [3.8 KOTOR Community Patch & Patch](#38-kotor-community-patch--patch)

---
### 3.11 Ultimate Korriban & Patch

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1367) [Patch](https://mega.nz/file/NEpH3AoZ#5RVfQHjkdk6b3lgcJzgitpCb1YQlfYqhTM0XF3Z9LMM)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
**Installation instructions:** Delete or fix `LKO_blast01`, `LKOa_blast1`. See [5.2 Texture Outlines](#52-texture-outlines)

---
### 3.12 Ultimate Kashyyyk

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1365)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
---
### 3.13 Ultimate Tatooine

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1364)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
**Installation instructions:** Delete or fix `LTA_blas01`. See [5.2 Texture Outlines](#52-texture-outlines)

---
### 3.14 Ultimate Dantooine

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1368)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
**Installation instructions:** Delete or fix `LDA_leaf01`, `02`, and `04`. See [5.2 Texture Outlines](#52-texture-outlines)

---
### 3.15 Ultimate Endar Spire +

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1370)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
---
### 3.16 Ultimate Manaan

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1366)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
---
### 3.17 Ultimate Taris

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1360)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
**Installation instructions:** Delete `LSI_win01.tpc` and `LSI_box01.tpc` before moving to override

---
### 3.18 Ultimate Character Overhaul

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1282)
- **Method:** Loose-file\
**Download instructions:** Download only the 2x `.tpc` version\
---
### 3.19 Ultimate Unknown World

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1369)
- **Method:** Loose-file\
**Download instructions:** Download the `.tpc` version\
**Installation instructions:** Delete `LUN_blst01.tpc` and `LUN_blst02.tpc` before moving to override. Delete or fix `LUN_blst01`, `02`, `LUN_rocky2`, `LUN_sand02`. See [5.2 Texture Outlines](#52-texture-outlines)

---
### 3.20 Korriban Sith Art

- **Author:** MessesWithWolves
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1632)
- **Method:** Loose-file\
**Download instructions:** Download and install both files.\
---
### 3.21 Duncan on Manaan

- **Author:** Seamhainn
- **Download:** [Mod](https://mega.nz/file/IR4QASTa#V28cTdgcNTMPwPrNbMElbnNVHkqhkKu7vJgL7PWVZ0U)
- **Method:** Loose-file
---
### 3.22 Consistent Conditioning

- **Author:** Sdub
- **Download:** [Mod](https://deadlystream.com/files/file/2013-consistent-conditioning-icons/)
- **Method:** Loose-file
---
### 3.23 HD Pazaak Cards

- **Author:** CarthOnasty
- **Download:** [Mod](https://deadlystream.com/files/file/1361-hd-pazaak-cards/)
- **Method:** Loose-file\
**Installation instructions:** Move all the loose files to override. If you'd like Kotor 2-style specialty cards (green-colored), move the files from the "green" folder to the override folder as well.

---
### 3.24 HD PC Portraits

- **Author:** ndix UR
- **Download:** [Mod](https://deadlystream.com/files/file/1547-hd-pc-portraits/)
- **Method:** Loose-file
---
### 3.25 PMHA05 HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1857-pmha05-hd/)
- **Method:** Loose-file
---
### 3.26 PMHA02 HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1843-pmha02-hd/)
- **Method:** Loose-file
---
### 3.27 PMHA01 HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1837-pmha01-hd/)
- **Method:** Loose-file
---
### 3.28 PFHC05 HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1738-pfhc05-hd/)
- **Method:** Loose-file
---
### 3.29 PFHB02 Eye Fix

- **Author:** Darth Parametric
- **Download:** [Mod](https://deadlystream.com/files/file/1762-player-head-pfhb02-dark-side-transition-eye-fix/)
- **Method:** Loose-file
---
### 3.30 High-Poly Grenades

- **Author:** MadDerp
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1209)
- **Method:** Loose-file
---
### 3.31 HD Gizka

- **Author:** Emperor Turnip
- **Download:** [Mod](https://deadlystream.com/files/file/1190-emperor-turnips-hd-gizka/)
- **Method:** Loose-file\
**Installation instructions:** The file has the wrong readme; move all the files in the Creatures folder, except for the readme and Gizka.jpg (any .jpg/.png files are always previews and can be deleted), to the override.

---
### 3.32 Gammorean Reskin Pack

- **Author:** Quanon
- **Download:** [Mod](http://deadlystream.com/files/file/1023-quanons-gammorean-reskin-pack/)
- **Method:** Loose-file
---
### 3.33 War Droids HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2188-war-droid-mark-i-hd/)
- **Method:** Loose-file
---
### 3.34 HD Cleaning Droids

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2220-astromechhd/)
- **Method:** Loose-file
---
### 3.35 HD Jawas

- **Author:** Etienne76
- **Download:** [Mod](https://deadlystream.com/files/file/2517-hd-realistic-jawas/)
- **Method:** Loose-file
---
### 3.36 HD Sand People & Patch

- **Author:** Etienne76
- **Download:** [Mod](https://deadlystream.com/files/file/2514-hd-realistic-sand-people/) [Patch](https://mega.nz/file/1ApXxLgY#iAK97Ydx2xvH5ws7NevJGU3ZJQarhBwDAIFcH73O3W4)
- **Method:** Loose-file\
**Download instructions:** For this mod, download the `.tga` filetype version (not the `.tpc`).\
---
### 3.37 Better Twi'lek Heads

- **Author:** Ashton Scorpius
- **Download:** [Mod](https://deadlystream.com/files/file/1430-k1-better-twilek-male-heads/)
- **Method:** HoloPatcher\
**Installation instructions:** Choose whether to use the slim or original necks; your preference.

---
### 3.38 HD Twi'lek Females

- **Author:** Dark Hope
- **Download:** [Mod](http://deadlystream.com/files/file/982-hd-twilek-female/)
- **Method:** Loose-file\
**Download instructions:** Download the 'hd_twilek_female.rar' file, and ignore the other versions.\
---
### 3.39 Thigh-High Boots for Twi'lek

- **Author:** DarthParametric
- **Download:** [Mod](http://deadlystream.com/files/file/1087-k1-thigh-high-boots-for-female-twilek-body-modders-resource/)
- **Method:** Loose-file\
**Installation instructions:** Unzip the mod, enter the NPC Replacement folder, and move the six files within (NOT including the optional folder or its contents) to the override.

---
### 3.40 Shaleena/Lashowe Mouth Fix

- **Author:** Ashton Scorpius
- **Download:** [Mod](https://deadlystream.com/files/file/1480-k1-shaleenalashowe-mouth-adjustment/)
- **Method:** Loose-file
---
### 3.41 Calo Nord Recolor

- **Author:** Watcher07
- **Download:** [Mod](https://mega.nz/file/hJhGEbza#qemCHVzBcCWkL__n6mrmVNzD3P2qdV4MWEYQvJudtJY)
- **Method:** Loose-file
---
### 3.42 HD Darth Malak

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/980-hd-darth-malak/)
- **Method:** Loose-file\
**Download instructions:** Do not download the .tga file.\
**Installation instructions:** If intending to use CineMalak below (recommended!), select your preferred head texture from the Malak (Red Eyes) or Malak (Blue Eyes) folders and move the files within to your override. You can ignore N_DarthMalak01.tga, unless you do not want to use CineMalak, in which case you should also move it to your override.

---
### 3.43 CineMalak

- **Author:** PoopaPoppaPalpatine
- **Download:** [Mod](https://deadlystream.com/files/file/2787-cinemalak-hd-malak-retexture/)
- **Method:** Loose-file\
**Installation instructions:** The downloaded file is a loose .tga, not inside an archive. For this mod, just move the downloaded file (N_DarthMalak01.tga) to your override directly.

---
### 3.44 Detran's Darth Revan

- **Author:** Detran
- **Download:** [Mod](https://deadlystream.com/files/file/2350-detrans-darth-revan/)
- **Method:** Loose-file\
**Installation instructions:** Make a copy of the file and rename it PMBJ01.tga, then move all files to override.

---
### 3.45 Darth Bandon HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2164-darth-bandon-hd/)
- **Method:** Loose-file
---
### 3.46 HD Vrook

- **Author:** Dark Hope, edited by Publicola
- **Download:** [Mod](https://deadlystream.com/files/file/1962-hd-vrook-recolored/)
- **Method:** Loose-file
---
### 3.47 HD UI Elements & Switch Patch

- **Author:** Sdub, Switch Patch by VeSeeker
- **Download:** [Mod](https://deadlystream.com/files/file/1909-random-hd-ui-elements/) [Switch Patch](https://www.mediafire.com/file/yufzempfpbom5vr/Random_HD_UI_Elements_Switch_Patch.zip/file)
- **Method:** Loose-file\
**Download instructions:** Download just the random UI elements download, not the optional T3-M4 request.\
**Installation instructions:** Install the Planet Icons from the main mod, and then move the Switch Patch into override

---
### 3.48 HD NPC Portraits

- **Author:** ndix UR
- **Download:** [Mod](https://deadlystream.com/files/file/1213-hd-npc-portraits/)
- **Method:** Loose-file\
**Download instructions:** Download the V2 option.\
**Installation instructions:** Ignore the 'V1 Looks' option.

---
### 3.49 Male NPC Clothing

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2516-npc-clothing-m/)
- **Method:** Loose-file\
**Download instructions:** Ignore the txi.rar file.\
**Installation instructions:** Delete n_commm07.tga and N_CommMD01.tga. Delete N_CommM08.tga, then make a copy of N_CommM0801 and paste it in the same directory. This should create a duplicate file; rename that duplicate file to "N_CommM08.tga" and then move all files to override.

---
### 3.50 ~~Juhani Appearance Overhaul & Patch~~

- **Author:** Stormie97, Patch by JCarter
- **Download:** [Mod](https://deadlystream.com/files/file/1669-juhani-appearance-overhaul/) [Patch](https://mega.nz/file/wM5hwA7Z#tbwFY3_kU2oR_AcKl879tCOlyC_i-cUtqb_HXak3lBU)
- **Method:** TSLPatcher\
**Installation instructions:** ~~Use the Body & Lightsaber version, we will use a different head model. Make sure to install the patch after, it fixes an issue with her lightsaber which can cause it to disappear.~~ Avoid unless you can figure out this bug: [5.3 Model Problems](#53-model-problems)

---
### 3.51 Juhani Cathar Head

- **Author:** Miro42
- **Download:** [Mod](http://deadlystream.com/files/file/702-juhani-real-cathar-head/)
- **Method:** Loose-file
---
### 3.52 Korriban: Back in Black

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1293-jcs-korriban-back-in-black-for-k1/)
- **Method:** TSLPatcher\
**Installation instructions:** If running the Community Patch (you should be), install the Community Patch-Compatible install option; otherwise, select Basic. If you would like Master Uthar or Yuthura Ban (the two top Sith at the academy) to wear alternate outfits instead of robes, re-run the patcher to select your preferred options AFTER running the initial install.

---
### 3.53 Cloaked Jedi Robes

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1378-jcs-fashion-line-i-cloaked-jedi-robes-for-k1/)
- **Method:** TSLPatcher\
**Installation instructions:** When installing, use the screenshots provided to determine which robe style you would like to use. Aesthetically, I strongly recommend the Brown-Red-Blue Alternative.

---
### 3.54 JC's Jedi Tailor

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1477-jcs-jedi-tailor-for-k1/)
- **Method:** TSLPatcher\
**Installation instructions:** If you use Cloaked Jedi Robes's 100% Brown option, make sure to install the 100% Brown compatibility patch after the main mod installation (re-run the executable).

---
### 3.55 Cloaks with Shadows

- **Author:** PapaZinos
- **Download:** [Mod](https://deadlystream.com/files/file/2357-robes-with-shadows-for-k1-jcs-port/)
- **Method:** Loose-file\
**Installation instructions:** Only move the files from "Jedi Robes Override".

---
### 3.56 Qel-Droma Reskin

- **Author:** Effix
- **Download:** [Mod](https://deadlystream.com/files/file/2019-effixians-qel-droma-robes-reskin-for-jcs-cloaked-jedi-robes/)
- **Method:** Loose-file
---
### 3.57 Quanon's HK-47

- **Author:** Quanon
- **Download:** [Mod](http://deadlystream.com/files/file/1001-quanons-hk-47-reskin/)
- **Method:** Loose-file\
**Installation instructions:** Delete PO_phk47.tga before moving the two other files to the override.

---
### 3.58 HD Sign Placeable

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2442-plc_sign/)
- **Method:** Loose-file
---
### 3.59 HD Kiosk & Patch

- **Author:** Dark Hope, patch by Marius Fett
- **Download:** [Mod](https://deadlystream.com/files/file/2277-kiosk-hd/) [Patch](https://deadlystream.com/files/file/2909-kiosk-model-fix-for-k1/)
- **Method:** Loose-file\
**Download instructions:** Download the "Kiosk HD 15.03.2024" version.\
---
### 3.60 HD Desk

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2441-plc_desk/)
- **Method:** Loose-file
---
### 3.61 HD Escape Pod

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2435-lts_escapepod-hd/)
- **Method:** Loose-file
---
### 3.62 HD Weapon Placeables

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2434-non-game-weapon/)
- **Method:** Loose-file
---
### 3.63 K2 Swoops to K1

- **Author:** CaptainSpoque
- **Download:** [Mod](https://deadlystream.com/files/file/2729-k1-k2-swoops-to-k1/)
- **Method:** HoloPatcher
---
### 3.64 HD Stun Batons & Switch Patch

- **Author:** Dark Hope, Switch Patch by VeSeeker
- **Download:** [Mod](https://deadlystream.com/files/file/2430-stunbaton-hd/) [Switch Patch](https://www.mediafire.com/file/01zojm92663bs8x/HD_Stun_Batons_Switch_Patch.zip/file)
- **Method:** Loose-file\
**Download instructions:** Unless you want icons like those in the preview images (which I recommend against, as it will not match the vanilla aesthetic for most of the other equipment icons in the game), do not download the "stunbaton 2025" file; only download "Stun baton HD".\
**Installation instructions:** Install the main mod, and then move the file from the Switch Patch into override

---
### 3.65 Unique Sith Governor

- **Author:** N-DReW25
- **Download:** [Mod](https://deadlystream.com/files/file/2302-unique-sith-governor/)
- **Method:** HoloPatcher
---
### 3.66 HD Ithorians

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2382-ithorian-hd/)
- **Method:** Loose-file\
**Download instructions:** Choose between the base install and the Vurt retexture based on your preference. The preview screenshots at the top of the page are the base install, the spoilered screenshots at the bottom of the mod description are the modified Vurt versions.\
---
### 3.67 HD Duros

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2252-duros-hd/)
- **Method:** Loose-file
---
### 3.68 HD Quarren

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2383-qarren-hd/)
- **Method:** Loose-file
---
### 3.69 HD Davik

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2371-davik-hd/)
- **Method:** Loose-file
---
### 3.70 HD Doctors

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2475-doctors-hd/)
- **Method:** Loose-file
---
### 3.71 Kebla Yurt HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2471-kebla-yurt-hd/)
- **Method:** Loose-file\
**Installation instructions:** Delete N_CommF02.tga & .txi before moving to override.

---
### 3.72 HD Deadeye Duncan

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2801-deadeye-duncan-hd/)
- **Method:** Loose-file
---
### 3.73 N_oldAMH01 HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2806-n_oldamh01-hd/)
- **Method:** Loose-file
---
### 3.74 HD Astromech Droids

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1894-astromech-droid-hd/)
- **Method:** Loose-file\
**Installation instructions:** Delete po_pt3m33.tga before moving the files to your override.

---
### 3.75 HD Protocol Droids

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2056-protocol-droid-hd/)
- **Method:** Loose-file
---
### 3.76 Davik's Trophies

- **Author:** Thor110
- **Download:** [Mod](https://deadlystream.com/files/file/2559-daviks-trophies/)
- **Method:** Loose-file
---
### 3.77 HD Carth Onasi

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1133-hd-carth-onasi/)
- **Method:** Loose-file\
**Download instructions:** Download the file "Carth Onasi (new clothes).rar", unless you like the head & face changes the mod makes.\
**Installation instructions:** Delete PO_pcarth3.tga before moving the other files to the override.

---
### 3.78 HD Canderous Ordo & Patch

- **Author:** Dark Hope
- **Download:** [Mod](http://deadlystream.com/files/file/1123-hd-canderous-ordo/) [Patch](https://mega.nz/#!dFJBEYhA!FY9h6AmYVDizyVPZo_I3vXqAIWVrK1TUzT42msGqtpQ)
- **Method:** Loose-file & Patch\
**Download instructions:** Download only the version marked 'new clothes,' which includes both clothing and body textures. We get our head texture from the below mod. Remember to also download the patch.\
---
### 3.79 Quanon's Canderous

- **Author:** Quanon
- **Download:** [Mod](http://deadlystream.com/files/file/941-quanons-canderous-ordo-reskin/)
- **Method:** Loose-file\
**Installation instructions:** Move only P_CandH01.tga to your override.

---
### 3.80 Jolee HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1935-jolee-bindo-hd/)
- **Method:** Loose-file
---
### 3.81 Fen's Jolee

- **Author:** Fenharel
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1192)
- **Method:** Loose-file\
**Download instructions:** Download the default, not the iconic recolor.\
**Installation instructions:** Move ONLY P_joleeh01.tga and P_joleeh01.txi to your override.

---
### 3.82 Zaalbar HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2031-zaalbar-hd/)
- **Method:** Loose-file\
**Download instructions:** Personally recommend against the "ZaalbarHD (Vurt's KotOR Visual Resurgence)" version. It's a larger texture which I personally think looks worse.\
**Installation instructions:** Delete po_pzaalbar3.tga before moving the files to your override.

---
### 3.83 Sith Uniform Reformation Revised

- **Author:** Heyorange, Sith Holocron, JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2808-heyoranges-sith-uniform-reformation-revised/)
- **Method:** TSLPatcher\
**Installation instructions:** When installing, select the Community Patch-compatible installation, if using the K1CP (you should be). Ignore the other install options.

---
### 3.84 Stylized Portraits

- **Author:** /u/Tinman888
- **Download:** [Mod](https://deadlystream.com/files/file/1929-stylized-portraits-by-tinman888/)
- **Method:** Loose-file\
**Installation instructions:** Strongly recommend the Lite version—the quality difference is not noticeable, but the filesize footprint of the large versions is huge and could contribute to load errors in multiple modules. Do not install the files from the "PC" folder unless you want your character's portrait appearance to be that of Revan.

---
### 3.85 Star Map Revamp & Switch Patch

- **Author:** Carth0nasty, Switch Patch by VeSeeker
- **Download:** [Mod](https://deadlystream.com/files/file/1262-star-map-revamp/) [Switch Patch](https://www.mediafire.com/file/ktsbj636fj97qw8/Star_Map_Revamp_Switch_Patch.zip/file)
- **Method:** Loose-file\
**Installation instructions:** Install the main mod, and then move the file from the Switch Patch into override.

---
### 3.86 Background Improvements

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1125-hd-kt-400-military-droid-carrier-and-lethisk-class-armed-freighter/)
- **Method:** Loose-file\
**Download instructions:** Download the "hd_kt_400_military_droid_carrier_and_lethisk_class_armed_freighter.rar" option.\
---
### 3.87 Kebla Yurt Renovation

- **Author:** N-DReW25
- **Download:** [Mod](https://deadlystream.com/files/file/2785-kebla-yurt-renovation/)
- **Method:** HoloPatcher
---
### 3.88 Hi-Res Ebon Hawk

- **Author:** Vurt
- **Download:** [Mod](https://www.gamefront.com/games/knights-of-the-old-republic/file/vurt-s-k1-hi-res-ebon-hawk-retexture)
- **Method:** Loose-file\
**Installation instructions:** Once the mod is extracted, copy the file 'LDA_EHawk01' and make a duplicate of it. Rename this duplicate to 'M36_EHawk01.tga' and then move all files to the override.

---
### 3.89 Ebon Hawk Repairs

- **Author:** PapaZinos
- **Download:** [Mod](https://deadlystream.com/files/file/2036-ultimate-ebon-hawk-repairs-for-k1/)
- **Method:** Loose-file\
**Installation instructions:** Move the files from "to override" to your override folder, then also move the files from the "Animated Monitors" folder and overwrite when prompted.

---
### 3.90 HQ Cockpit Skyboxes

- **Author:** Sithspecter
- **Download:** [Mod](http://deadlystream.com/files/file/938-high-quality-cockpit-skyboxes/)
- **Method:** Loose-file\
**Download instructions:** Download the small version\
---
### 3.91 Yavin Station Hangar

- **Author:** WildKarrde
- **Download:** [Mod](https://deadlystream.com/files/file/2068-yavin-station-hangar/)
- **Method:** TSLPatcher & Loose-file with SITUATIONAL Patch (see Installation Instructions!)\
**Installation instructions:** If you would like the forcefield for the hangar to be visible, re-run the installer after installing the main option and also install the visible forcefield option. If using HQ Cockpit Skyboxes, move the files from the resolution folder corresponding to the HQ Cockpit Skyboxes size you utilized to your override, then delete ebo_yab.tga, ebo_yaf.tga, ebo_yal.tga, ebo_yar.tga and ebo_yat.tga from your override. Finally, if you utilize Vurt's "K1 Hi-Res Ebon Hawk Retexture," download [this patch](https://mega.nz/file/QAhhFTzD#rxS91pehFgNP7xFh3DNnNFC1d_YelF43K4-q6mh8xfI) and move its contents to your override.

---
### 3.92 Ebon Hawk Cockpit Upgrade I

- **Author:** Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/2258-ebon-hawk-cockpit-upgrade-leh_scre01-more-subtle-version/)
- **Method:** Loose-file
---
### 3.93 Ebon Hawk Cockpit Upgrade II

- **Author:** Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/2247-ebon-hawk-cockpit-upgrade-leh_scre02/)
- **Method:** Loose-file\
**Installation instructions:** Recommend the version without overlays, but it's personal preference.

---
### 3.94 Taris Reskin & Patch

- **Author:** Quanon, patch by JCarter426
- **Download:** [Mod](http://www.nexusmods.com/kotor/mods/10/) [Patch](https://mega.nz/file/8MogRKIa#NKl_vTrTMQiAPtjNZ4chvsaw6aOd_4l-8lC47ODW1Z0)
- **Method:** Loose-file\
**Installation instructions:** Don't install the included modifications to the Dantooine Estates or Sith Base, you'll only be installing the contents of Part 1 and Part 2. You will additionally need to delete the following files from the Part 1 folder before moving the mod content to the override folder: LTS_Bsky01.tga, LTS_Bsky02.tga, and (sorted by name) LTS_sky0001.tga through LTS_SKY0005.tga

---
### 3.95 High Quality Starfields & Switch Patch

- **Author:** Kexikus, Switch Patch by VeSeeker
- **Download:** [Mod](http://deadlystream.com/files/file/491-kotor-high-quality-starfields-and-nebulas/) [Switch Patch](https://www.mediafire.com/file/2rfg9vovbpten5g/High_Quality_Starfields_Switch_Patch.zip/file)
- **Method:** Loose-file\
**Installation instructions:** Install the main mod, and then move the file from the Switch Patch into override

---
### 3.96 HQ Skyboxes II & Patch

- **Author:** Kexikus, patch by CaptainSpoque
- **Download:** [Mod](https://deadlystream.com/files/file/723-high-quality-skyboxes-ii/) [Patch](https://deadlystream.com/files/file/2796-high-quality-skyboxes-model-fixes-v10/)
- **Method:** Loose-file\
**Download instructions:** Unless using one of the mods for which Kex has developed skyboxes (not recommended, as they're almost certainly not compatible with this build) simply download the 'HQSkyboxesII_K1.7z' file.\
**Installation instructions:** Delete m36aa_01_lm0 through m36aa_01_lm2.tga before moving to the override, then apply the patch. Delete `CM_m02abB.tga`, otherwise you crash in Taris upper city.

---
### 3.97 Ebon Hawk Transparent Cockpit Windows

- **Author:** WildKarrde
- **Download:** [Mod](https://deadlystream.com/files/file/2354-ebon-hawk-transparent-cockpit-windows-for-k1/)
- **Method:** Loose-file\
**Installation instructions:** Apply the main installation, then go into the Compatibility Patches folder and apply the contents of the "Leviathan - K1CP Forcefield" folder (if using K1CP), HQ Skyboxes compatch (if using HQ Skyboxes), and Yavin Station Hangar (if using WildKarrde's Yavin Station Hangar).

---
### 3.98 Hires Beam Effects

- **Author:** InSidious
- **Download:** [Mod](https://deadlystream.com/files/file/260-k1-hi-res-beam-effects/)
- **Method:** Loose-file
---
### 3.99 HD Fire & Ice

- **Author:** Cinder Skye
- **Download:** [Mod](https://deadlystream.com/files/file/455-hd-fire-and-ice-whee/)
- **Method:** Loose-file
---
### 3.100 Animated Energy Shields & Switch Patch

- **Author:** Dark Hope, Switch Patch by VeSeeker
- **Download:** [Mod](https://deadlystream.com/files/file/2193-animated-energy-shields/) [Switch Patch](https://www.mediafire.com/file/a7dwopmivrocajp/Animated_Energy_Shields_Switch_Patch.zip/file)
- **Method:** Loose-file\
**Installation instructions:** Install the main mod, and then move the files in the Switch Patch into override

---
### 3.101 Animated Cantina Sign

- **Author:** Sith Holocron
- **Download:** [Mod](http://deadlystream.com/files/file/1129-animated-cantina-sign-for-kotor-1/)
- **Method:** Loose-file
---
### 3.102 Revamped FX

- **Author:** olegkuz1997
- **Download:** [Mod](https://deadlystream.com/files/file/2581-revamped-fx/)
- **Method:** Loose-file\
**Installation instructions:** I recommend against any of the included optional files.

---
### 3.103 Terminal Texture

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1925-terminal-texture/)
- **Method:** Loose-file\
**Download instructions:** Which version to use is up to you; the first image on the mod page is the version of the texture from the "PLC_CompPnl(Vurt's KotOR Visual Resurgence) 2026.rar" download, the second image is the original download, and the third image is the vanilla terminal texture.\
---
### 3.104 HD Workbench

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2222-reptab-hd/)
- **Method:** Loose-file
---
### 3.105 Animated Swoop Monitors

- **Author:** ebmar
- **Download:** [Mod](https://deadlystream.com/files/file/1398-k1-animated-swoop-screen-tslport/)
- **Method:** Loose-file
---
### 3.106 Loadscreens in Color

- **Author:** Sithspecter
- **Download:** [Mod](http://deadlystream.com/files/file/916-loadscreens-in-color/)
- **Method:** Loose-file
---
### 3.107 ~~Reflective Lightsaber Blades~~

- **Author:** Crazy34
- **Download:** [Mod](https://deadlystream.com/files/file/1846-new_lightsaber_blade_model_k1/)
- **Method:** TSLPatcher\
**Installation instructions:** ~~The mod builds are only tested with the standard install option; other options are untested for compatibility and function. Use at your own risk!~~ Avoid unless you can figure out this bug: [5.7 Reflective Lightsaber Problem](#57-reflective-lightsaber-problem)

---
### 3.108 ~~Darth Malak's Lightsaber~~

- **Author:** Marius Fett
- **Download:** [Mod](https://deadlystream.com/files/file/2506-darth-malaks-lightsaber-k1/)
- **Method:** HoloPatcher\
**Installation instructions:** Avoid unless you can figure out this bug: [5.7 Reflective Lightsaber Problem](#57-reflective-lightsaber-problem)

---
### 3.109 Blaster Visual Effects

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1271-jcs-blaster-visual-effects-for-k1/)
- **Method:** Loose-file\
**Installation instructions:** Move everything from the override folder to your game's override directory, unless you would like yellow/green disruptors, in which case those files should be moved from the optional folder after moving all loose files to the override first.

---
### 3.110 Wookiee Warblade Fix

- **Author:** RedRob
- **Download:** [Mod](https://deadlystream.com/files/file/1899-wookie-warblade-fix/)
- **Method:** Loose-file
---
### 3.111 Kill The Czerka Guard

- **Author:** TamerBill
- **Download:** [Mod](https://deadlystream.com/files/file/1856-request-kill-the-czerka-jerk-on-kashyyyk/)
- **Method:** TSLPatcher
---
### 3.112 Korriban Workbench

- **Author:** InSidious
- **Download:** [Mod](https://deadlystream.com/files/file/375-korriban-academy-workbench/)
- **Method:** Loose-file
---
### 3.113 Senni Vek Mod

- **Author:** N-DReW25
- **Download:** [Mod](https://deadlystream.com/files/file/1090-senni-vek-mod/)
- **Method:** HoloPatcher\
**Installation instructions:** For realism I personally recommend the "Senni Vek's Ambush" install, but if you'd like to remain as close to vanilla as possible, choose the Senni Vek Restoration instead.

---
### 3.114 Male Twi'lek Diversity

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2228-kotor-1-twilek-male-npc-diversity/)
- **Method:** HoloPatcher\
**Installation instructions:** Run the installer and install the Main Installation first. Once the main install is completed, select the optional upscaled textures install option and install it, if desired. If using the original necks option of Ashton Scorpius's Better Twi'lek Males mod, also ensure to run the "[Optional] Original Necks" install option. Finally, if using the Senni Vek Mod, ensure to also re-run the installer and select the compatibility patch for whichever version of that mod you've chosen to use (Senni Vek's Ambush or Senni Vek Restoration).

---
### 3.115 Ixgil the Bith

- **Author:** Crimson Knight
- **Download:** [Mod](https://deadlystream.com/files/file/2108-ixgil-the-bith/)
- **Method:** TSLPatcher
---
### 3.116 Hidden Bek Control Room

- **Author:** N-DReW25
- **Download:** [Mod](https://deadlystream.com/files/file/908-hidden-bek-control-room-restoration/)
- **Method:** Loose-file
---
### 3.117 Swoop Bike Upgrades

- **Author:** Salk
- **Download:** [Mod](https://deadlystream.com/files/file/2473-kotor-swoop-bike-upgrades/)
- **Method:** TSLPatcher
---
### 3.118 Jedi Choice Dialogue Enhancement

- **Author:** Emperor Devon
- **Download:** [Mod](https://deadlystream.com/files/file/2428-jedi-choice-dialogue-enhancement/)
- **Method:** Loose-file\
**Installation instructions:** Move "dan13_dorak.dlg" only.

---
### 3.119 Juhani Restoration

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2173-juhani-dialogue-restoration/)
- **Method:** Loose-file
---
### 3.120 Vision Enhancement

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1402-jcs-vision-enhancement-for-k1/)
- **Method:** TSLPatcher
---
### 3.121 New Leviathan Dialogue

- **Author:** Revanator
- **Download:** [Mod](http://deadlystream.com/files/file/895-leviathan-differentiated-dialogue/)
- **Method:** Loose-file
---
### 3.122 Balanced Pazaak

- **Author:** A Future Pilot
- **Download:** [Mod](https://deadlystream.com/files/file/1270-balanced-pazaak/)
- **Method:** Loose-file
---
### 3.123 Camera Replacement

- **Author:** LDR
- **Download:** [Mod](http://deadlystream.com/files/file/827-ebon-hawk-camera-replacement/)
- **Method:** Loose-file
---
### 3.124 Rebalanced Grenades

- **Author:** Timbo
- **Download:** [Mod](https://deadlystream.com/files/file/2522-rebalanced-grenades/)
- **Method:** HoloPatcher
---
### 3.125 HD Grenades & Mines

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2409-grenades-and-mines-hd/)
- **Method:** Loose-file\
**Installation instructions:** Delete "ii_trapkit_001.tga" through "ii_trapkit_004.tga" before installing.

---
### 3.126 Turret Minigame Remover

- **Author:** KittyKitty
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/90)
- **Method:** Loose-file
---
### 3.127 Tutorial Remover

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2184-trask-ulgo-without-tutorials/)
- **Method:** TSLPatcher
---
### 3.128 ~~Leviathan Prison Break~~

- **Author:** Darth Parametric
- **Download:** [Mod](https://deadlystream.com/files/file/2097-all-hands-on-deck-for-the-leviathan-prison-break/)
- **Method:** TSLPatcher\
**Installation instructions:** ~~The optional file included in the install is compatible with the builds, and it's your choice to use it or not.~~ Avoid unless you can figure out this bug: [5.8 Camera Placement Bug](#58-camera-placement-bug)

---
### 3.129 Ain't No Air in Space

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2281-jcs-leviathan-aint-no-air-in-space-for-k1/)
- **Method:** TSLPatcher
---
### 3.130 Party Conversations on the Ebon Hawk

- **Author:** WildKarrde
- **Download:** [Mod](https://deadlystream.com/files/file/2284-party-conversations-on-ebon-hawk/)
- **Method:** TSLPatcher\
**Installation instructions:** Use the K1CP compatible install option, if using the K1CP (you should be).

---
### 3.131 Mission to Sleheyron

- **Author:** SAO1138
- **Download:** [Mod](https://deadlystream.com/files/file/2754-mission-to-sleheyron-a-new-story-expansion-mod-for-kotor/)
- **Method:** HoloPatcher\
**Installation instructions:** **THIS MOD IS NOT PART OF NEOCITIES AND MAY CAUSE PROBLEMS** If you are just following this guide for a stable Switch build, skip this mod for the time being.

I'm testing installing the it here. It's kind of random, but FTD said to install it after [3.128 ~~Leviathan Prison Break~~](#3128-leviathan-prison-break), but that mod doesn't work on the Switch. If I get it to work at some point then I don't have to move this one

So going off of what FTD says, I'm installing the main mod, and then installing these compatches in this order: K1CP Comp Patch, JC's K2 Robes Comp Patch, Animated Neon Cantina Signs

---
### 3.132 Dark Sacrifice

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2225-jcs-romance-enhancement-dark-sacrifice-for-k1/)
- **Method:** TSLPatcher
---
### 3.133 Saber Throw Knockdown

- **Author:** uwadmin12
- **Download:** [Mod](https://deadlystream.com/files/file/1487-k1-saber-throw-knockdown-effect/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.134 Sunry Enhancement

- **Author:** FallenGuardian
- **Download:** [Mod](http://deadlystream.com/files/file/324-sunry-murder-recording-ehancement/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.135 Davik Slave Change

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2214-pc-dialogue-with-daviks-slaves-change/)
- **Method:** TSLPatcher\
**Installation instructions:** I personally recommend option 2.

---
### 3.136 Taris Rapid Transit

- **Author:** CaptainSpoque
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1666)
- **Method:** TSLPatcher\
**Download instructions:** Full or Light version is your choice.\
---
### 3.137 Manaan Rapid Transit

- **Author:** The_Chaser_One
- **Download:** [Mod](https://deadlystream.com/files/file/2739-manaan-fast-travel-system/)
- **Method:** HoloPatcher\
**Download instructions:** If wishing to use a non-English mod version, download the mod version which matches your language of choice.\
---
### 3.138 Recruit T3-M4 Early

- **Author:** brents742
- **Download:** [Mod](https://deadlystream.com/files/file/1868-recruit-t3-m4-early/)
- **Method:** Loose-file
---
### 3.139 Security Spikes for K1

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1439-jcs-security-spikes-for-k1/)
- **Method:** TSLPatcher
---
### 3.140 HQ Blasters

- **Author:** Sithspecter
- **Download:** [Mod](http://deadlystream.com/files/file/861-high-quality-blasters/)
- **Method:** TSLPatcher\
**Installation instructions:** Extract the mod, navigate to the 'TSLPatchdata' folder, and delete the file 'keblastore.utm'. Run the installer—it will give you a single error, this is intended. After the install has completed, rename the files 'w_ionrfl_04.mdl' and 'w_ionrfl_04.mdx' to 'w_ionrfl_004.mdl' and 'w_ionrfl_004.mdx'. Delete the following files from your override directory: w_rptnblstr_004.mdl, w_rptnblstr_004.mdx, w_blstrpstl_006.mdl, w_blstrpstl_006.mdx and g1_w_rptnblstr01.uti

---
### 3.141 Crashed Republic Cruiser

- **Author:** LDR
- **Download:** [Mod](https://deadlystream.com/files/file/1878-a-crashed-republic-cruiser-on-a-nameless-world/)
- **Method:** TSLPatcher\
**Installation instructions:** Run the installer to install the mod, then re-run it twice more, once for each of the optional installs, if using Loadscreens in Color/HQ Blasters.

---
### 3.142 Trandoshans Rescaled

- **Author:** DarthParametric
- **Download:** [Mod](http://deadlystream.com/files/file/947-trandoshans-rescaled-for-k1/)
- **Method:** TSLPatcher
---
### 3.143 Custom Selkath Animation

- **Author:** Alvar007
- **Download:** [Mod](https://deadlystream.com/files/file/1555-custom-selkath-animation/)
- **Method:** TSLPatcher
---
### 3.144 Bastila Has TSL Battle Meditation

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2379-bastila-has-tsl-battle-meditation/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.145 Sneak Attack Restoration

- **Author:** N-DReW25
- **Download:** [Mod](http://deadlystream.com/files/file/1124-sneak-attack-10-restoration/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.146 Sentinel Sneak Attack

- **Author:** darthbdaman
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1710)
- **Method:** HoloPatcher
---
### 3.147 Thematic The One

- **Author:** Sniggles & JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2467-thematic-the-one/)
- **Method:** TSLPatcher
---
### 3.148 Sherruk with Lightsabers & Patch

- **Author:** Shem, patch by A Future Pilot & Darth Parametric
- **Download:** [Mod](http://deadlystream.com/files/file/693-sherruk-attacks-with-lightsabers/) [Patch](https://mega.nz/#!QNImBQSb!OPon0ZYbakcZpxZKMxSp559ezQWFU-wNXJ7Sj3ERBg4)
- **Method:** TSLPatcher, Loose-File Patch\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection). Install the base mod first, then move the file from the patch directly to your override.

---
### 3.149 Improved Cantina Sitters

- **Author:** Alvar007
- **Download:** [Mod](https://deadlystream.com/files/file/2792-improved-cantina-sitters/)
- **Method:** TSLPatcher
---
### 3.150 Helena Shan Improvement

- **Author:** VarsityPuppet
- **Download:** [Mod](https://deadlystream.com/files/file/1218-helena-shan-improvement/)
- **Method:** TSLPatcher
---
### 3.151 Bastila's Dark Bodysuit

- **Author:** Revanator
- **Download:** [Mod](https://deadlystream.com/files/file/1006-bastilas-dark-bodysuit-by-quanon-revanator/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection). Use the regular install—other install variants have been linked to sequence breaks, but the normal install variant is fully functional. After installing, delete `P_BastilaBB02.mdl` and `.mdx` from override, see [5.3 Model Problems](#53-model-problems)

---
### 3.152 Dueling Arena Adjustment

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1404-taris-dueling-arena-adjustment/)
- **Method:** TSLPatcher
---
### 3.153 Bendak Non-Darkside Option

- **Author:** Thrak Farelle, edited by A Future Pilot
- **Download:** [Mod](https://drive.google.com/file/d/1NuewBFq390wkZuBkbJzN-mN4sIRlvXGd/view)
- **Method:** Loose-file\
**Installation instructions:** This mod is not a file archive unlike all the other mods you've downloaded, just a single pre-extracted file. When you get the file, just put it directly in your Override folder.

---
### 3.154 Kashyyyk Forcefield Rework

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1427-control-panel-for-kashyyyk-shadowlands-forcefield/)
- **Method:** TSLPatcher
---
### 3.155 Swoop Platform Repair

- **Author:** CaptainSpoque
- **Download:** [Mod](https://deadlystream.com/files/file/2723-k1-swoop-platform-model-repairs/)
- **Method:** HoloPatcher\
**Installation instructions:** Which of the three versions is used is up to your preference. Full is the entire package, lite is without the player swoop displayed on the race platform, and ultra lite is without the doors fix.

---
### 3.156 Engine Lab Bench

- **Author:** Darth Parametric
- **Download:** [Mod](https://deadlystream.com/files/file/1747-black-vulkar-base-engine-lab-bench-for-swoop-accelerator/)
- **Method:** TSLPatcher
---
### 3.157 Missing Lamps Fix

- **Author:** Ebmar
- **Download:** [Mod](https://deadlystream.com/files/file/1545-k1-temple-main-floor-missing-lamps-fix/)
- **Method:** Multi-Run TSLPatcher\
**Installation instructions:** If you have installed the K1CP, install just the pillar facing fix. The lighting fix is already included in the K1CP.

---
### 3.158 Czerka Business Attire

- **Author:** JCarter426, HD Ithorian patch by Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/2309-jcs-czerka-business-attire-for-k1/)
- **Method:** TSLPatcher\
**Installation instructions:** If using Dark Hope's HD Ithorian texture, also download and apply [this patch](https://mega.nz/file/wUYRUTAD#tE7J08QTc0NSSbG-Xu3cSFsynLVtg7J59BruxOlDnKY), which Sith Holocron was kind enough to make at my request, after installing this mod.

---
### 3.159 Sith Texture Restoration

- **Author:** A Future Pilot
- **Download:** [Mod](https://deadlystream.com/files/file/1289-sith-soldier-texture-restoration/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection), `Main/changes.ini`

---
### 3.160 Diversified Republic Soldiers

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1179-diversified-wounded-republic-soldiers-on-taris/)
- **Method:** TSLPatcher
---
### 3.161 Diversified Jedi Captives

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1199-diversified-jedi-captives-on-the-star-forge/)
- **Method:** TSLPatcher\
**Download instructions:** I recommend the Base install option. If you wish to add these NPCs to Dantooine, you can also install the optional module; just make sure to add the compatibility patch if you're using 'Cloaked Jedi Robes' above.\
---
### 3.162 Juhani Romance Enhancement

- **Author:** Kexikus
- **Download:** [Mod](https://deadlystream.com/files/file/772-juhani-romance-enhancement/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.163 Dodonna's Transmission

- **Author:** danil-ch
- **Download:** [Mod](https://deadlystream.com/files/file/1101-dodonna%27s-transmission/)
- **Method:** TSLPatcher\
**Installation instructions:** Recommend the Revisited option.

---
### 3.164 ~~Endgame Hologram Fix~~

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1342-movie-style-holograms-for-end-game-cutscenes/)
- **Method:** TSLPatcher\
**Installation instructions:** Crashes, probably related to problem this mod has on Mac/Linux

---
### 3.165 Twisted Rancor Trio Fix

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1736-movie-style-holograms-for-twisted-rancor-trio-puzzle/)
- **Method:** TSLPatcher
---
### 3.166 Rakatan Hologram Fix

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1346-movie-style-rakatan-holograms/)
- **Method:** TSLPatcher
---
### 3.167 Ending Enhancement

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1958-dark-side-ending-cutscene-enhancement/)
- **Method:** TSLPatcher
---
### 3.168 Elder Droid Unique VO

- **Author:** ebmar
- **Download:** [Mod](https://deadlystream.com/files/file/1531-k1-legends-elder-droids-unique-vo/)
- **Method:** TSLPatcher
---
### 3.169 Ajunta Pall's Swords

- **Author:** Rece
- **Download:** [Mod](http://deadlystream.com/files/file/541-ajunta-palls-swords-revamped/)
- **Method:** TSLPatcher\
**Installation instructions:** Use the version not for the Weapon Model Overhaul, unless you choose to install it separately (NOT tested and NOT recommended).

---
### 3.170 Ajunta Pall's Blade

- **Author:** Ebmar
- **Download:** [Mod](https://deadlystream.com/files/file/1338-k1-legends-ajunta-palls-blade/)
- **Method:** TSLPatcher\
**Installation instructions:** Install the VarsityPuppet/Rece compatibility option if using Ajunta Pall's Swords.

---
### 3.171 JC's Mandalorian Armor

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1454-jcs-mandalorian-armor-for-k1/)
- **Method:** Multi-Run TSLPatcher\
**Installation instructions:** Install Option A. I recommend NOT re-running the patcher to install the extra textures, as upscaled textures installed in UCO are much higher-quality than these.

---
### 3.172 Multifire & Autofire

- **Author:** darthbdaman
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1711)
- **Method:** HoloPatcher\
**Installation instructions:** Run the patcher and select your desired install. I personally would recommend using at least one of the first three, as the mod is not worth it for just the feat changes in my opinion. My personal recommendation would be option 2 or 3 (especially if intending to use JC's Blaster Adjustment below), but I tested it with option 1 and did not find it terribly overpowered. Indeed, it made the game way harder at points as enemies were beaming me with multiple rifle attacks, so if you want an extra challenge option 1 is a valid choice.

---
### 3.173 Blaster Adjustment

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2827-jcs-blaster-adjustment-for-k1/)
- **Method:** TSLPatcher\
**Installation instructions:** If you installed the main option of Multifire and Autofire, I recommend using the Blaster Pistol + Critical option of this mod, as applying its changes to repeaters and rifles would make them insanely overpowered with their auto-attacks. If using Options 2 or 3 of Multifire and Autofire, I would recommend the Blaster Pistol & Blaster Rifle + Critical version of this mod--don't worry, it won't make rifles way stronger; JC's changes to the damage will overwrite bdaman's, in effect just adding JC's alterations to the critical strike ranges. Finally, if not using bdaman's mod, I recommend the full install.

---
### 3.174 HQ Gaffi Stick

- **Author:** Fallen Guardian
- **Download:** [Mod](http://deadlystream.com/files/file/312-gaffi-stick-improvement/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.175 HD Quarterstaffs

- **Author:** DeadMan, ported by N-DReW25
- **Download:** [Mod](https://deadlystream.com/files/file/2231-quarterstaff-replacement-pack-for-k1/)
- **Method:** Loose-file
---
### 3.176 Training Lightsabers

- **Author:** Kexikus
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/66/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.177 Logical Datapads

- **Author:** Sdub
- **Download:** [Mod](https://deadlystream.com/files/file/2008-logical-datapads/)
- **Method:** TSLPatcher
---
### 3.178 Realistic Visual Effects

- **Author:** Shem
- **Download:** [Mod](http://deadlystream.com/files/file/681-realistic-visual-effects/)
- **Method:** TSLPatcher
---
### 3.179 Minor Music Tweaks

- **Author:** Crimson Knight
- **Download:** [Mod](https://deadlystream.com/files/file/2321-minor-music-tweaks/)
- **Method:** TSLPatcher
---
### 3.180 NPC Alignment Fix

- **Author:** TK-664
- **Download:** [Mod](https://deadlystream.com/files/file/1866-npc-alignment-fix/)
- **Method:** TSLPatcher\
**Installation instructions:** [2.1.2 TSLPatcher automatic installation detection](#212-tslpatcher-automatic-installation-detection)

---
### 3.181 Repair Affects Stun Droid

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2502-repair-affects-stun-droid-k1/)
- **Method:** TSLPatcher
---
### 3.182 Alignment Affects Force Powers

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2759-alignment-affects-force-powers-k1/)
- **Method:** TSLPatcher\
**Installation instructions:** Ignore the Patch folder unless using K2 Force Powers for K1 (untested, but should function). I strongly recommend the combined install of "Alignment Affects Force Powers + Treat Injury Affects Force Healing."

---
### 3.183 Galaxy Map Fix

- **Author:** Kexikus & Sith Holocron
- **Download:** [Mod](http://deadlystream.com/files/file/1068-k1-galaxy-map-fix-pack/)
- **Method:** TSLPatcher
---
### 3.184 Remove Duplicate TGA/TPC

- **Author:** Flachzangen, Malacand for the .sh script
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1384) [Mod](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/scripts/k1/tpc-deduper.sh)
- **Method:** .bat Patcher, .sh script\
**Installation instructions:** For Windows: Place DelDuplicateTGA-TPC in your main game folder (NOT override!), run it, say that TPC should be deleted and do not manually confirm. If you are on a Mac or other device that cannot run .bat files, you can also try downloading the [3C-FD tool](https://github.com/J0-o/3C-FD-Patcher) to identify the duplicates. If you aren't comfortable with downloading C3-FD, a list of all the files you will need to manually delete can be found [here](/modding/mod_builds/k1/delete). MAKE SURE THIS SCRIPT RUNS PROPERLY! On some operating systems, overzealous antivirus setups, or filepaths with particular characters in them it may fail. If the file outputs "Finished, Press any key to continue" but does not list any files it deleted, it is not working, and if it does not work it will crash your game. You can try to resolve this by moving your Override folder to a different location (I recommend a subfolder in your Documents or Downloads directories), putting the .bat file there and running it through that directory, but if that doesn't work you will need to manually go through and delete the duplicates from the link above. For Linux/Mac: Download the script from the linked GitHub page. For Mac, it can be run with the "zsh" command. The script does assume you're using the default installation path for the Steam version; if you aren't, you just need to change the GAMEDIR variable at the top of the script to point to your game folder (NOT your override folder) before you run it. You may have to run the script twice, if a given TPC file has BOTH a matching TGA file and a matching DDS file.

---
### 3.185 Ultimate Character Overhaul Patches

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1282?tab=files)
- **Method:** Loose-file\
**Download instructions:** Skip the compatch for Better Twi'lek Male Heads if you chose to use Leilukin's Male Twi'lek NPC Diversity.\
**Installation instructions:** Scroll down to the "optional files" section of the mod page. In order, install the compatch for JC's Minor Fixes (delete N_CommM02 - N_CommM08 from the Aesthetics Improvements folder before moving to override, if using Dark Hope's male clothing upscale), the K1CP (delete "PLC_SSldCrps.tpc". Additionally delete N_CommM01 - 06, plus N_CommM08, if using Dark Hope's male clothing upscale, both before moving to override), and then all remaining content that matches content you chose to use from the builds (skipping Better Twi'lek Male Heads, if using Leilukin's male Twi'lek mod, as well as skipping the compatch for Republic Soldier's New Shade). I also recommend against using the patch for JC's Mandalorian Armor, as there are better options (in my opinion) in Character Textures & Model Fixes below. If using Thigh-High Boots for Twi'lek, move both the files within the NPC Replacement folder but exclude the files in the Optional folder therein.

---
### 3.186 Republic Soldier Fix

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1180-jcs-republic-soldier-fix-for-k1/)
- **Method:** Loose-file\
**Installation instructions:** Move the files from the mod's Override folder to your game's override folder. For compatibility, you will need to only install the player clothing texture replacement for Soldier-class characters: move all files beginning "PFBBL" and "PMBBL" from the mod's Player Clothing folder to your override.

---
### 3.187 Republic Soldier's New Shade

- **Author:** ebmar
- **Download:** [Mod](https://deadlystream.com/files/file/1365-k1-republic-soldiers-new-shade/)
- **Method:** Multi-Run TSLPatcher\
**Installation instructions:** If using both components of JC's Republic Soldier Fix mod (the override files & the player replacement for the soldier characters), install Options 3 and 5; if using only the main component of JC's mod, install only Option 5; if not using JC's mod, install the Main file and Option 2.

---
### 3.188 Character Textures & Model Fixes

- **Author:** Redrob41
- **Download:** [Mod](https://deadlystream.com/files/file/2659-4x-upscale-character-textures-model-fixes/)
- **Method:** Loose-file\
**Download instructions:** 2x `.tpc`\
**Installation instructions:** If you are on a system which can run .bat files, I strongly recommend using the automated system to deal with compatibility for this mod. To do so, first extract redrob's mod from its archive, then go to [this page](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/scripts/cleaner.bat) and click on the button with the arrow pointing down at the top of the code list (the one which says "download raw file"). Place cleaner.bat in the folder from redrob's mod called "Copy contents to KotOR's Override folder", then go to [here](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/scripts/cleanlist_k1.txt) and repeat the same step, placing cleanlist_k1.txt in the same location. You can now run cleanlist.bat: follow the instructions onscreen, selecting whether you did or didn't use any of the given mods (note that the first thing it will ask you is whether you've installed "Mandatory Deletions"; rather than a mod, this is a required step to delete files that need to be removed regardless of what mods you're using, so just approve it). The batch file will automatically delete the incompatible files based on which mods you select that you've used in your install. Once you reach the end of the list, you can exit the .bat window, delete cleaner.bat and cleanlist_k1.txt, and then move the remaining files in the folder to your override. If you cannot run .bat files or feel uncomfortable running this file, you will need to manually delete the files yourself, following the instructions [here](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/content/k1/redrob_deletions.md).

---
### 3.189 ~~4GB Patcher~~

- **Author:** Daniel Pistelli
- **Download:** [Mod](https://ntcore.com/?page_id=371)
- **Method:** Executable\
**Installation instructions:** There is no `.exe` to patch lol

---
### 3.190 Turret Cockpit Widescreen

- **Author:** MadDerp
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1211)
- **Method:** Loose-file
---
### 3.191 ~~HR Menus~~

- **Author:** ndix UR
- **Download:** [Mod](https://deadlystream.com/files/file/1159-kotor-high-resolution-menus/?tab=comments)
- **Method:** .bat Patcher with Loose-File Components\
**Installation instructions:** The Switch version Fixes a lot of widescreen things

---
### 3.192 ~~HD UI Menu Pack~~

- **Author:** ndix UR
- **Download:** [Mod](https://deadlystream.com/files/file/1226-hd-ui-menu-pack/)
- **Method:** Loose-file\
**Installation instructions:** The buttons don't quite line up on most of these. lbl_abi_cost and lbl_align are okay though.

---
### 3.193 Workbench Camera Tweak

- **Author:** Darth Parametric
- **Download:** [Mod](https://deadlystream.com/files/file/1742-workbench-upgrade-screen-camera-tweak-for-k1/)
- **Method:** Loose-file
---
### 3.194 Pretty Good! Icons

- **Author:** ajdrenter
- **Download:** [Mod](https://deadlystream.com/files/file/1815-pretty-good-icons-for-kotor/)
- **Method:** Loose-file\
**Installation instructions:** I recommend using the .tpc file option. For THIS MOD ONLY, do not overwrite when prompted!

---
### 3.195 Robe Icons for JC's Cloaked Robes

- **Author:** Nehua
- **Download:** [Mod](https://deadlystream.com/files/file/2303-hd-robe-icons-for-jcs-cloaked-jedis-and-effixs-extra-robes/)
- **Method:** Loose-file\
**Installation instructions:** In the "JC's Cloaked Jedis" folder, select the files from the version of JC's Cloaked Jedi Robes you utilized. Ignore the Effix folder unless playing with that specific mod.

---
### 3.196 Upscaled Computer

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2025-upscaled-computer/)
- **Method:** Loose-file
---
### 3.197 ~~Widescreen Fade Fix~~

- **Author:** Doiinko
- **Download:** [Mod](https://deadlystream.com/files/file/1792-kotor-widescreen-fade-fix/)
- **Method:** Loose-file\
**Installation instructions:** The Switch version Fixes a lot of widescreen things

---
### 3.198 ~~Main Menu Widescreen Fix~~

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1173-k1-main-menu-widescreen-fix/)
- **Method:** Loose-file\
**Installation instructions:** The Switch version Fixes a lot of widescreen things

---
### 3.199 ~~Cutscenes Rescaled~~

- **Author:** Pops Maellard
- **Download:** [Mod](https://deadlystream.com/files/file/2380-k1-cutscenes-rescaled/)
- **Method:** Loose-file\
**Installation instructions:** The Switch version has 720p upscaled versions of the cutscenes already. I tried adding the 1080p versions, but the audio becomes choppy. Just skip these

---
### 3.200 ~~Remastered Cutscenes~~

- **Author:** naelavok
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1306)
- **Method:** Loose-file\
**Installation instructions:** The Switch version has 720p upscaled versions of the cutscenes already. I tried adding the 1080p versions, but the audio becomes choppy. Just skip these

---
### 3.201 IPS Patches

- **Author:** VeSeeker
- **Download:** [Mod](https://github.com/VeSeeker/switch-kpm-ips-patches)
- **Method:** Loose-file\
**Installation instructions:** These are executable patches for the Switch, based on the [KPM](https://github.com/LaneDibello/Kotor-Patch-Manager) patches. You are free to pick and choose which patches you want to use. At a minimum, I strongly suggest using `AnimatedTextureFix`. I haven't finished porting many patches to the Switch as of yet, I will update this guide when I have ported all of them. To install a patch, you will move the patch **folder** to `atmosphere/exefs_patches/<patchName>/<BID>.ips` on your Switch. Do not put patches into override, or anywhere in `K1romfs`, it will not do anything.

---
## 4 Finalizing

### 4.1 Finishing Up

Run `ksmt finalize 1`. **Add responses to each YesNo prompt**.
This should leave you with the folder `kotor-switch-modding-tool/0100854015868000`. Connect your Switch (or sd card) to your computer and navigate to `atmosphere/contents`. If there is already a `0100854015868000` folder, delete it, and then move the finalized `0100854015868000` from the modding tool. The file structure should be: `atmophere/contents/0100854015868000/`.

Don't forget to move IPS patches to `atmosphere/exefs_patches/`!

### 4.2 Final Thoughts

Be aware that adding these mods increases load times by a bit. It's not unbearable, but it is noticeable.

I'm pretty happy with this build. I'll continue to update it as I make more IPS patches. I'll also try to keep it up to date with neocites.

## 5 Bugs, Issues, & Extras

### 5.1 Out of VRAM

When you have too many high quality textures, the Switch runs out of the VRAM pool of it's unified memory. Most commonly, this results in a crash during a loading screen. Rarely, you will be in an area, and new textures that would load in are invisible, and then you crash. The solution is just to downscale some of the textures. We end up getting pretty close to the limit in some modules.

#### 5.1.1 Extra Downscales

Below is a list of models where I crashed, so I picked a few textures in that module to downscale. These are all downscaled automatically by my modding tool, so the lists below are mostly just for my reference. If you run out of VRAM in a module, let me know so I can add it to the list.

##### 5.1.1.1 Lower city apartments

Consistent crash. Downscaling: LTS_lotrim01, 02, 04, 09, 10, LTS_loflr05

##### 5.1.1.2 Anchorhead

Inconsistent crashes. Downscaling: LTA_FLalpha, LTA_flr01a, LTA_flr01, LTA_sail02, LTA_sand01, LTA_wall00, LTA_wll01, LTA_wll01_00a

##### 5.1.1.3 Matale Grounds -> Return to Ebon Hawk

Inconsistent crash. Downscaling: LDA_bark04, LDA_flr01

##### 5.1.1.4 Exiting Ebon Hawk on Yavin

Inconsistent crash. Downscaling: LYV_wall03, 04, 05, 08, 09

##### 5.1.1.5 Temple Exterior on Unknown World

Inconsistent crash. Downscaling: LUN_grss02, LUN_wll01, 02

### 5.2 Texture Outlines

Some textures have weird either white outlines as with the Dantooine leaf textures, or alpha outline problems, as with damage decals on the sand crawler in the Dune Sea, and many others.

Many of these problems have actually been reported as bugs on nexus mods, and the mod creator said that they fixed them, so I really don’t know why the Switch still experiences the problem.

Reading the bug reports, some people have seemingly fixed these on their own by downloading the .tga version and converting the suspect files to .tpc themselves. Something about batch converting messing with the type of compression used. You are welcome to try this, but I couldn’t get it to work.

### 5.3 Model Problems

Some modded models cause problems in the game. For example, [3.50 ~~Juhani Appearance Overhaul & Patch~~](#350-juhani-appearance-overhaul--patch) makes Juhani completely gone from the grove. The cutscene tries to play but there is nothing there so it just gets stuck. If you delete S_JuhMod01.mdl, then her model is all messed up but she is actually there and the cutscene can play.

[3.151 Bastila's Dark Bodysuit](#3151-bastilas-dark-bodysuit) adds some model files, one of which crashes the game only in the final cutscene of the darkside ending. I suspect this has to do with an animation that only plays during that cutscene, but I’m really not sure. I don’t know much about models in this game, so someone smarter than me will have to figure this out.

### 5.4 Flickering Textures

Sometimes models flicker wildly. This is because the modded textures are arrays of images the game is supposed to cycle through (also known as an animated texture). This works for tons of basegame and modded textures, but for whatever reason the game doesn’t like a few specific ones, so my solution is just to take the first frame of the cycle and set that as the texture. I do this automatically for the modded textures where this is a problem with the modding tool. (This change affects these mods: [3.58 HD Sign Placeable](#358-hd-sign-placeable), [3.59 HD Kiosk & Patch](#359-hd-kiosk--patch), [3.60 HD Desk](#360-hd-desk), [3.103 Terminal Texture](#3103-terminal-texture), [3.104 HD Workbench](#3104-hd-workbench)). Kind of sucks because the textures are no longer animated, but neither were the basegame ones, so now at least we have upscaled versions.

### 5.5 Animated Texture Problem

On the Switch, animated textures aren't, well, animated. Some are never animated, and some are only animated if you are sufficiently far away from them. There are two reasons for this problem:

#### 5.5.1 Missing .txi

The first is simply that the modded animated textures come as .tga files without .txis. I’m guessing on the PC version, the original animated textures are in .tga and have a .txi in the basegame files, so modders didn’t need to include the .txi and it still works. We need the .txi files though because we have to convert them to .tpc. I fixed this by getting the .tpc from the dumped Switch game files and providing the .txi files in patches.

#### 5.5.2 Mipmap 0 Animation

The second problem was very annoying to figure out. Basically, the highest quality mipmap level is not animated on the Switch. So if a texture's mipmap was set to 0, then it was always static, and if it was set to 1, it was animated until you got close enough to it, and then it would be come static. [Here](https://youtu.be/CmlEmN5rivw) is a video showing this.

Thankfully, the AnimatedTextureFix in [3.201 IPS Patches](#3201-ips-patches) fixes this, so animated textures work exactly the same as the do on PC.

### 5.6 Garbled Icons & Textures

Some of the mods provide updated icons for items in the game. If those images aren't a power of 2 resolution (64x64, 128x128, etc.), they end up looking weird and garbled. The fix is to resize them to be a power of 2 resolution. This is done automatically with the modding tool.

![Garbled screenshot](https://github.com/VeSeeker/kotor-switch-modding-tool/Screenshots/K1_Garbled.png)

### 5.7 Reflective Lightsaber Problem

This is specific to [3.107 ~~Reflective Lightsaber Blades~~](#3107-reflective-lightsaber-blades) and [3.108 ~~Darth Malak's Lightsaber~~](#3108-darth-malaks-lightsaber). For some reason, some, but not all of the lightsabers have these weird flat lines coming off of the sides of them.

![Reflective screenshot](https://github.com/VeSeeker/kotor-switch-modding-tool/Screenshots/K1_Reflective.png)

Again it's not all lightsabers so I really don't know what's going on, somebody smarter than me is needed to fix this cause I don't understand how this mod works well enough to fix it.

### 5.8 Camera Placement Bug

Sometimes the camera bugs out during conversations / in-engine cutscenes. It'll either be blocked by something, or be completely black (this might just be the camera being blocked by a black textures). This happens on Carth's last transmission on the Endar Spire (very short). It also happens for the whole conversation on the Leviathan where Saul tortures Carth, as well as for cameras seen through computer terminals on the Leviathan if you use [3.128 ~~Leviathan Prison Break~~](#3128-leviathan-prison-break). Not sure what's going on here.

Also happens on the Korriban start map reveal scene. You spend like 15 seconds looking at a close up of some brown rock. I don't think any mod affects this, so I suspect it is a base game bug. I'm planning on looking into fixing this at some point. If I can, then I'll also try to fix the aforementioned Leviathan issues.
