#-------------------------------------------------------------------------------
# Name:		   Log
# Purpose:
#
# Author:	   Marcos Trampal <marcos.trfn@gmail.com>
#
# Created:	   06/03/2013
# Copyright:   (c) marcos.trfn@gmail.com
# Licence:	   GPL
#-------------------------------------------------------------------------------
#!/usr/bin/env python

#-------------------------------------------------------------------------------
# info:
# Level		  value
# CRITICAL	  50
# ERROR		  40
# WARNING	  30
# INFO		  20
# DEBUG		  10
# NOTSET	  0
#-------------------------------------------------------------------------------

__author__ = 'Marcos Trampal <marcos.trfn@gmail.com>'
__copyright__ = 'Copyright (c) marcos.trfn@gmail.com'
__license__ = 'GPL'

import logging
import datetime
import os

'''
log_name = os.path.abspath(os.path.join(os.path.dirname(__file__),__file__.split('.py')[0]))
logger = get_file_log(log_name, log_constantes.DEBUG)
logger.debug("[%s - %s] - %s " % (whoami(), whosdaddy(), 'response=ok'))
'''

class log_constantes:
	CRITICAL = 50
	ERROR = 40
	WARNING =	  30
	INFO =  20
	DEBUG =   10
	NOTSET =  0

def get_log(file_name='log', tipo=10):
	# create logger

	name = os.path.basename(file_name)
	
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)

	# log a pantalla
	ch = logging.StreamHandler()
	ch.setLevel(tipo)

	# create formatter
	f = '%(asctime)s - %(levelname)s - %(message)s'
	formatter = logging.Formatter(f)
	# add formatter to ch
	ch.setFormatter(formatter)
	# add ch to logger
	logger.addHandler(ch)
	return logger
	
def get_file_log(file_name='log', tipo=10):
	# create logger

	name = os.path.basename(file_name)
	
	logger = logging.getLogger(name)
	logger.setLevel(logging.DEBUG)

	# log a fichero
	file_log = str(datetime.date.today()) + '.' + name + '.log'
	name_file_log = os.path.abspath(os.path.join(
	   os.path.dirname(__file__),"..","log", file_log ))

	ch = logging.FileHandler(name_file_log)
	ch.setLevel(tipo)
	# create formatter
	f = '%(asctime)s - %(levelname)s - %(message)s'
	formatter = logging.Formatter(f)
	# add formatter to ch
	ch.setFormatter(formatter)
	# add ch to logger
	logger.addHandler(ch)
	return logger

