"""
Setup A C/C++ language project environment under Windows [using (msvc) cl compiler].
Copyright 2021 Omar M.Gindia.
"""

import sys
import os
import datetime

license = {
        "MIT" : """MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
        """,
}

def main():
    """
    Sets up a C/C++ language project environment under Windows.
    """
    folder_name = os.path.basename(os.getcwd())
    YEAR: str = str(datetime.datetime.now().year)

    Project_Name: str = input(f"Project Name ({folder_name}): ")
    if Project_Name == "":
        Project_Name = folder_name

    Project_Description: str = input(f"Project Description: ")
    Author_Name: str = input(f"Author Name: ")

    License_Type: str = input(f"License Type (NONE): ")

    Language: str = input(f"Language (C): ")
    if Language == "":
        Language = "C"

    # Directories
    os.makedirs("target", exist_ok=True) # output directory
    os.makedirs("assets", exist_ok=True)
    os.makedirs("code",   exist_ok=True) # source code directory

    file_name: str
    std: str
    if Language.lower() == "c":
        file_name = "code/main.c"
        std = "c17"
    elif Language.lower() == "c++" or Language.lower() == "cpp":
        file_name = "code/main.cpp"
        std = "c++20"
    else:
        print("Invalid Language")
        sys.exit(1)

    # files
    with open(file_name, "w") as f:
        f.write(f"""/* (C) Copyright {YEAR} {Author_Name}. */
#include <stdio.h>
int main(void) {{
  return 0;
}}""")

    with open("build.bat", "w") as f:
        f.write(f"""@ECHO off
:: The timer Reference: https://stackoverflow.com/questions/9922498/calculate-time-difference-in-windows-batch-file
REM Setting the timer
SETLOCAL EnableDelayedExpansion
SET "startTime=%time: =0%"

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:: the build environment.
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
SET EXE={Project_Name}.exe
SET COMPILATION_UNIT=../{file_name}
SET STD={std}

PUSHD target
cl -nologo %COMPILATION_UNIT% -std:%STD% -Od -EHsc -Wall -WX -wd4201 -Zi -fp:fast -link -INCREMENTAL:NO -DEBUG:FULL -OUT:%EXE%
POPD

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

REM print the time taken to compile
SET "endTime=%time: =0%"

REM Get elapsed time:
SET "end=!endTime:%time:~8,1%=%%100)*100+1!"  &  set "start=!startTime:%time:~8,1%=%%100)*100+1!"
SET /A "elap=((((10!end:%time:~2,1%=%%100)*60+1!%%100)-((((10!start:%time:~2,1%=%%100)*60+1!%%100), elap-=(elap>>31)*24*60*60*100"

REM Convert elapsed time to HH:MM:SS:CC format:
SET /A "cc=elap%%100+100,elap/=100,ss=elap%%60+100,elap/=60,mm=elap%%60+100,hh=elap/60+100"

SET GREENBACK_CYANFRONT=[102;30;4m
SET RESET=[0m
ECHO %GREENBACK_CYANFRONT%DONE%RESET% : %hh:~1%%time:~2,1%%mm:~1%%time:~2,1%%ss:~1%%time:~8,1%%cc:~1%

IF NOT %ERRORLEVEL%==0 GOTO :DONE
call run.bat
:DONE
""")
    with open("run.bat", "w") as f:
        f.write(f"""@echo off
pushd target
{Project_Name}.exe
popd
""")

    # Git
    os.system("git init") # initialize git repository
    os.system("git lfs track \"*.png\" \"*.jpg\" \"*.jpeg\" \"*.gif\" \"*.ogg\"") # track images
    with open("README.md", "w") as f:
        f.write(f"# {Project_Name}\n")
        f.write(f"{Project_Description}\n")
        f.write(f"\n")

    with open(".gitignore", "w") as f:
        f.write("""*
!**\\assets
!**\\assets\\*
!**\\code
!**\\code\\*
!.gitignore
!.gitattributes
!README.md
!LICENSE
!Makefile
!build.bat
!run.bat
""")

    with open("code/.gitignore", "w") as f:
        f.write("!*\n!.gitignore\n")

    with open("assets/.gitignore", "w") as f:
        f.write("!*\n!.gitignore\n")

    if License_Type in license.keys():
        with open("LICENSE", "w") as f:
            f.write(license[License_Type].replace("[year]", YEAR).replace("[fullname]", Author_Name))


if __name__ == "__main__":
    main()
    sys.exit(0)
