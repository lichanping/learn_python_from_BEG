# PyInstaller

## How to Install

### pip install pyinstaller

PyInstaller requires two Python modules in a Windows system. If you install PyInstaller using pip, and PyWin32 is not already installed, pywin32 is automatically installed. PyInstaller also requires the pefile package.

### pip install pypiwin32 

### how to resolve install timeout

- -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

### Verifying the installation

- pyinstaller --version

## How to Bundle

### to One Folder

- Steps:

	- 1. >pyinstaller myscript.py

		- the default result is a single folder named myscript. 
This folder contains all your script's dependencies, and an executable file also named myscript (myscript.exe in Windows).
		- What will PyInstaller do?

			- Writes myscript.spec in the same folder as the script.
			- Creates a folder build in the same folder as the script if it does not exist.
Writes some log files and working files in the build folder.
			- Creates a folder dist in the same folder as the script if it does not exist.
			- Writes the myscript executable folder in the dist folder.

	- 1.a. For certain uses you may edit the contents of myscript.spec. After you do this, you name the spec file to PyInstaller instead of the script:

		- >pyinstaller myscript.spec

	- 2. Compress the folder to myscript.zip and transmit it to your users.
	- 3. Your user unzip and launch the myscript executable inside it.

- Advantages

	- Easy to debug problems that occur when building the app when you use one-folder mode. 
	- You can see exactly what files PyInstaller collected into the folder.
	- When you change your code, as long as it imports exactly the same set of dependencies, you could send out only the updated myscript executable.

- Disadvantages

	-  The one folder contains a large number of files. Your user must find the myscript executable in a long list of names or among a big array of icons.
	- Your user can create a problem by accidentally dragging files out of the folder.

- -D, --onedir	Create a one-folder bundle containing an executable (default)

###  to One File

- Advantages

	- a single executable to launch

- Disadvantages

	- any related files such as a README must be distributed separately.
	- the single executable is a little slower to start up than the one-folder bundle.

- Important note

	- Before you attempt to bundle to one file, make sure your app works correctly when bundled to one folder.
It is is much easier to diagnose problems in one-folder mode.

- -F, --onefile	Create a one-file bundled executable.

### Compare the total Execution Time of the same py file

- Using PowerShell

	- PowerShell includes the built-in Measure-Command cmdlet that helps you measure the time it takes to run script blocks, cmdlets, or even external programs. 
	- Here is a sample PowerShell command-line 
which measures the times takes for the ping google.com 
command-line to finish:

Measure-Command { ping google.com | Out-Host }
	- Here is how to measure the time for executing bundled exe:

Measure-Command { .\main.exe pycharm }

-  to One File

	- TotalSeconds      : 10.9675003

- to One Folder

	- TotalSeconds      : 7.1455235

## Command General Options

### -h, --help	show this help message and exit

### -v, --version	Show program version info and exit.

### --distpath DIR	Where to put the bundled app (default: ./dist)

### -workpath WORKPATH

- Where to put all the temporary work files, .log, .pyz and etc. (default: ./build)

### -y, --noconfirm

- Replace output directory (default: SPECPATH/dist/SPECNAME) without asking for confirmation

### -a, --ascii	Do not include unicode encoding support (default: included if available)

### --clean	Clean PyInstaller cache and remove temporary files before building.

### --log-level LEVEL

- Amount of detail in build-time console messages. LEVEL may be one of TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL (default: INFO).

### -n NAME, --name NAME

- Name to assign to the bundled app and spec file (default: first scripts basename)

### -i <FILE.ico or FILE.exe,ID or FILE.icns or "NONE">, --icon <FILE.ico or FILE.exe,ID or FILE.icns or "NONE">

- FILE.ico: apply that icon to a Windows executable. FILE.exe,ID, extract the icon with ID from an exe.
- FILE.icns: apply the icon to the .app bundle on Mac OS X. Use "NONE" to not apply any icon, thereby making the OS to show some default (default: apply PyInstaller's icon)

### -w, --windowed, --noconsole

- Windows and Mac OS X: do not provide a console window for standard i/o. 
- On Mac OS X this also triggers building an OS X .app bundle. 
- On Windows this option will be set if the first script is a '.pyw' file. This option is ignored in *NIX systems.

## Running PyInstaller from Python code

### If you want to run PyInstaller from Python code, you can use the run function defined in PyInstaller.__main__.

### For instance

- import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    r'-iFacebook_icon-icons.com_66805.ico',
    '--windowed'
])

	- make sure no space after -i, seems like a defect of PyInstaller

## Running PyInstaller with Python optimizations

### Note: 

- When using this feature, you should be aware of how the Python bytecode optimization mechanism works. 
When using -O, 
1. __debug__ is set to False 
2. assert statements are removed from the bytecode. 
The -OO flag additionally removes docstrings.

### Disadvantage

-  If your code (or any module imported by your script) relies on these features, your program may break or have unexpected behavior.

### basic optimizations

- python -O -m PyInstaller main.py
- >Measure-Command {python -O -m PyInstaller main.py} 

	- TotalSeconds      : 59.0210546

### also discard docstrings

- python -OO -m PyInstaller main.py

### explicitly setting the PYTHONOPTIMIZE 
environment variable to a non-zero value

- # Windows
set PYTHONOPTIMIZE=1 && pyinstaller myscript.py
- >Measure-Command {set PYTHONOPTIMIZE=1 | PyInstaller main.py}

	- TotalSeconds      : 58.4737788

## PyInstaller Manual

### https://pyinstaller.readthedocs.io/en/stable/index.html

*XMind - Trial Version*