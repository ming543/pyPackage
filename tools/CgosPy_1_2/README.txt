09-09-2016	LKA		Initial release
06-11-2019	LKA		Update for Python3 support

====================
CgosPy installation:
====================


WINDOWS:

- Install Python (Version 2 or 3) if not already done.
- Add "C:\Python27\;C:\Python27\Scripts\" or the corresponding Python3 folders to your PATH variable if not already done.
- Using the command prompt, enter the CgosPy folder where the "setup.py" file is located.
- Run "python setup.py install".


LINUX:

- In the terminal, enter the CgosPy folder where the "setup.py" file is located.
- Run "python setup.py install" as root.

--------------------------------------------

From now on, the cgos module can be accessed e.g. in the Python shell system wide using "import cgos".
The version of the cgos module can be checked by printing __version__ .
For general usage of the CGOS API please refer to the congatec operating system (CGOS) API software developers guide (CGOSAPImXX.pdf)
For Python 3 please use Version 1.2 and above.
