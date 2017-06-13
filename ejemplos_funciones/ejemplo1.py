

'''Cadena de descripción del módulo

Puede tener una línea de encabezado,
y después uno o más párrafos de explicación...'''

__author__ = 'xxxx xxxx'
__date__ = 'xxxx xxxx'
__version__ = 'xxxx xxxx'
__credits__ = 'xxxx xxxx'
__text__ = 'xxxx xxxx'
__file__ = 'xxxx xxxx'


import sys
import os
import winshell

for i in range(0,100):
	try:
		print "{} {}".format(i,winshell.folder(i))
	except:
		pass


from funciones.files import findFiles
from funciones.util.functionName import whoami, whosdaddy
from funciones.log.log import get_file_log, get_log, log_constantes

# NIVELES DE LOG logger = log.fileLog(log_name, NIVEL)
CRITICAL = 50
ERROR = 40
WARNING = 30
INFO = 20
DEBUG = 10
NOTSET = 0

print whoami(), whosdaddy()
print log_constantes.DEBUG	

log_name = os.path.abspath(os.path.join(os.path.dirname(__file__),__file__.split('.py')[0]))
logger = get_log(log_name, log_constantes.DEBUG)

logger.debug("[%s - %s] - %s " % (whoami(), whosdaddy(), 'response=ok'))

sys.exit()

dir_source = "c:\\tmp"
for file in findFiles.get_files_recursive_yield(dir_source, None):		
	print file