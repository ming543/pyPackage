"""
Copyright (c) 2019, congatec AG. All rights reserved.

This program is free software; you can redistribute it and/or
modify it under the terms of the BSD 2-clause license which 
accompanies this distribution. 

This program is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the BSD 2-clause license for more details.

The full text of the license may be found at:        
http://opensource.org/licenses/BSD-2-Clause   

--------------------------------------------------------------

Rev 1.0   09-09-2016	LKA		Initial release.
Rev 1.1   13-03-2018	LKA		released version 1.1 - see history.txt
Rev 1.2	  20-03-2019	LKA	    released version 1.2 - see history.txt
"""

from distutils.core import setup

setup(name='cgos',
      version='1.2',
      description='ctypes wrapper for the CGOS API',
      url='http://www.congatec.com',
      author='congatec',
      author_email='info@congatec.com',
      license='BSD',
      packages=['cgos'],
)
