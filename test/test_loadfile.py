#--------------------------------------------------------------------
#Administration Details
#--------------------------------------------------------------------
__author__ = "Mats Larsen"
__copyright__ = "Mats Larsen 2014"
__credits__ = ["Mats Larsen"]
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"
__description__ = "Module is for testing of loading any kind of format file based on setups. It can also be a database file. E.q. file in a list form. A path has be be given to be able to find it. "
__file__ = "test_loadfile.py"
__class__ ="TestLoadFile"
__dependencies__ = []
#--------------------------------------------------------------------
#Version
#--------------------------------------------------------------------
__version_stage__ = "Pre_alpha"
__version_number__ = "0.1"
__version_date__ = "20140917"
__version_risk__ = "This current version is in Pre-alpha version, which meaning that the program can crash or perform other unrespected behavoiurs."
__version_modification__ = "The development project has just been created."
__version_next_update__ = "Implementation of more messeages."
#--------------------------------------------------------------------
#Hardware
#--------------------------------------------------------------------
"""
This project is not releated to any kind of hardware, like GPIOs.
"""
#-------------------------------------------------------------------
#Import
#-------------------------------------------------------------------
import traceback
import os
from loadfile import LoadFile
#--------------------------------------------------------------------
#CONSTANTS
#--------------------------------------------------------------------
LOG_LEVEL = 2 # Information level
LOG_ALWAYS = 3 # Always log data
#--------------------------------------------------------------------
#METHODS
#--------------------------------------------------------------------
def log(msg, log_level=LOG_LEVEL):
    """
    Print a message, and track, where the log is invoked
    Input:
    -msg: message to be printed, ''
    -log_level: informationlevel, i
    """
    global LOG_LEVEL
    if log_level <= LOG_LEVEL:
        print(str(log_level) + ' : ' + __file__ + '.py::' + traceback.extract_stack()[-2][2] + ' : ' + msg)

path = 'debuggingModule_pins_setup.txt'
lf = LoadFile(name='test_load',path=path,col_number=5)
data = lf.data
#print(data)
log('Print of First row...........')
#print(data[0][0])
for i in range(0,5):
    print(data[0][i])
data[0][0] = 'sdsdsd'
log('Get a copy of the instance..............')
print(lf.copy_data())
print(lf)

