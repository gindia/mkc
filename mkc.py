"""
Setsup A C language project environment under Windows.
Copyright 2021 Omar M.Gindia.
"""

import sys
import os
import datetime

license = {
        "MIT": """MIT License

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
    Sets up a C language project environment under Windows.
    """
    folder_name = os.path.basename(os.getcwd())
    YEAR: str = str(datetime.datetime.now().year)

    Project_Name: str = input(f"Project Name ({folder_name}): ")
    if Project_Name == "":
        Project_Name = folder_name

    Project_Description: str = input(f"Project Description: ")
    Author_Name: str = input(f"Author Name: ")

    License_Type: str = input(f"License Type (MIT): ")
    if License_Type == "":
        License_Type = "MIT"

    # Directories
    os.makedirs("target", exist_ok=True) # output directory
    os.makedirs("assets", exist_ok=True)
    os.makedirs("code",   exist_ok=True) # source code directory

    # files
    with open("code/main.c", "w") as f:
        f.write(f"""/* (C) Copyright {YEAR} {Author_Name}. */
#include <stdio.h>
int main(void) {{
  return 0;
}}""")

    with open("build.bat", "w") as f:
        f.write(f"""@echo off
pushd target
cl.exe -nologo -EHsc -Wall -wd4201 -wd5045 -DDEBUG:1 -Zi ../code/main.c -fp:fast -Fe:{Project_Name}.exe -link -INCREMENTAL:NO -DEBUG:FULL
popd
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
