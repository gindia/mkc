# MKC
A small script to init an empty project for C/Cpp under Microsoft Windows, using cl.exe compiler.

## deps
1. git (also uses lfs).
1. python.
1. GNU Make.

## How to use?
1. make a folder and place the script in it.
1. run `py mkc.py`
1. done..

## Folder structure.
```
Project_Name
 | - code <folder>
 | - code\main.c
 | - target <folder>
 | - assets <folder>
 | - Makefile
 | - build.bat
 | - run.bat
 | - README.md
 | - LICENSE
 | - {git stuff}.
```

## Tip.
insted of copying the file all around. you can do the following.
1. add the script to a folder.
1. add the folder to %PATH%
1. create a `mkc.bat` file.
1. add the following to it
```bat
@echo off
py {full path to mkc.py script}
```
now under any folder run from the commandline `mkc` or `mkc.bat`.

## FAQ.
- Why GNU make?
> It integrates with my nvim workflow.
