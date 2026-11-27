# Kotor 1 Switch Modding Guide
#### By VeSeeker

## 1 Introduction
#### You don't have to read this, but you may have questions if you don't

This guide is based on the neocities [KOTOR 1 Full Build for PC](https://kotor.neocities.org/modding/mod_builds/k1/full).

Some modules get extremely close to the VRAM limit, so follow this guide closely. See [4.1 Out of VRAM](#41-out-of-vram).

## 2 Setup
#### You really do need to read this part

This is the setup section.

### 2.1 Tools

This is the tools body

#### 2.1.1 Kotor Switch Modding Tool

I made this cool tool

#### 2.1.2 Fixing TSLPatcher automatic installation detection

Fix that tool

## 3 Mods

### 3.1 Switch Texture Restoration

- **Author:** jacqylfrost
- **Download:** [Mod](https://deadlystream.com/files/file/2103-kotor-switch-texture-restoration)
- **Method:** Loose-file\
**Installation instructions:** Extract the texture files into override, not a subfolder

---
### 3.2 Character Startup Changes & Patch

- **Author:** jonathan7, patch by A Future Pilot
- **Download:** [Mod](http://deadlystream.com/files/file/349-character-start-up-change/) [Patch](https://mega.nz/file/sRw1GBIK#J8znLBwR6t7ZvZnpQbsUBYcUNfPCWA7wYNW3qU6gZSg)
- **Method:** TSLPatcher, Loose-file\
**Installation instructions:** Run TSLPatcher first, then copy the loose files into override.

---
### 3.3 4GB Patcher

- **Author:** Daniel Pistelli
- **Download:** [Patch](https://ntcore.com/?page_id=371)
- **Method:** Executable\
**Installation instructions:** This step should only be performed if you are NOT on the Aspyr patch and have not applied J's 3C-FD patcher! 3C-FD applies this as part of its fixes to the Aspyr version. Just like 3C-FD, since the Mac Appstore version is not an executable, this program cannot be utilized on the Mac Appstore edition of the game.

---
### 3.4 TSLRCM

- **Author:** zbyl2, DarthStoney, Hassat Hunter & VarsityPuppet
- **Download:** [Mod](https://deadlystream.com/files/file/578-tsl-restored-content-mod/)
- **Method:** Executable\
---
### 3.5 TSLRCM Tweak Pack

- **Author:** Pavijan (update by Fair Strides)
- **Download:** [Mod](http://deadlystream.com/files/file/296-unofficial-tslrcm-tweak-pack/)
- **Method:** Multi-Run TSLPatcher\
**Installation instructions:** Don't use the complete installer, instead selecting the individual component installer—this is critical for compatibility, not just to choose specific options. The installer for this mod will need to be run 6 times, once to install each of the options we'll be using: Kaevee Removal Parts 1 & 2, Saedhe's Head, Kreia-Atris Dialogue Tweak, Trayus Mandalore Conversation, and Trayus Sith Lord Masks. Most of the other options for this mod are untested with the mod builds, but will likely function--I still recommend against using them, since compatibility isn't 100% guaranteed, but you can try. The one exception is Atton at the End, which is completely incompatible with one of the most important mods in this build, which is a much more comprehensive implementation of Atton's dialogue at endgame.

---
### 3.6 Silent Sion

- **Author:** Emperor Devon
- **Download:** [Mod](https://deadlystream.com/files/file/2426-silent-sion-restoration/)
- **Method:** Loose-File\
**Installation instructions:** Move just 153sion.dlg to the override.

---
### 3.7 Thematic KOTOR 2 Companions

- **Author:** Sniggles & JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2662-thematic-kotor-2-companions/)
- **Method:** TSLPatcher\
**Installation instructions:** If you would like to have Visas's class as Sith Assassin, install the "Standard + Sith Assassin Visas" option. Otherwise, simply install "Standard."

---
### 3.8 Saving Throw Fixes

- **Author:** Rovan
- **Download:** [Mod](http://deadlystream.com/files/file/828-tsl-prestige-class-saving-throw-fixes/)
- **Method:** Loose-file\
**Installation instructions:** I advise users to only install the Jedi Master/Sith Lord fixes.

---
### 3.9 Classic Class Attack

- **Author:** Crimson Knight
- **Download:** [Mod](https://deadlystream.com/files/file/2812-classic-class-attack-bonus/)
- **Method:** TSLPatcher\
**Installation instructions:** Strongly recommend downloading the standard option. Weaker Consulars can be extremely punishing, so if you choose this option be aware that you're in for a rough time at some places!

---
### 3.10 Robes with Shadows

- **Author:** PapaZinos
- **Download:** [Mod](https://deadlystream.com/files/file/2075-robes-with-shadows-for-tsl/)
- **Method:** Loose-file\
**Installation instructions:** Extract the mod. Ignore the included subfolders, and move just the files in the base folder to your override. Overwrite when prompted.

---
### 3.11 K2CP

- **Author:** Multiple; A Future Pilot, JCarter426 Curates
- **Download:** [Patch](https://deadlystream.com/files/file/1280-kotor-2-community-patch/)
- **Method:** TSLPatcher\
**Installation instructions:** Remember, warnings during an installation are normal—errors are not.

---
### 3.12 Remote Tells Influence & Patch

- **Author:** tk102, patch by Leilukin
- **Download:** [Mod](https://www.gamefront.com/games/knights-of-the-old-republic-ii/file/remote-tells-influence) [Patch](https://www.dropbox.com/s/af3h6y793f3zjxq/Remote%20Tells%20Influence%20Patch%20for%20TSLRCM.zip?dl=0)
- **Method:** Loose-file & Patch\
---
### 3.13 Better Czerka Salvager

- **Author:** OzilsEyes
- **Download:** [Mod](https://deadlystream.com/files/file/2576-fixed-better-czerka-salvager/)
- **Method:** TSLPatcher\
---
### 3.14 Ultimate HR Textures

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1100)
- **Method:** Loose-file\
**Installation instructions:** Download the .tpc variant of the mod. Delete PER_Gr01.tpc, TEL_rock.tpc through TEL_rock07.tpc, and TEL_wl05.tpc before moving the files to your override folder.

---
### 3.15 Ultimate Character Overhaul

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1060)
- **Method:** Loose-file\
**Installation instructions:** For now, ignore all patches (those will be installed later). Just download the main package, either Full or Lite based on your quality preferences (I recommend the 2x version, as the graphical differences are minimal). Just MAKE SURE they are in .tpc file format! Delete N_OndSoldMH1.tpc, PMBJ02.tpc, PMHC03.tpc, PMHC03D1.tpc, and PMHC03D2.tpc before moving to override.

---
### 3.16 Ultimate Nar Shaddaa

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1101)
- **Method:** Loose-file\
**Installation instructions:** Download the .tpc variant of the mod. Delete NAR_fl01.tpc, NAR_Met4.tpc, and NAR_wl07.tpc before moving to your Override.

---
### 3.17 Ultimate Dantooine

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1103)
- **Method:** Loose-file\
**Installation instructions:** Download the .tpc variant of the mod. Delete DAN_birds.tpc, DAN_MWFl.tpc, DAN_NEW1.tpc and DAN_wall03.tpc before moving to your Override.

---
### 3.18 Ultimate Dxun & Patch

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1105) [Patch](https://mega.nz/file/kUZTmT6K#9Ymj028VHivAoY7RaW1mKXu1H28NvYVNfM44p5C-IIM)
- **Method:** Loose-file\
**Installation instructions:** Download the .tpc variant of the mod. Delete DXN_BWa1 through DXN_BWa8.tpc before moving the files to your override folder, then apply the patch.

---
### 3.19 Ultimate Onderon

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1102)
- **Method:** Loose-file\
**Installation instructions:** Download the .tpc variant of the mod. Delete OND_dor1.tpc & OND_dor3.tpc before moving to your Override.

---
### 3.20 Ultimate Korriban

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1104)
- **Method:** Loose-file\
**Installation instructions:** Download the .tpc variant of the mod. Delete KOR_water01.tpc before moving the files to your override folder.

---
### 3.21 Ultimate Malachor

- **Author:** ShiningRedHD
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1106)
- **Method:** Loose-file\
**Installation instructions:** Download the .tpc variant of the mod. For this mod only, do not overwrite if prompted!

---
### 3.22 Korriban Sith Art

- **Author:** MessesWithWolves
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1632)
- **Method:** Loose-file\
**Download instructions:** Download and install both files.\
---
### 3.23 Ritual and Water Textures

- **Author:** Nehua
- **Download:** [Mod](https://deadlystream.com/files/file/2286-freedon-nadds-tomb-ritual-and-water-textures/)
- **Method:** Loose-file\
**Installation instructions:** Move only the files from the ritual folder, not the water.

---
### 3.24 PFHC06 Fix

- **Author:** Ferc Kast
- **Download:** [Mod](https://deadlystream.com/files/file/1442-pfhc06-fix/)
- **Method:** Loose-file\
---
### 3.25 Droid Special Weapons Fix

- **Author:** LoneWanderer
- **Download:** [Mod](https://deadlystream.com/files/file/1860-droid-special-weapons-fix-for-tsl-v10/)
- **Method:** TSLPatcher\
**Download instructions:** Use the V2 version of the mod.\
---
### 3.26 Honest Merchant

- **Author:** TK-664
- **Download:** [Mod](https://deadlystream.com/files/file/1904-honest-merchant-tslrcm/)
- **Method:** TSLPatcher\
---
### 3.27 JC's Minor Fixes

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1215-jcs-minor-fixes-for-k2/)
- **Method:** Loose-file\
**Installation instructions:** If you are using the K2 Community Patch, install the contents of every folder but Straight Fixes (that was already in the K2CP). Delete DXn_grassfx.tga and DXN_jungfx.tga in Aesthetic Improvements before moving files to override.

---
### 3.28 Maintenance Reskin

- **Author:** Malkior
- **Download:** [Mod](https://deadlystream.com/files/file/165-maintenance-officer-realistic-reskin/)
- **Method:** Loose-file\
---
### 3.29 HD Sign Placeable

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2442-plc_sign/)
- **Method:** Loose-file\
---
### 3.30 HD Kiosk & Patch

- **Author:** Dark Hope, patch by Marcus Ramikin
- **Download:** [Mod](https://deadlystream.com/files/file/2277-kiosk-hd/) [Patch](https://deadlystream.com/files/file/2910-kiosk-model-fix-for-k2/)
- **Method:** Loose-file\
**Download instructions:** Download the "Kiosk HD 15.03.2024" version.\
---
### 3.31 HD Desk

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2441-plc_desk/)
- **Method:** Loose-file\
---
### 3.32 Hires Beam Effects

- **Author:** InSidious
- **Download:** [Mod](http://deadlystream.com/files/file/221-hi-res-beam-effects/)
- **Method:** Loose-file\
---
### 3.33 Fire and Ice HD

- **Author:** Cinder Skye
- **Download:** [Mod](http://deadlystream.com/files/file/454-fire-and-ice-hd-whee/)
- **Method:** Loose-file\
---
### 3.34 Animated Energy Shields

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2193-animated-energy-shields/)
- **Method:** Loose-file\
---
### 3.35 Blaster Visual Effects

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1272-jcs-blaster-visual-effects-for-k2/)
- **Method:** Loose-file\
**Installation instructions:** Move everything from the override folder to your game's override directory, unless you would like yellow/green disruptors, in which case those files should be moved from the optional folder after moving all loose files to the override first.

---
### 3.36 Head Model Fixes

- **Author:** Redrob41
- **Download:** [Mod](http://deadlystream.com/files/file/489-tsl-head-model-fixes/)
- **Method:** Loose-file\
---
### 3.37 New Holocron Textures

- **Author:** Sith Holocron
- **Download:** [Mod](http://deadlystream.com/files/file/283-new-texture-of-holocrons-in-the-telos-secret-academy/)
- **Method:** Loose-file\
---
### 3.38 Thigh-High Boots for Twi'lek

- **Author:** DarthParametric
- **Download:** [Mod](http://deadlystream.com/files/file/1088-tsl-thigh-high-boots-for-female-twilek-body-modders-resource/)
- **Method:** Loose-file\
**Installation instructions:** Ignore the "Player Bodies" folder. Go into the NPC Replacement folder and move all the loose files to the override directory. Ignore the optional folder.

---
### 3.39 Better Twi'lek Heads

- **Author:** Ashton Scorpius
- **Download:** [Mod](https://deadlystream.com/files/file/1432-tsl-better-male-twilek-heads/)
- **Method:** HoloPatcher\
**Installation instructions:** Choose whether to use the slim or original necks; your preference.

---
### 3.40 Twi'lek Male Diversity

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2242-tsl-twilek-male-npc-diversity/)
- **Method:** HoloPatcher\
**Installation instructions:** Run the installer and install the Main Installation first. Once the main install is completed, select the optional upscaled textures install option and install it, if desired. If using the original necks option of Ashton Scorpius's Better Twi'lek Males mod, also ensure to run the "[Optional] Original Necks" install option.

---
### 3.41 Dahnis Unique Look

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2198-dahnis-unique-look/)
- **Method:** HoloPatcher\
**Installation instructions:** The use of the upscaled textures or not is your preference, though I recommend them.

---
### 3.42 Darth Malak's Armor

- **Author:** DarthParametric
- **Download:** [Mod](http://www.nexusmods.com/kotor2/mods/9/?)
- **Method:** Loose-file\
---
### 3.43 Supermodel Fix

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1141-jcs-supermodel-fix-for-k2/)
- **Method:** Loose-file\
**Installation instructions:** Move the files from the override folder to your override directory. Optionally, if you prefer the aesthetic of the K1 running animation, you can also move the files from the 'K1 Style Running' folder to your override and overwrite.

---
### 3.44 Worn-Out Mando Armor

- **Author:** LordRevan999
- **Download:** [Mod](https://mega.nz/#!1A4RCLha!Ro2GNVUPRfgot-woqh80jVaukixr-cnUmTdakuc0Ca4)
- **Method:** Loose-file\
---
### 3.45 HD NPC Portraits

- **Author:** ndix UR
- **Download:** [Mod](https://deadlystream.com/files/file/1770-hd-npc-portraits/)
- **Method:** Loose-file\
---
### 3.46 HD PC Portraits

- **Author:** ndix UR
- **Download:** [Mod](https://deadlystream.com/files/file/1769-hd-pc-portraits/)
- **Method:** Loose-file\
---
### 3.47 Stylized Portraits TSL

- **Author:** Tinman888 & Sdub
- **Download:** [Mod](https://deadlystream.com/files/file/1977-stylized-portraits-tsl-created-by-tinman888/)
- **Method:** Loose-file\
---
### 3.48 PFHC03 Restoration

- **Author:** Effix
- **Download:** [Mod](https://deadlystream.com/files/file/2003-effixians-pfhc03-restoration/)
- **Method:** TSLPatcher\
**Installation instructions:** Recommend the 'zombie-like' appearance, as it matches vanilla DS transitions.

---
### 3.49 4K Atton

- **Author:** Constar
- **Download:** [Mod](http://deadlystream.com/files/file/441-4k-atton/)
- **Method:** Loose-file\
**Download instructions:** Download the .tpc version of the mod.\
---
### 3.50 Atton with Scruff

- **Author:** felixfelicitas
- **Download:** [Mod](http://deadlystream.com/files/file/528-atton-rand-with-scruff/)
- **Method:** Loose-file\
**Installation instructions:** Ignore the MacOS folder, only move the .TGA files.

---
### 3.51 Rounder G0-T0

- **Author:** dirigibalistic
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1296)
- **Method:** Loose-file\
---
### 3.52 Dark Harbinger

- **Author:** NiuHaka
- **Download:** [Mod](https://mega.nz/#!kARxFSbS!wVaTMHT3LZ1Z2nFzjCiattphsim1p-0ReALIcb9h8pQ)
- **Method:** Loose-file\
**Installation instructions:** Choose which version of the head model you would like to use from the screenshots provided. Place the files from the corresponding folder into your override.

---
### 3.53 HD Vrook

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1504-vrook-hd-international-global-mod/)
- **Method:** Loose-file\
---
### 3.54 HD Darth Nihilus

- **Author:** Darth_Sapiens
- **Download:** [Mod](http://deadlystream.com/files/file/367-darth-sapiens-presents-hd-darth-nihilus/)
- **Method:** Loose-file\
**Download instructions:** Download and install the .tpc filetype version: it is nearly lossless, much more performant due to the smaller size, and critically fixes several issues caused by the very large texture size of the original upload.\
---
### 3.55 Darth Sion Remake

- **Author:** FF97
- **Download:** [Mod](https://deadlystream.com/files/file/1244-darth-sion-remake/)
- **Method:** Loose-file\
**Installation instructions:** Install the files within the Override folder.

---
### 3.56 Detran's Revan

- **Author:** Detran
- **Download:** [Mod](https://deadlystream.com/files/file/2350-detrans-darth-revan/#)
- **Method:** Loose-file\
---
### 3.57 Lore-Friendly Mandalore

- **Author:** constantinople33
- **Download:** [Mod](https://deadlystream.com/files/file/1848-expanded-lore-friendly-mandalores-mask-with-matching-armor-and-icons-upscaled-high-quality-textures/)
- **Method:** Loose-file\
---
### 3.58 Visas Reduced Model Clipping

- **Author:** Feeling
- **Download:** [Mod](https://deadlystream.com/files/file/2299-visas-reduced-model-clipping/)
- **Method:** Loose-file\
**Download instructions:** Either option is fine, choose which you prefer based on the screenshots.\
---
### 3.59 HD Visas Marr

- **Author:** Darth_Sapiens
- **Download:** [Mod](http://deadlystream.com/files/file/519-darth-sapiens-presents-hd-2k-visas-marr/)
- **Method:** Loose-file\
**Installation instructions:** Only move the four .dds filetype files to your override, ignore the remainder. If installing this mod alongside either the K2CP or Ultimate Character Overhaul, P_VisasBB.tpc, P_VisasH01.tpc/.tga, P_VisasHD01.tpc/.tga, and P_VisasHD02.tpc/.tga must be deleted from the override so this mod's .dds-based files will load.

---
### 3.60 Mira Unpoofed

- **Author:** Ashton Scorpius
- **Download:** [Mod](https://deadlystream.com/files/file/1733-tsl-mira-unpoofed/)
- **Method:** Loose-file\
---
### 3.61 T3M4 HD 2K

- **Author:** Darth_Sapiens
- **Download:** [Mod](http://deadlystream.com/files/file/514-darth-sapiens-presents-t3m4-hd-2k/)
- **Method:** Loose-file\
**Installation instructions:** If present in your Override, P_t3m4_01.tpc/.tga must be deleted so this mod's .dds-based files will load.

---
### 3.62 HD Astromechs

- **Author:** Darth_Sapiens and Sith Holocron
- **Download:** [Mod](http://deadlystream.com/files/file/971-refurbished-astromech-droids/)
- **Method:** Loose-file\
---
### 3.63 War Droid HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2188-war-droid-mark-i-hd/)
- **Method:** Loose-file\
---
### 3.64 HD Duros & Patch

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2252-duros-hd/) [Patch](https://mega.nz/file/RBBUTKoB#FTWDzUf8SwWBoaGgtAGXfUHjOP_BZxfFPKASf8hlC1M)
- **Method:** Loose-file\
**Installation instructions:** Before moving the files to override, make a copy of N_Duros02.tga and paste it into the same location you extracted the mod to. On a Windows OS, this should create a file called "N_Duros02 - Copy.tga". Rename this file to "N_Duros04.tga". Repeat this process with the file N_Duros03.tga, creating two copies and naming them N_Duros05.tga and N_Duros06.tga. When you move all the files to the override, you should be moving eight total. Following this, download and install the patch.

---
### 3.65 HD Ithorians

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2382-ithorian-hd/)
- **Method:** Loose-file\
**Installation instructions:** Similar to the above, make a copy of C_Ithorian03.tga and rename it to N_Chodo.tga. You should move a total of 5 files to the override.

---
### 3.66 N_oldAMH01 HD

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2806-n_oldamh01-hd/)
- **Method:** Loose-file\
---
### 3.67 Canonical Jedi Exile

- **Author:** michaelfung2000
- **Download:** [Mod](http://deadlystream.com/files/file/170-canonical-jedi-exile/)
- **Method:** Loose-file\
---
### 3.68 Lightsaber Visual Effects

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1317-jcs-lightsaber-visual-effects-for-k2/)
- **Method:** Loose-file\
**Installation instructions:** Recommend using the default without optional textures, because J's mod below uses the defaults as its base for its reflections.

---
### 3.69 Lightsaber Hilt Variety

- **Author:** J
- **Download:** [Mod](https://deadlystream.com/files/file/2794-enhanced-lightsaber-hilt-variety/)
- **Method:** Loose-file\
**Installation instructions:** If you don't like the little semi-random bronze pieces on each lightsaber hilt, move w_lghtsbr_001.tga from the alt_texture folder within the download to your override after installing the base version of the mod.

---
### 3.70 Random Panels

- **Author:** Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/2588-kotor2-random-panels/)
- **Method:** Loose-file\
---
### 3.71 Neglected Computer Panel

- **Author:** ScrierOne
- **Download:** [Mod](https://deadlystream.com/files/file/2063-neglected-computer-panel/)
- **Method:** Loose-file\
**Download instructions:** Download only the Damaged version, it contains files for both.\
---
### 3.72 Improved Peragus Asteroids

- **Author:** VasiliiZaytsev
- **Download:** [Mod](http://deadlystream.com/files/file/321-improved-peragus-asteroid-fields/)
- **Method:** Loose-file\
---
### 3.73 Swoop Monitor Replacement

- **Author:** Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/1252-tsl-swoop-monitors-replacement-pack/)
- **Method:** Loose-file\
---
### 3.74 HD Terminal Texture

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/1925-terminal-texture/)
- **Method:** Loose-file\
**Download instructions:** Which version to use is up to you; the first image on the mod page is the version of the texture from the "PLC_CompPnl(Vurt's KotOR Visual Resurgence) 2026.rar" download, the second image is the original download, and the third image is the vanilla terminal texture.\
**Installation instructions:** The files in this mod need to be duplicated and those duplicates renamed. On a Windows OS you can do this by copying the two files within and pasting them into the same folder which you copied them from. This should create duplicates of the original files with a slightly different filename (such as PLC_CompPnl-COPY). Take the two copied files and rename them to PLC_CompPnl_b, retaining their original file extensions (that means the .tga filetype file should be the larger one!). When the files are moved to the override, you should be moving four files: PLC_CompPnl.tga, PLC_CompPnl.txi, PLC_CompPnl_b.tga, and PLC_CompPnl_b.txi

---
### 3.75 Animated Computer Panel

- **Author:** ebmar
- **Download:** [Mod](https://deadlystream.com/files/file/1385-tsl-animated-computer-panel/)
- **Method:** TSLPatcher\
**Installation instructions:** Recommend solid options. Do NOT use experimental install options!

---
### 3.76 HD Workbench

- **Author:** Dark Hope
- **Download:** [Mod](https://deadlystream.com/files/file/2222-reptab-hd/)
- **Method:** Loose-file\
---
### 3.77 Backdrop Improvements

- **Author:** Kexikus
- **Download:** [Mod](http://deadlystream.com/files/file/949-tsl-backdrop-improvements/)
- **Method:** Loose-file\
**Installation instructions:** Install the files from the included Override directory only. Delete all the files beginning with "leh_". There should be four.

---
### 3.78 Citadel Station Backdrop

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1217-jcs-citadel-station-backdrop/)
- **Method:** Loose-file\
---
### 3.79 HQ Skyboxes II

- **Author:** Kexikus
- **Download:** [Mod](https://deadlystream.com/files/file/1793-high-quality-skyboxes-ii/)
- **Method:** TSLPatcher\
**Download instructions:** Download just the main file (HQSkyboxesII_TSL.7z or HQSkyboxesII_TSL_1k.7z), not any of the compatches. Whether you use the 1k version is your choice or not; on older systems, the 1k version will give better performance.\
**Installation instructions:** After this mod has finished installing, if you are using the K2CP, extract the K2CP once again—do not re-run its TSLPatcher! Open the TSLPatchdata folder and move 231teld.mdl and 231teld.mdx to your override, and overwrite when prompted.

---
### 3.80 Ebon Hawk Cockpit Upgrade I

- **Author:** Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/2258-ebon-hawk-cockpit-upgrade-leh_scre01-more-subtle-version/)
- **Method:** Loose-file\
---
### 3.81 Ebon Hawk Cockpit Upgrade II

- **Author:** Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/2247-ebon-hawk-cockpit-upgrade-leh_scre02/)
- **Method:** Loose-file\
**Installation instructions:** Recommend the version without overlays, but it's personal preference.

---
### 3.82 Spark Effect

- **Author:** PapaZinos
- **Download:** [Mod](https://deadlystream.com/files/file/2314-spark-effect-ebon-hawk/)
- **Method:** Loose-file\
---
### 3.83 Transparent Cockpit Windows

- **Author:** WildKarrde
- **Download:** [Mod](https://deadlystream.com/files/file/2355-transparent-cockpit-windows-for-tsl/)
- **Method:** TSLPatcher\
**Download instructions:** I recommend the reskin-friendly version; the reflectivity version is untested with the builds and may look odd.\
**Installation instructions:** Apply the main installation, then go into the Compatibility Patches folder and apply any of the following you use in this order: K2CP ("K2CP and_or Nar Shaddaa Landing Pad Repair by PapaZinos"), "High Quality Skyboxes II by Kexikus" (but NOT the 'M4-78 with HQ Skyboxes II' folder!), and "Spark Effect - Ebon Hawk by PapaZinos". DO NOT USE the content of the "Korriban Distorted Model Fix" folder, even if you are on the Aspyr patch! With the 3C-FD patcher, this is no longer a concern.

---
### 3.84 HD Cockpit Skyboxes

- **Author:** tjsase
- **Download:** [Mod](http://deadlystream.com/files/file/931-hd-cockpit-skyboxes/)
- **Method:** Loose-file\
**Download instructions:** Download the version of the mod you would like based upon how detailed you want the cockpit skyboxes to appear. Keep in mind that load time into the Ebon Hawk could be significantly increased if using very large cockpit textures, and there's also a risk of save corruption when using very large texture sizes—I recommend the Medium texture option for the best balance of quality and size/performance. Whatever size you decide to use, make sure to use the .tpc format files!\
**Installation instructions:** Move the loose files to the override, followed by the file in the "With Nar Realistic Skybox" folder if you use HQ Skyboxes II.

---
### 3.85 FTL Loop

- **Author:** Nym182
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1161?tab=description)
- **Method:** Loose-file\
---
### 3.86 Aleema Keto's Robe Fix

- **Author:** milestails
- **Download:** [Mod](http://deadlystream.com/files/file/842-aleema-ketos-robe-description-correction/)
- **Method:** Loose-file\
**Download instructions:** Download the larger of the two files.\
---
### 3.87 Short-Term Memory Fix

- **Author:** SuperChameau
- **Download:** [Mod](https://deadlystream.com/files/file/2654-vaklu-short-term-memory-fix/)
- **Method:** HoloPatcher\
**Installation instructions:** Recommend Drew's fix, as it preserves more of the original dialogue.

---
### 3.88 Onderon News Makes Sense

- **Author:** SuperChameau
- **Download:** [Mod](https://deadlystream.com/files/file/2655-onderon-news-make-sense/)
- **Method:** HoloPatcher\
---
### 3.89 Hawk Downloadable Map

- **Author:** Ashton Scorpius
- **Download:** [Mod](https://deadlystream.com/files/file/1406-tsl-ebon-hawk-downloadable-map/)
- **Method:** HoloPatcher\
---
### 3.90 Kinrath Egg Crystal Drop

- **Author:** Hassat Hunter
- **Download:** [Mod](http://deadlystream.com/files/file/167-kinrath-egg-bash-crystal-drop/)
- **Method:** Loose-file\
---
### 3.91 Thorium Charge Mod

- **Author:** darth_gil
- **Download:** [Mod](http://deadlystream.com/files/file/147-thorium-charge-mod/)
- **Method:** Loose-file\
---
### 3.92 Kill the Ithorian

- **Author:** Markus Ramikin
- **Download:** [Mod](http://deadlystream.com/files/file/10-kill-the-ithorian/)
- **Method:** Loose-file\
---
### 3.93 Red Floating Lightsabers

- **Author:** Crimson Knight
- **Download:** [Mod](https://deadlystream.com/files/file/2635-red-floating-lightsabers/)
- **Method:** Loose-file\
---
### 3.94 Mira or Hanharr

- **Author:** Hassat Hunter
- **Download:** [Mod](http://deadlystream.com/files/file/108-choose-mira-or-hanharr/)
- **Method:** Loose-file\
---
### 3.95 Kreia's Fall Cutscene

- **Author:** danil-ch
- **Download:** [Mod](https://deadlystream.com/files/file/1228-kreias-fall-cutscene-in-game/)
- **Method:** TSLPatcher\
---
### 3.96 PartySwap

- **Author:** DarthTyren & Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/544-partyswap/)
- **Method:** HoloPatcher\
**Installation instructions:** Run the HoloPatcher executable. Select the default install, not M4-78, then re-run the installer, select the "ADD-ON: PartySwap Item" install option from the drop-down, and install that as well (without it, you won't be able to actually switch between the companions). When the install is completed, go into the "Compatibility Patches" folder, enter the one for Kreia's Fall Ingame Cutscene, and install that patch as well if you've chosen to use the above mod.

---
### 3.97 Extended Enclave

- **Author:** danil-ch & Darth Hayze
- **Download:** [Mod](http://deadlystream.com/files/file/428-extended-enclave-tslrcm-add-on/)
- **Method:** TSLPatcher\
---
### 3.98 PartySwap-EE Compatch

- **Author:** Leilukin
- **Download:** [Patch](https://deadlystream.com/files/file/1304-partyswap-and-extended-enclave-compatibility-patch/)
- **Method:** TSLPatcher\
**Installation instructions:** Use the 'No M4-78EP Installed' option. The 'Extended Enclave Tweaks' is a separate mod we don't use in this build.

---
### 3.99 Extended Korriban Arrival

- **Author:** danil-ch
- **Download:** [Mod](http://deadlystream.com/files/file/250-extended-korriban-arrival/)
- **Method:** TSLPatcher\
---
### 3.100 Prologue Item Recovery

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2211-prologue-item-recovery/)
- **Method:** TSLPatcher\
**Installation instructions:** Use the TSLPatcher installer method (mandatory for compatibility), not the manual install.

---
### 3.101 Balance Tweak Pack

- **Author:** Pavijan
- **Download:** [Mod](https://deadlystream.com/files/file/1790-balance-tweak-pack/)
- **Method:** TSLPatcher\
**Installation instructions:** Run the installers for Force Crush Balance and Disable Droid Interface Feat. The other mod options are untested with the builds and I don't personally recommend them.

---
### 3.102 Mines Overhaul

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2753-mines-overhaul-tsl/)
- **Method:** HoloPatcher\
**Installation instructions:** Recommend running all three options, the main install first and then the two optionals.

---
### 3.103 No Health Regeneration

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2530-no-health-regeneration/)
- **Method:** HoloPatcher\
**Installation instructions:** The option to gradually restore health while on the Ebon Hawk is compatible with the builds--if you'd like to use it, re-run the HoloPatcher and install that option after installing the base mod first.

---
### 3.104 Thematic Sith Lords

- **Author:** Sniggles & JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/1535-thematic-sith-lords/)
- **Method:** TSLPatcher\
**Installation instructions:** First choose your base install option, either Standard or No Force Rating (the latter removes the inherent DS alignment bonus to saves in some modules, which also gives an equivalent malus to LS characters in those modules). After this is installed, if you would like for Visas to ambush you as a Sith Assassin (which is a very difficult fight—remember, she will have Sneak Attack, and that fight forcibly stuns you), re-run the patcher and also install that option.

---
### 3.105 Thematic Jedi Masters

- **Author:** Sniggles & JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2633-thematic-jedi-masters/)
- **Method:** TSLPatcher\
---
### 3.106 Better Disciple Meditation

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2612-better-disciple-meditation/)
- **Method:** TSLPatcher\
---
### 3.107 Bao-Dur & Heavy Armor

- **Author:** Effix
- **Download:** [Mod](https://deadlystream.com/files/file/2189-bao-dur-can-wear-heavy-armor/)
- **Method:** TSLPatcher\
---
### 3.108 JC's Crystal Attunement

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2269-jcs-crystal-attunement-for-k2/)
- **Method:** TSLPatcher\
**Installation instructions:** Practically speaking there are only two relevant install options: "Class-Based Properties + Workbench Attunement", which is the full package, or "Bug Fixes Only". If you don't like the mod's changes but would like to have its bugfixes, install the latter; otherwise, install the former.

---
### 3.109 Jekk'Jekk'Tarr Thugs

- **Author:** SuperChameau
- **Download:** [Mod](https://deadlystream.com/files/file/2684-better-jekkjekk-tarr-thugs/)
- **Method:** HoloPatcher\
---
### 3.110 Logical Jekk'Jekk Tarr

- **Author:** N-DReW25
- **Download:** [Mod](https://deadlystream.com/files/file/2790-logical-jekkjekk-tarr/)
- **Method:** HoloPatcher\
**Installation instructions:** Install part 1 and then part 2, then, if using Better Jekk'Jekk Tarr Thugs, also install the compatch.

---
### 3.111 Mira's Vanilla Escape

- **Author:** WildKarrde
- **Download:** [Mod](https://deadlystream.com/files/file/2671-miras-vanilla-escape-for-tslrcm/)
- **Method:** TSLPatcher\
**Installation instructions:** I recommend the "With Additional Scene" option for maximum restored content and internal consistency for the sequence.

---
### 3.112 Kreia's Longsword

- **Author:** bead-v
- **Download:** [Mod](https://deadlystream.com/files/file/1538-kreias-lightsaber-long-sword/)
- **Method:** TSLPatcher\
**Installation instructions:** The lightsaber version of this mod is broken when used alongside the mod builds, so please ensure to use specifically the longsword version.

---
### 3.113 Harbinger Performance Fix

- **Author:** PapaZinos
- **Download:** [Mod](https://deadlystream.com/files/file/2027-harbingers-arrival-performance-enhancement-for-tslrcm/)
- **Method:** TSLPatcher\
**Installation instructions:** Use the installer version.

---
### 3.114 Visas VO Tweak

- **Author:** danil-ch
- **Download:** [Mod](http://deadlystream.com/files/file/431-nihilusvisas-scene-vo-tweak/)
- **Method:** Loose-file\
---
### 3.115 Sion and a Male Exile

- **Author:** Leilukin
- **Download:** [Mod](http://deadlystream.com/files/file/996-darth-sion-and-male-exile-mod/)
- **Method:** HoloPatcher\
---
### 3.116 Assassins with Lightsabers

- **Author:** Lewok2007
- **Download:** [Mod](https://deadlystream.com/files/file/2631-sith-assassins-with-lightsabers/)
- **Method:** HoloPatcher\
---
### 3.117 True Sith Assassins

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2649-true-sith-assassins-awareness-restoration/)
- **Method:** Multi-Run HoloPatcher\
**Installation instructions:** Unless you intend on playing a character with very high awareness, I recommend the reduced difficulty option if using Lewok's Sith Assassins with Lightsabers, because the damage will be ridiculous. Remember to also apply the compatch for Lewok's mod after running the main install option of your choice, if using it.

---
### 3.118 For Mandalore!

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2666-for-mandalore/)
- **Method:** HoloPatcher\
**Installation instructions:** Strongly recommend using the Snigaroo Cut for balance and immersion's sake.

---
### 3.119 Peragus Medical Bay Enhancement

- **Author:** WildKarrde
- **Download:** [Mod](https://deadlystream.com/files/file/2513-peragus-medical-bay-enhancement/)
- **Method:** TSLPatcher\
**Installation instructions:** When installing, for best internal consistency choose install options 1 or 2 (not underwear). Option 2 is technically the most consistent but the visual differentiation is very slight and likely would not be noticeable. When the install is completed, if you would like the miners to have burned skin (as they realistically would have had) move the files from the "OPTION - Burned Skin Textures" folder (or the upscaled textures therein) to your override.

---
### 3.120 HQ Blasters

- **Author:** Sithspecter
- **Download:** [Mod](http://deadlystream.com/files/file/915-high-quality-blasters/)
- **Method:** TSLPatcher\
---
### 3.121 Droid Model Fix

- **Author:** CaptainSpoque
- **Download:** [Mod](https://deadlystream.com/files/file/2748-droid-models-animation-fix/)
- **Method:** Loose-file\
**Installation instructions:** Move all the various files inside the 7 folders within the "TSL Version" folder, EXCEPT for "War Droid K1," if using HQ Blasters above.

---
### 3.122 Quarterstaff Replacements

- **Author:** DeadMan
- **Download:** [Mod](http://deadlystream.com/files/file/218-quarterstaff-replacement-pack/)
- **Method:** TSLPatcher\
---
### 3.123 Upscaled Icon Overhaul

- **Author:** Pramod Marlon
- **Download:** [Mod](https://deadlystream.com/files/file/1536-tsl-ai-upscaled-icon-overhaul/)
- **Method:** Loose-file\
**Installation instructions:** Delete if_finesse01.tga, if_finesse02.tga, iw_dblsbr_010.tga, iw_dsrptpstl_001.tga, iw_dsrptpstl_002.tga, iw_dsrptpstl_003.tga, iw_dsrptpstl_004.tga,iw_Lghtsbr_011.tga, iw_qtrstaff_001.tga, iw_qtrstaff_002.tga, and iw_qtrstaff_003.tga before moving the files to the override and overwriting any conflicts.

---
### 3.124 Rescaled Trandoshans

- **Author:** Schizo
- **Download:** [Mod](https://deadlystream.com/files/file/946-re-scaled-trandoshans/)
- **Method:** TSLPatcher\
---
### 3.125 Visually Repair HK

- **Author:** Kexikus
- **Download:** [Mod](https://deadlystream.com/files/file/1434-visually-repair-hk-47/)
- **Method:** TSLPatcher\
**Installation instructions:** Select between one of the two TSLRCM-compatible install options.

---
### 3.126 Expanded Ending

- **Author:** WildKarrde
- **Download:** [Mod](https://deadlystream.com/files/file/2672-tsl-expanded-ending/)
- **Method:** TSLPatcher\
**Installation instructions:** If you are NOT playing the game on a 4:3 aspect ratio monitor, regardless of what your aspect ratio is, install the 16:9 main install option. Then re-run the patcher and apply the Transparent Cockpit Windows - Retexture Friendly option, if using the Transparent Cockpit Windows mod.

---
### 3.127 Consistent Bastila Recognition

- **Author:** Leilukin
- **Download:** [Mod](https://deadlystream.com/files/file/2695-consistent-bastila-recognition/)
- **Method:** HoloPatcher\
**Installation instructions:** Run the patcher using the Default install option, then re-run and apply the Expanded Ending compatch, if using Expanded Ending.

---
### 3.128 Handmaiden Fit Model & Patch

- **Author:** Fair Strides, patch by JCarter426
- **Download:** [Mod](http://deadlystream.com/files/file/846-handmaiden-fit-and-athletic/) [Patch](https://mega.nz/#!gcxRTYTJ!ILbLFRyGEr4lGZYDOLN_Qg17fCm-TJw4Y1RDuy4WiWI)
- **Method:** TSLPatcher & Loose-File Patch\
**Installation instructions:** Ignore all the loose files in the folder; use the TSLPatcher to install the mod. Then copy the two files from the patch into override.

---
### 3.129 JC's Handmaiden Sisters

- **Author:** JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/810-jcs-handmaiden-sisters/)
- **Method:** TSLPatcher\
---
### 3.130 Replacement Loadscreens

- **Author:** Sith Holocron
- **Download:** [Mod](https://deadlystream.com/files/file/1255-replacement-loading-screens-for-kotor2-original-pack-with-or-without-tslrcm-part-1/) [Mod](https://deadlystream.com/files/file/1256-replacement-loading-screens-for-kotor2-original-pack-with-or-without-tslrcm-part-2/) [Mod](https://deadlystream.com/files/file/1257-replacement-loading-screens-for-kotor2-original-pack-with-or-without-tslrcm-part-3/)
- **Method:** Loose-file\
**Installation instructions:** Move all the files but load_301NARa (in Part 2) to the override.

---
### 3.131 Vibrocutter Changes

- **Author:** Lewok2007
- **Download:** [Mod](https://deadlystream.com/files/file/2670-vibrocutter-changes/)
- **Method:** HoloPatcher\
**Installation instructions:** Recommend the "Location and Medpac" install option, it gives the player an extra medpac as compensation for having to fight the first droids with a plasma torch.

---
### 3.132 Peragus Monitor Adjust

- **Author:** Sith Holocron
- **Download:** [Mod](http://deadlystream.com/files/file/317-peragus-large-monitor-adjustment/)
- **Method:** Loose-file\
**Installation instructions:** Use the files in the "Alternate Textures" folder.

---
### 3.133 Replacement Peragus II

- **Author:** Sith Holocron
- **Download:** [Mod](http://deadlystream.com/files/file/361-replacement-peragus-ii-artwork-by-trench/)
- **Method:** Loose-file\
**Installation instructions:** Move the files from the Original folder to the override, as well as the file from the "One Replacement Screen" folder if using Peragus Large Monitor Adjustment.

---
### 3.134 TSL Galaxymap Fixpack

- **Author:** bead-v, Kexikus, and Sith Holocron
- **Download:** [Mod](http://deadlystream.com/files/file/1057-tsl-galaxy-map-fix-pack/)
- **Method:** TSLPatcher\
**Installation instructions:** Install the Vanilla/TSLRCM option.

---
### 3.135 Fixed Hologram Models

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1201-fixed-hologram-models-and-admiralty-redux-for-tslrcm/)
- **Method:** TSLPatcher\
**Download instructions:** Download just the main file, not the robes patch.\
---
### 3.136 Relighting TSL

- **Author:** J
- **Download:** [Mod](https://deadlystream.com/files/file/2752-relighting-tsl-early-release/)
- **Method:** Loose-file\
**Download instructions:** Download and apply all files, unless NOT using TSLRCM (in which case, skip relightingtsl_298TELk_1.0.zip).\
---
### 3.137 Companion Clothes

- **Author:** Ol' Cappy
- **Download:** [Mod](https://deadlystream.com/files/file/2145-k2-companion-starting-armors/)
- **Method:** TSLPatcher\
---
### 3.138 Improved Enlightenment/Corruption

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2577-improved-ls-enlightenment-ds-corruption-feats/)
- **Method:** Loose-file\
---
### 3.139 Repair Affects Stun Droid

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2436-repair-affects-stun-droid-tsl/)
- **Method:** TSLPatcher\
---
### 3.140 Improved Force Sight

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2651-improved-force-sight/)
- **Method:** HoloPatcher\
**Installation instructions:** Recommend installing all three modules.

---
### 3.141 Alignment Affects Force Powers

- **Author:** offthegridmorty
- **Download:** [Mod](https://deadlystream.com/files/file/2815-alignment-affects-force-powers-tsl/)
- **Method:** TSLPatcher\
**Installation instructions:** I strongly recommend the combined install of "Alignment Affects Force Powers + Treat Injury Affects Force Healing."

---
### 3.142 Ultimate Character Overhaul Patches

- **Author:** ShiningRedHD
- **Download:** [Patch](https://www.nexusmods.com/kotor2/mods/1060?tab=files)
- **Method:** Loose-file\
**Installation instructions:** Scroll down to the "optional files" section of the mod page. You will install the compatches for all the content you chose to install, in the following order: TSLRCM The K2CP, ensuring to delete C_DrdAstro01.tga, C_DrdAstro02.tga, C_DrdAstro03.tga, C_Hutt03.tga, C_Kinrath01.tga, C_Kinrath02.tga, C_Kinrath03.tga, C_Kinrath04.tga, C_SenBall01D.tga, p_hk47_01.tga, C_hk50.tga, and C_hk51.tga before moving to your override. If utilizing Darth Sapiens's HD Visas mod, also delete P_VisasH01.tga, P_VisasHD01.tga and P_VisasHD02.tga. JC's Minor Fixes All remaining content that matches content you chose to use from the builds (skipping Better Twi'lek Male Heads, if using Leilukin's Male Twi'lek Diversity mod)

---
### 3.143 Bao-Dur/Darth Maul

- **Author:** Nimduril
- **Download:** [Mod](https://mega.nz/#!BJgCDJLY!miLH-LcFEgiRWlmfWixicFdn1o_uoFHb76g9NOo0CHM)
- **Method:** Loose-file\
---
### 3.144 Realistic Visual Effects

- **Author:** Shem
- **Download:** [Mod](http://deadlystream.com/files/file/735-realistic-visual-effects/)
- **Method:** TSLPatcher\
---
### 3.145 Remove Duplicate TGA/TPC

- **Author:** Flachzangen, Malacand for the .sh script
- **Download:** [Mod](https://www.nexusmods.com/kotor/mods/1384) [Mod](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/scripts/k2/tpc-deduper.sh)
- **Method:** .bat Patcher, .sh script\
**Installation instructions:** For Windows: Place DelDuplicateTGA-TPC in your main game folder (NOT override!), run it, say that TPC should be deleted and do not manually confirm. If you are on a Mac or other device that cannot run .bat files, you can also try downloading the [3C-FD tool](https://github.com/J0-o/3C-FD-Patcher) to identify the duplicates. If you aren't comfortable with downloading C3-FD, a list of all the files you will need to manually delete can be found [here](/modding/mod_builds/k2/delete). MAKE SURE THIS SCRIPT RUNS PROPERLY! On some operating systems, overzealous antivirus setups, or filepaths with particular characters in them it may fail. If the file outputs "Finished, Press any key to continue" but does not list any files it deleted, it is not working, and if it does not work it will crash your game. You can try to resolve this by moving your Override folder to a different location (I recommend a subfolder in your Documents or Downloads directories), putting the .bat file there and running it through that directory, but if that doesn't work you will need to manually go through and delete the duplicates from the link above. For Linux/Mac: Download the script from the linked GitHub page. For Mac, it can be run with the "zsh" command. The script does assume you're using the default installation path for the Steam version; if you aren't, you just need to change the GAMEDIR variable at the top of the script to point to your game folder (NOT your override folder) before you run it. You may have to run the script twice, if a given TPC file has BOTH a matching TGA file and a matching DDS file.

---
### 3.146 TOMB

- **Author:** Sniggles & JCarter426
- **Download:** [Mod](https://deadlystream.com/files/file/2663-thematic-obscured-mausoleum-burial/)
- **Method:** TSLPatcher\
---
### 3.147 Character Textures & Model Fixes

- **Author:** Redrob41
- **Download:** [Mod](https://deadlystream.com/files/file/2660-4x-upscale-character-textures-model-fixes-tsl/)
- **Method:** Loose-file\
**Download instructions:** Strongly recommend the 2x .tpc version; the fidelity loss for 2x is minimal, .tpc is a lossless conversion and is much slimmer in filesize, and the automated compatibility program for this mod relies on the filetype being .tpc to function.\
**Installation instructions:** If you are on a system which can run .bat files, I strongly recommend using the automated system to deal with compatibility for this mod. To do so, first extract redrob's mod from its archive, then enter the "TSL Optional Kreia Model" folder, copy the four model files within, paste them into the "Copy contents to TSL's Override folder" and overwrite. After this, navigate to [this page](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/scripts/cleaner.bat) and click on the button with the arrow pointing down at the top of the code list (the one which says "download raw file"). Place cleaner.bat in the folder from redrob's mod called "Copy contents to TSL's Override folder", then go to [here](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/scripts/cleanlist_k2.txt) and repeat the same step, placing cleanlist_k2.txt in the same location. You can now run cleanlist.bat: follow the instructions onscreen, selecting whether you did or didn't use any of the given mods (note that the first thing it will ask you is whether you've installed "Mandatory Deletions"; rather than a mod, this is a required step to delete files that need to be removed regardless of what mods you're using, so just approve it). The batch file will automatically delete the incompatible files based on which mods you select that you've used in your install. Once you reach the end of the list, you can exit the .bat window, delete cleaner.bat and cleanlist_k1_sf.txt, and then move the remaining files in the folder to your override. If you cannot run .bat files or feel uncomfortable running this file, you will need to manually delete the files yourself, following the instructions [here](https://github.com/KOTOR-Community-Portal/mod-builds/blob/main/content/k2/redrob_deletionsk2.md).

---
### 3.148 Main Menu Fix

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1138-tsl-main-menu-model-fix-for-widescreen/)
- **Method:** Loose-file\
**Installation instructions:** Apply the contents of the "for override folder". If you would like to have the TSLRCM version of the KOTOR 2 logo on your main menu, you will need to BOTH move the contents of the "FOR TSLRCM" folder to your override, as well as the contents of the separate download "Updated_TSLRCM_Logo_v1.8.6".

---
### 3.149 K2 Cutscenes Rescaled

- **Author:** Pops Maellard
- **Download:** [Mod](https://deadlystream.com/files/file/2503-k2-cutscenes-rescaled/)
- **Method:** Loose-file\
**Download instructions:** Choose the resolution option which most closely fits your monitor's screen size during the download process. If using TSLRCM or Extended Enclave, download both the main file most closely corresponding to your monitor resolution as well as the file of the same resolution with "_mods" appended to the filename (for instance, k2rs_30fps_1920x1080.7z and k2rs_30fps_mods_1920x1080.7z).\
**Installation instructions:** When installing, there will be several optional files based on how dialogue in cutscenes are displayed (floating text or not, etc). Which of these you choose is your preference; use the mod screenshots to determine. Install the main module first, then open the "mods" version of the file and apply the upscaled cutscenes for any mods which you use from the main build list. Bear in mind that the files from this mod go in your movies folder, not override. If you experience issues with the game minimizing during cutscenes, it might be necessary to go to [this video](https://www.youtube.com/watch?v=l7euNu1Tt5E) and follow the instructions to use RAD tools to "upscale" the cutscenes to match your exact resolution, though I have not personally attempted this so I don't know how much time it would take to complete. I would estimate around 8 hours, which is the typical time it takes for the native movies to be scaled to 1920x1080 using the same system, but remember that this would be a fully-automated process.

---
### 3.150 K2 Remastered Cutscenes

- **Author:** naelavok
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1066/)
- **Method:** Loose-File Components, possible .bat patcher\
**Installation instructions:** Use only Pops Maellard's cutscenes or this version by naelavok. To install, choose the resolution option which most closely fits your monitor's screen size during the download process. Bear in mind that the files from this mod go in your movies folder, not override. If you experience issues with the game minimizing during cutscenes, it might be necessary to go to [this video](https://www.youtube.com/watch?v=l7euNu1Tt5E) and follow the instructions to use RAD tools to "upscale" the cutscenes to match your exact resolution, though I have not personally attempted this so I don't know how much time it would take to complete. I would estimate around 8 hours, which is the typical time it takes for the native movies to be scaled to 1920x1080 using the same system, but remember that this would be a fully-automated process.

---
### 3.151 Loading Screen Rescaled

- **Author:** Pops Maellard
- **Download:** [Mod](https://deadlystream.com/files/file/2622-k2-loading-screen-rescaled/)
- **Method:** Loose-file\
---
### 3.152 Workbench Camera Tweak

- **Author:** DarthParametric
- **Download:** [Mod](https://deadlystream.com/files/file/1743-workbench-upgrade-screen-camera-tweak-for-tsl/)
- **Method:** Loose-file\
---
### 3.153 Upscaled Maps

- **Author:** Tunalex
- **Download:** [Mod](https://www.nexusmods.com/kotor2/mods/1086)
- **Method:** Loose-file\
---
## 4 Bugs, Issues, & Extras

### 4.1 Out of VRAM

#### 4.1.1 Extra Downscales

##### 4.1.1.1 Lower city apartments

Consistent crash
