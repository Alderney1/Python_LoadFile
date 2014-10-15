#--------------------------------------------------------------------
#Administration Details
#--------------------------------------------------------------------
__author__ = "Mats Larsen"
__copyright__ = "Mats Larsen 2014"
__credits__ = "Mats Larsen"
__license__ = "GPLv3"
__maintainer__ = "Mats Larsen"
__email__ = "larsen.mats.87@gmail.com"
__status__ = "Development"
__description__ = "Module is for loading any kind of format file based on setups. It can also be a database file. E.q. file in a list form. A path has be be given to be able to find it. "
__file__ = "loadfile.py"
__class__ ="LoadFile"
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
import copy # Inport the copy functuon
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

class LoadFile(object):
    """
    This class load a file.
    """
    def __init__(self,name='LoadFile',path=None,split=':',comment='#',col_number=2):
        """
        The constuctor of the class with arguments.
        Inputs:
        name-> STR : The name of the instance.
        path-> STR : The path and name of the file that is desired to be loaded.
        comment-> STR : A list of elements that have to be ignored.
        col_number-> int : The number of how many columes that are used.
        """
        print(path)
        self._name = name 
        log('Name of the path -> ' + path)
        if path != None and  os.path.exists(path):
            self._path = path
        else:
            print('Error--------')
        self._file = open(self._path,'r') # Open the desired file(path)
        self._count_lines = 0 # count the relevant lines in the file.
        col=[] # Make an array with col_number, that should contain of the file.
        for i in range(0,col_number):
            col.append([])
        #print(col)
        for line in self._file: # Loop each line in the file.
            if line.startswith(comment): # Skip the line which first one of the signs in the argumet 'comment'.
                pass 
            else: # relavant data
                self._count_lines +=1
                for x in range(0,col_number):
                    #print(col)
                    col[x].append(line.split(':')[x].strip()) # insert in the correct matrix and split with : and remove spaces.
        # Create a matrix and insert the data from the file.
                #print(col)
        self._data = [[0 for x in range(col_number)] for x in range(self._count_lines)] 
        # Inserting the data into a matrix.
        #print(col)
        #print(self._data)
        for x in range(0,self._count_lines):
            for n in range(0,col_number):
                self._data[x][n] = col[n][x]
            #print(self._data)

    def copy_data(self):
        """
        Return a complete copy of this instance data.
        """
        return copy.deepcopy(self.data)

    def get_data(self):
        """
        Return the data. Be aware that the returned object has reference to this object, so operations will affect this instance. Get cpopy method can be used instead if the instance has to be manipulated.
        """
        return self._data

    def set_data(self, new_data):
        """
        Set new data, that will override the data from the file.
        """
        self._data = new_data
    data = property(get_data,set_data, doc='Data Property')

    def get_name(self):
        """
        Return the name of the instance.
        """
        return self._name
    
    def set_name(self, new_name):
        """
        Set new name of the instance.
        """
        self._name = new_name
    name = property(get_name, set_name, doc = 'Name Property')
  
    def get_path(self):
        """
        Return the path tol this file.
        """
        return self._path

    def set_path(self,newpath):
        """
        Set a new path.
        """
        self._path = newpath
    path = property(get_path,set_path,doc='Path Property')


    def __repr__(self):
        """
        Present the data of the object.
        """
        return '----------------------------------------------------\nAdministration Details : \n' + 'author-> %s \ncopyright-> %s \ncredits-> %s \ndescription-> %s \nlicense-> %s'   % (__author__, __author__,__credits__,__description__,__license__)
# + '
