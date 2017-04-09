#####################################
#   Class Time
#####################################

class Time( object ):
    
    def __init__(self, hour=0, mins=0, secs=0):
        ''' 
        Initializes the variables, constructs a time using three integers
        '''
        self.__hour = hour
        self.__mins = mins
        self.__secs = secs
        
    def __repr__( self ):
        '''
        Return a string with the format "Class Time: hh:mm:ss"
        '''
        out_str = "Class Time: {:02d}:{:02d}:{:02d}".format(self.__hour, \
        self.__mins, self.__secs)
        
        return out_str
        
    def __str__( self ):
        '''
        Return a string with the format "hh:mm:ss:"
        '''
        out_str = "{:02d}:{:02d}:{:02d}".format(self.__hour, \
        self.__mins, self.__secs)
        
        return out_str
        
    def from_str( self, input_str ):
        '''
        Returns an object of type Time using string slicing
        '''
        input_str.strip()
        self.__hour = int(input_str[0:2])
        self.__mins = int(input_str[3:5])
        self.__secs = int(input_str[6:8])
        



###############################
#   clockDemo.py
##############################

A = Time(6, 34, 44)
print( A )

B = Time()
B.from_str("04:52:31")
B