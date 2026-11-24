# kotor-switch-modding-tool

This is a python rewrite of DrSnuggly's [kotor-ii-switch-modding](https://github.com/DrSnuggly/kotor-ii-switch-modding). It supports both Kotor 1 & 2, and should run on any OS with Python.
It also optionally uses the same logic as my tga2tpc-py to automatically convert .tga files to .tpc

Currently W.I.P. Basic commands are working, but bugs still exist:
    YesNo questions need consistent formatting
    Downscaling is doing something, but the resulting files are the same size
    Downscaling is done one file at a time
    TPC to TGA is one file at a time
    TGA to TPC is one file at a time
    Haven't added specific file fixes from fixRandomTextures.sh
