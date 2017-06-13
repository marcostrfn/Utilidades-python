#-------------------------------------------------------------------------------
# Name:        FunctionName
# Purpose:
#
# Author:      Marcos Trampal <marcos.trfn@gmail.com>
#
# Created:     06/03/2013
# Copyright:   (c) marcos.trfn@gmail.com
# Licence:     GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

__author__ = 'Marcos Trampal <marcos.trfn@gmail.com>'
__copyright__ = 'Copyright (c) marcos.trfn@gmail.com'
__license__ = 'GPL'


import inspect

# functions
def whoami():
	try:
		return inspect.stack()[1][3]
	except:
		return None
	
def whosdaddy():
	try:
		return inspect.stack()[2][3]
	except:
		return None

